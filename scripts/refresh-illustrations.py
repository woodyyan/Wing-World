"""只更新图解和相关索引；正文、事实、词条与搜索内容保持不变。"""
from pathlib import Path
from html import escape
from html.parser import HTMLParser
import json, re, sys, xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parent.parent
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'scripts/illustrations'))
import natural,city,living,culture,rules
ART={}
for module in [natural,city,living,culture,rules]:
    for key,data in module.DIAGRAMS.items():
        assert key not in ART,key
        ET.fromstring(data['svg'])
        ART[key]=data
PLACEMENTS=json.loads((ROOT/'scripts/illustrations/placements.json').read_text())
ASSETS=json.loads((ROOT/'static-assets.json').read_text())
ENTRIES=[n for n in ASSETS if n.startswith('e-')]
assert len(ART)==53
assert set(PLACEMENTS)=={n[2:-5] for n in ENTRIES}
assert {key for values in PLACEMENTS.values() for key,n in values}==set(ART)

class Plain(HTMLParser):
    def __init__(self): super().__init__();self.parts=[]
    def handle_data(self,data):self.parts.append(data)
def plain(s):
    p=Plain();p.feed(s);return ''.join(p.parts)

def without_figures(s):return re.sub(r'<figure\b.*?</figure>','',s,flags=re.S)

def figure(key):
    d=ART[key]
    # 放大时才克隆同一SVG，不把53幅图的双份图形塞入初始文档。
    notes=''.join(f'<li><span class="note-index" aria-hidden="true">{i+1}</span><div><strong>{escape(n[0])}</strong><p>{escape(n[1])}</p></div></li>' for i,n in enumerate(d['notes']))
    return f'<figure class="diagram illustrated-plate" id="diagram-{key}" data-artwork="{key}"><div class="plate-heading"><span class="plate-type">观察图鉴 · 形制示例</span><h3>{escape(d["title"])}</h3></div>{d["svg"]}<div class="plate-observe"><span>观察一下</span>{escape(d["question"])}</div><ol class="plate-notes">{notes}</ol><details class="diagram-zoom"><summary>放大观察细节 · 可横向查看</summary><div class="diagram-zoom-scroll" data-zoom-pending="true"></div></details><figcaption><span class="diagram-label">图注</span>{escape(d["caption"])}</figcaption></figure>'

# 保存当前正文基线仅用于本次变化检查，不写入页面。
changed=[]
for name in ENTRIES:
    p=ROOT/name;s=p.read_text();id=name[2:-5]
    baseline=plain(without_figures(s))
    new=without_figures(s)
    for key,number in PLACEMENTS[id]:
        pattern=re.compile(r'(<section class="article-section" id="section-'+str(number)+r'">)(.*?)(</section>)',re.S)
        m=pattern.search(new)
        assert m,(id,number)
        new=new[:m.start()]+m.group(1)+m.group(2)+figure(key)+m.group(3)+new[m.end():]
    assert baseline==plain(without_figures(new)),id
    if new!=s:p.write_text(new);changed.append(name)

index=ROOT/'index.html';s=index.read_text();s=re.sub(r'<figure class="diagram[^\"]*" id="diagram-city".*?</figure>',figure('city'),s,flags=re.S)
s=s.replace('<span>系统图解</span><strong>16</strong>','<span>图鉴与图解</span><strong>53</strong>')
s=s.replace('图解为关系或流程示意，不表示统一的高度、距离、容量或建筑形制。','图鉴用线描、淡彩与动作草稿说明关系；人物、器物和建筑形制为示例，不规定统一高度、距离或容量。')
index.write_text(s)

# 总览保留页面框架、导航和尾部，替换图鉴正文并按主题组织。
atlas=ROOT/'atlas.html';s=atlas.read_text();start=s.index('<p class="kicker">',s.index('<main'));end=s.index('<footer class="footer">',start)
body='<p class="kicker">图鉴 · 剖切 · 动作观察</p><h1 class="page-title">图解总览</h1><p class="page-intro">53幅线描淡彩图鉴与注释草稿。从羽毛、身体和日常器物，到城市、生产和区域环境，先观察对象，再查阅关系与条件。</p><div class="note">编号对应图下说明，核心解释在小屏也可阅读。建筑、器物和祖先轮廓为形制或功能示例；地域图不是地图，未给出的解剖和工程细节仍待补充。</div>'
groups=[('生命与羽翼',['anatomy','plumage','molting','life','reproduction','wing-care','evolution']),('城市与通行',['city','city-section','platform','waiting','vertical','dual-entry','airspace','wind','commute','landing-chain','transport','navigation','flight','privacy']),('生活与生产',['housing','objects','clothing','agriculture','industry','logistics','food','energy','resilience','rescue','medicine','education','sports','travel','daily']),('地域与生态',['regions','region-wind','region-tide','region-canopy','region-basin','region-cliff','region-frost','boundaries','ecology','pollution']),('历史与文化',['history','events','governance','culture','etiquette','festivals','memorial'])]
titles={name[2:-5]:re.search(r'<h1 class="article-title">(.*?)</h1>',(ROOT/name).read_text()).group(1) for name in ENTRIES}
body+='<nav class="atlas-jump" aria-label="图鉴分类">'+''.join(f'<a class="chip" href="#atlas-group-{i}">{escape(name)}</a>' for i,(name,keys) in enumerate(groups))+'</nav>'
used=[]
for i,(name,keys) in enumerate(groups):
    body+=f'<section class="index-block" id="atlas-group-{i}"><h2>{name}</h2><div class="diagram-index">'
    for key in keys:
        related=[id for id,values in PLACEMENTS.items() if any(k==key for k,num in values)]
        body+='<section class="atlas-plate">'+figure(key)+'<div class="atlas-links">'+''.join(f'<a href="e-{id}.html">{escape(titles[id])} →</a>' for id in related)+'</div></section>'
        used.append(key)
    body+='</div></section>'
assert len(used)==len(set(used))==53
atlas.write_text(s[:start]+body+s[end:])

sources=ROOT/'sources.html';s=sources.read_text();s=s.replace('和16幅图解','和53幅图鉴与图解').replace('16幅图解','53幅图鉴与图解');sources.write_text(s)
print(json.dumps({'artworks':len(ART),'illustrated_entries':sum(bool(v) for v in PLACEMENTS.values()),'placements':sum(len(v) for v in PLACEMENTS.values()),'updated_entry_pages':len(changed),'prose_unchanged':True},ensure_ascii=False))
