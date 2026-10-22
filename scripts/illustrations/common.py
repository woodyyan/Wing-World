"""飞羽世界百科插图共用线描。几何是图解示例，不增加正典。"""
from html import escape
import math

INK='#1F1E1B'
MUTED='#5C5A55'
PAPER='#F8F5F0'
WHITE='#FFFFFF'
GREEN='#87A878'
TERRA='#D89575'
GOLD='#D4A574'
LINE='#C8D4BD'
BLUE='#7599A8'
PALE='#E9EFE2'
SAND='#EEE1CD'


def text(x,y,s,size=21,fill=INK,anchor='start',weight=400):
    lines=str(s).split('\n')
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">'+''.join(f'<tspan x="{x}" dy="{0 if i==0 else size*1.4}">{escape(line)}</tspan>' for i,line in enumerate(lines))+'</text>'


def path(d,fill='none',stroke=INK,width=2.2,dash=None,opacity=1):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" opacity="{opacity}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'


def rect(x,y,w,h,fill=WHITE,stroke=INK,r=0,width=2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'


def ellipse(x,y,rx,ry,fill=PALE,stroke='none',width=2):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'


def group(x,y,body,scale=1,rotate=0):
    return f'<g transform="translate({x} {y}) rotate({rotate}) scale({scale})">{body}</g>'


def line(x1,y1,x2,y2,color=INK,width=2,dash=None):
    return path(f'M{x1} {y1} L{x2} {y2}',stroke=color,width=width,dash=dash)


def arrow(points,color=BLUE,width=3,dash=None):
    if len(points)<2:return ''
    s=path('M'+' L'.join(f'{x} {y}' for x,y in points),stroke=color,width=width,dash=dash)
    a,b=points[-2],points[-1]
    angle=math.atan2(b[1]-a[1],b[0]-a[0]);n=10
    p1=(b[0]-n*math.cos(angle-.5),b[1]-n*math.sin(angle-.5));p2=(b[0]-n*math.cos(angle+.5),b[1]-n*math.sin(angle+.5))
    return s+path(f'M{p1[0]} {p1[1]} L{b[0]} {b[1]} L{p2[0]} {p2[1]}',stroke=color,width=width)


def curve_arrow(d,end,angle=0,color=BLUE,width=3,dash=None):
    x,y=end;n=10
    return path(d,stroke=color,width=width,dash=dash)+path(f'M{x-n*math.cos(angle-.5)} {y-n*math.sin(angle-.5)} L{x} {y} L{x-n*math.cos(angle+.5)} {y-n*math.sin(angle+.5)}',stroke=color,width=width)


def pin(n,x,y,tx=None,ty=None):
    s=''
    if tx is not None:s+=path(f'M{x} {y} Q{(x+tx)/2} {y} {tx} {ty}',stroke=MUTED,width=1.5)+ellipse(tx,ty,3,3,INK)
    return s+ellipse(x,y,16,16,WHITE,INK,1.6)+text(x,y+6,n,18,INK,'middle',600)


def ground(x,y,w):
    return path(f'M{x} {y} Q{x+w*.3} {y-3} {x+w*.6} {y+1} T{x+w} {y}',stroke=LINE,width=2)+path(f'M{x+15} {y+8} L{x+35} {y+8} M{x+w-65} {y+8} L{x+w-28} {y+8}',stroke=LINE,width=1)


def feather(x,y,h=120,color=SAND,angle=0,broken=False):
    b=path('M0 105 Q-35 85 -30 50 Q-23 14 0 -12 Q32 15 34 46 Q38 82 0 105Z',color,INK,1.7)
    b+=path('M0 -7 Q8 50 0 126',stroke=INK,width=1.8)
    for i in range(8):
        yy=8+i*12;r=14+14*math.sin(i/8*math.pi)
        b+=path(f'M3 {yy+10} Q{-r/2} {yy+3} {-r} {yy-6}',stroke=MUTED,width=.8)
        b+=path(f'M3 {yy+10} Q{r/2} {yy+2} {r} {yy-7}',stroke=MUTED,width=.8)
    if broken:b+=path('M-10 67 L7 59 L-6 80 L14 71',WHITE,TERRA,3)
    return group(x,y,b,h/138,angle)


def wing(opened=True,color=SAND,side=1):
    if opened:
        b=path('M9 -75 Q33 -108 73 -126 Q98 -139 119 -133 Q91 -100 87 -82 Q64 -52 20 -42Z',color,INK,2)
        for i in range(9):
            tx=116-i*7;ty=-131+i*5;bx=85-i*7;by=-79+i*4
            b+=path(f'M{tx} {ty} Q{tx+1} {ty+20} {bx} {by}',stroke=MUTED,width=1)
        b+=path('M13 -73 Q42 -87 69 -99',stroke=INK,width=1.4)
        for i in range(5):b+=path(f'M{25+i*8} {-80-i*4} q8 -10 16 -8',stroke=MUTED,width=.8)
    else:
        b=path('M11 -80 Q34 -84 42 -62 Q49 -21 26 2 Q15 -15 9 -48Z',color,INK,1.8)
        for i in range(5):b+=path(f'M{20+i*4} {-65+i*2} Q{43+i} {-20+i*2} {26+i} {-2+i*2}',stroke=MUTED,width=.85)
    return f'<g transform="scale({side} 1)">{b}</g>'


def human(x,y,h=130,pose='stand',shirt=GREEN,opened=False,back=False,child=False):
    """站姿、步行、坐姿和飞行均包含独立双手、双翼与双腿。坐标y为地面/脚。"""
    b=wing(opened,SAND,-1)+wing(opened,SAND,1)
    b+=ellipse(0,-100,13,16,'#E9C6A4',INK,1.8)
    b+=path('M-13 -104 Q-7 -124 10 -111 L13 -102 Q2 -107 -11 -100Z',MUTED,INK,1)
    if not back:b+=ellipse(5,-101,1.6,1.8,INK)+path('M5 -95 q4 2 6 -1',stroke=INK,width=.8)
    b+=path('M-12 -80 Q-4 -85 12 -80 L18 -41 Q0 -32 -18 -41Z',shirt,INK,2)
    b+=path('M-8 -79 Q0 -73 8 -79',stroke=WHITE,width=1.5)
    if pose in ['sit','care']:
        b+=path('M-11 -42 L-12 -21 L19 -21 L22 1 M11 -42 L17 -29 L34 -29 L34 1',stroke=INK,width=7)
        b+=path('M-12 -72 Q-26 -53 -14 -39 L7 -36 M13 -72 Q30 -59 30 -47 L15 -35',stroke='#E9C6A4',width=6)
        b+=path('M19 2 h15 M32 2 h14',stroke=INK,width=4)
    elif pose in ['walk','run']:
        b+=path('M-9 -42 L-18 -21 L-32 0 M10 -42 L25 -28 L38 -10',stroke=INK,width=7)
        b+=path('M-12 -72 L-28 -57 L-37 -73 M13 -72 L26 -53 L42 -51',stroke='#E9C6A4',width=6)
        b+=path('M-32 1 h13 M36 -9 l13 3',stroke=INK,width=4)
    elif pose in ['fly','glide','land']:
        b+=path('M-9 -42 Q-20 -23 -13 -7 M10 -42 L23 -23 L34 -17',stroke=INK,width=7)
        b+=path('M-12 -73 L-30 -67 L-44 -58 M13 -73 L32 -63 L44 -68',stroke='#E9C6A4',width=6)
        b+=path('M-14 -6 h14 M33 -16 l13 3',stroke=INK,width=4)
    else:
        b+=path('M-9 -42 L-10 -20 L-11 0 M10 -42 L12 -20 L13 0',stroke=INK,width=7)
        b+=path('M-13 -74 Q-26 -57 -24 -37 M13 -74 Q29 -56 26 -38',stroke='#E9C6A4',width=6)
        b+=path('M-11 1 h-12 M12 1 h14',stroke=INK,width=4)
    return group(x,y,b,h/118)


def chair(x,y,s=1):
    b=path('M-24 -35 L30 -35 L30 -30 L-24 -30Z',TERRA,INK,1.5)+path('M-22 -32 L-24 0 M26 -32 L28 0 M-22 -35 L-27 -75 L-10 -77 L-9 -56 M20 -56 L20 -77 L31 -75 L31 -35',stroke=INK,width=3)
    return group(x,y,b,s)


def bus(x,y,w=150):
    b=path('M0 -53 Q0 -64 12 -64 H123 Q140 -60 146 -43 V-10 H0Z',GREEN,INK,2)
    b+=rect(7,-57,99,27,PALE,INK,4,1.3)+rect(112,-49,21,35,PALE,INK,2,1.3)
    for xx in [32,58,84]:b+=line(xx,-56,xx,-30,INK,1)
    b+=line(3,-20,107,-20,MUTED,1)
    for xx in [27,119]:b+=ellipse(xx,-7,10,10,INK)+ellipse(xx,-7,4,4,WHITE)
    return group(x,y,b,w/146)


def truck(x,y,w=160):
    b=rect(0,-75,98,64,SAND,INK,2)+path('M98 -58 H126 L148 -36 V-10 H98Z',TERRA,INK,2)
    b+=path('M108 -52 H123 L139 -35 H108Z',PALE,INK,1)
    b+=line(108,-28,120,-28,INK,1)
    for xx in [24,82,127]:b+=ellipse(xx,-8,10,10,INK)+ellipse(xx,-8,4,4,WHITE)
    return group(x,y,b,w/148)


def crate(x,y,w=60,h=45):
    b=rect(x,y,w,h,SAND,INK,1,1.5)
    b+=line(x+6,y+4,x+6,y+h-4,MUTED,1)+line(x+w-6,y+4,x+w-6,y+h-4,MUTED,1)
    b+=path(f'M{x} {y+h*.4} H{x+w} M{x} {y+h*.75} H{x+w}',stroke=MUTED,width=1)
    return b


def parcel(x,y,w=35):
    return path(f'M{x} {y} l{w*.6} {-w*.25} l{w*.4} {w*.25} v{w*.6} l{-w*.6} {w*.2} l{-w*.4} {-w*.2}Z',GOLD,INK,1.5)+path(f'M{x} {y} l{w*.4} {w*.2} l{w*.6} {-w*.2} M{x+w*.4} {y+w*.2} v{w*.6}',stroke=INK,width=1)


def tree(x,y,h=180):
    b=path('M-4 0 L-7 -85 M4 0 L6 -90',stroke=MUTED,width=5)+path('M0 -55 L-32 -95 M0 -70 L25 -114',stroke=MUTED,width=3)
    b+=path('M-66 -101 Q-82 -123 -57 -140 Q-66 -166 -31 -169 Q-10 -195 12 -174 Q43 -187 54 -159 Q88 -149 70 -120 Q66 -89 32 -96 Q7 -75 -18 -91 Q-49 -76 -66 -101Z',PALE,GREEN,2)
    b+=path('M-41 -129 q21 -16 34 -1 M10 -153 q19 -12 33 1 M18 -108 q18 -14 30 -6',stroke=GREEN,width=1.2)
    return group(x,y,b,h/190)


def plant(x,y,h=45):
    return path(f'M{x} {y} Q{x-3} {y-h*.6} {x} {y-h}',stroke=GREEN,width=2)+path(f'M{x} {y-h*.5} Q{x-25} {y-h*.85} {x-25} {y-h*.5} Q{x-14} {y-h*.3} {x} {y-h*.5} M{x} {y-h*.65} Q{x+24} {y-h*.9} {x+22} {y-h*.55} Q{x+12} {y-h*.45} {x} {y-h*.65}',PALE,GREEN,1.3)


def cloud(x,y,w=100):
    return group(x,y,path('M-50 8 Q-64 -12 -39 -22 Q-31 -47 -6 -32 Q19 -50 31 -22 Q59 -18 52 7 Q24 18 -50 8Z',WHITE,LINE,1.5),w/110)


def house(x,y,w=160,h=200):
    b=rect(x,y-h,w,h,SAND,INK,2)
    b+=path(f'M{x-10} {y-h} L{x+w*.5} {y-h-35} L{x+w+10} {y-h}Z',GREEN,INK,2)
    b+=rect(x+w*.38,y-63,w*.22,63,TERRA,INK,1)
    for yy in [y-h+25,y-h+80]:
        for xx in [x+18,x+w-52]:b+=rect(xx,yy,32,37,PALE,INK,1)+line(xx+16,yy,xx+16,yy+37,LINE,1)
    return b


def cup(x,y,s=1):
    return group(x,y,path('M-17 -31 H17 L13 -2 Q0 4 -13 -2Z',WHITE,INK,1.5)+path('M17 -26 Q35 -28 26 -12 L16 -10',stroke=INK,width=1.5),s)


def book(x,y,w=70):
    return group(x,y,path('M-36 -32 Q-16 -42 0 -30 Q15 -40 36 -32 V8 Q16 1 0 12 Q-20 2 -36 8Z',WHITE,INK,1.5)+path('M0 -30 V12 M-29 -21 q14 -4 23 0 M8 -21 q12 -4 22 0 M-29 -10 q14 -3 23 0 M8 -10 q12 -3 22 0',stroke=MUTED,width=1),w/72)


def desk(x,y,w=130):
    return rect(x,y-50,w,7,SAND,INK,1)+path(f'M{x+8} {y-43} L{x+4} {y} M{x+w-8} {y-43} L{x+w-4} {y}',stroke=INK,width=3)


def sailboat(x,y,w=130):
    b=path('M-62 0 H66 L46 29 H-42Z',SAND,INK,1.8)+line(0,-108,0,0,INK,2)+path('M-4 -101 L-4 -7 L-50 -7Z',WHITE,INK,1.5)+path('M4 -90 L50 -9 H4Z',PALE,INK,1.5)
    b+=path('M-82 37 q17 -8 34 0 t34 0 t34 0 t34 0',stroke=BLUE,width=1.5)
    return group(x,y,b,w/130)


def notebook(x,y,w=75):
    return rect(x,y,w,w*1.25,PALE,INK,3)+path(f'M{x+12} {y} v{w*1.25}',stroke=INK,width=1.5)+path(f'M{x+25} {y+25} h{w-37} M{x+25} {y+45} h{w-37} M{x+25} {y+65} h{w-45}',stroke=LINE,width=2)


def make(key,title,body,caption,notes,question='',height=600):
    """SVG内只保留小编号，完整文字在HTML响应式图例中，避免小屏缩字。"""
    desc=title+'。'+caption+' '+' '.join(f'{i+1} {n[0]}：{n[1]}' for i,n in enumerate(notes))
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 {height}" role="img" aria-labelledby="art-{key}-title art-{key}-desc" class="encyclopedia-art"><title id="art-{key}-title">{escape(title)}</title><desc id="art-{key}-desc">{escape(desc)}</desc><rect width="900" height="{height}" fill="{PAPER}"/><g font-family="system-ui, PingFang SC, sans-serif">{body}</g></svg>'
    return {'title':title,'svg':svg,'caption':caption,'notes':notes,'question':question,'height':height}
