"""城市空间的淡彩剖切与生活速写；所有形制均为示例，不增加工程参数。"""
from common import *


SKIN = '#E9C6A4'
GLASS = '#E3ECE9'
CUT = '#DDC9B0'
GROUND_ROUTE = TERRA
AIR_ROUTE = BLUE


def _limb(name, body):
    return f'<g data-limb="{name}">{body}</g>'


def _person(x, y, h=100, pose='stand', shirt=GREEN, opened=False, elder=False):
    """脚下为稳定地面；翼、手臂和腿分别绘制，手持物不替代肢体。"""
    b = _limb('left-wing', wing(opened, SAND, -1))
    b += _limb('right-wing', wing(opened, SAND, 1))
    b += ellipse(0, -100, 13, 16, SKIN, INK, 1.8)
    b += path('M-13 -105 Q-7 -120 9 -111 L13 -103 Q1 -108 -11 -101Z', '#A7A39A' if elder else MUTED, INK, 1)
    b += ellipse(5, -102, 1.5, 1.7, INK)
    b += path('M6 -95 q4 2 6 -1 M-5 -84 L5 -84', stroke=INK, width=1)
    b += path('M-12 -80 Q0 -86 12 -80 L18 -42 Q1 -35 -18 -42Z', shirt, INK, 1.8)
    b += path('M-8 -78 Q0 -73 8 -78 M-15 -47 Q0 -42 15 -47', stroke=WHITE, width=1.1)
    if pose in ('sit', 'sit-drink'):
        legs = ('M-10 -42 L-12 -23 L17 -23 L20 0', 'M10 -42 L15 -31 L32 -31 L34 0')
        arms = ('M-12 -73 Q-27 -54 -13 -40 L4 -36', 'M13 -73 L33 -54 L25 -89' if pose == 'sit-drink' else 'M13 -73 Q28 -57 26 -44 L14 -36')
        feet = 'M18 1 h13 M33 1 h12'
    elif pose in ('walk', 'run'):
        legs = ('M-9 -42 L-18 -23 L-32 0', 'M10 -42 L25 -27 L38 -10')
        arms = ('M-12 -73 L-28 -57 L-37 -72', 'M13 -73 L26 -54 L41 -52')
        feet = 'M-33 1 h13 M36 -9 l12 3'
    elif pose == 'land':
        legs = ('M-9 -42 L-27 -23 L-23 0', 'M10 -42 L31 -31 L28 -11')
        arms = ('M-12 -73 L-31 -62 L-46 -55', 'M13 -73 L32 -62 L48 -67')
        feet = 'M-25 1 h17 M27 -10 l14 3'
    elif pose == 'drink':
        legs = ('M-9 -42 L-11 0', 'M10 -42 L13 0')
        arms = ('M-13 -73 Q-27 -57 -23 -36', 'M13 -73 L33 -54 L25 -89')
        feet = 'M-11 1 h-12 M12 1 h14'
    elif pose == 'prepare':
        legs = ('M-9 -42 L-11 0', 'M10 -42 L13 0')
        arms = ('M-12 -73 L-32 -61 L-29 -40', 'M13 -73 L24 -55 L-18 -51')
        feet = 'M-11 1 h-12 M12 1 h14'
    elif pose == 'phone':
        legs = ('M-9 -42 L-11 0', 'M10 -42 L13 0')
        arms = ('M-13 -73 Q-26 -50 3 -48 L45 -61', 'M13 -73 L26 -54 L36 -45')
        feet = 'M-11 1 h-12 M12 1 h14'
    else:
        legs = ('M-9 -42 L-11 -20 L-11 0', 'M10 -42 L12 -20 L13 0')
        arms = ('M-13 -73 Q-26 -57 -24 -37', 'M13 -73 Q29 -56 26 -38')
        feet = 'M-11 1 h-12 M12 1 h14'
    for name, d in zip(('left-leg', 'right-leg'), legs):
        b += _limb(name, path(d, stroke=INK, width=6.5))
    b += path(feet, stroke=INK, width=3.7)
    if pose == 'phone':
        b += _phone(34, -96, .65)
    for name, d in zip(('left-arm', 'right-arm'), arms):
        b += _limb(name, path(d, stroke=SKIN, width=6))
    if pose in ('drink', 'sit-drink'):
        b += cup(27, -86, .33)
    if elder:
        b += path('M28 -38 Q39 -42 39 -32 V0', stroke=MUTED, width=2.2)
    return group(x, y, b, h / 118)


def _flyer(x, y, scale=.65, angle=0, facing=1):
    """横向前进的一瞬，不是悬停；两翼在背后，两手独立伸向前方。"""
    b = ''
    wings = (
        ('left-wing', 'M-8 -9 Q-48 -82 -101 -71 Q-81 -43 -70 -20 Q-40 4 -13 9Z', -1),
        ('right-wing', 'M-13 -14 Q8 -67 62 -86 Q60 -48 45 -24 Q24 -9 -5 4Z', 1),
    )
    for name, outline, side in wings:
        w = path(outline, SAND, INK, 1.8)
        for i in range(7):
            if side < 0:
                w += path(f'M{-96+i*8} {-70+i*3} Q{-80+i*8} {-37+i*3} {-66+i*7} {-20+i*3}', stroke=MUTED, width=.85)
            else:
                w += path(f'M{59-i*7} {-81+i*3} Q{51-i*6} {-44+i*3} {41-i*6} {-24+i*3}', stroke=MUTED, width=.85)
        b += _limb(name, w)
    b += path('M-19 -8 Q-1 -19 24 -11 L28 9 Q0 22 -23 12Z', GREEN, INK, 1.8)
    b += path('M-15 -4 Q4 -10 21 -5', stroke=WHITE, width=1.2)
    b += ellipse(36, -15, 14, 13, SKIN, INK, 1.7)
    b += path('M23 -19 Q29 -36 47 -24 L50 -15 Q37 -23 26 -14Z', MUTED, INK, 1)
    b += ellipse(43, -15, 1.6, 1.6, INK)
    b += path('M45 -8 l5 -1', stroke=INK, width=1)
    b += _limb('left-leg', path('M-18 9 L-42 22 L-67 15', stroke=INK, width=6.5))
    b += _limb('right-leg', path('M-10 16 L-21 37 L-47 43', stroke=INK, width=6.5))
    b += path('M-69 15 l-9 7 M-49 43 l-8 8', stroke=INK, width=3.5)
    b += _limb('left-arm', path('M12 -10 L39 -2 L62 -12', stroke=SKIN, width=6))
    b += _limb('right-arm', path('M9 8 L34 18 L58 12', stroke=SKIN, width=6))
    b += path('M62 -12 l7 -2 M58 12 l7 2', stroke=INK, width=1.2)
    return group(x, y, f'<g transform="scale({facing} 1)">{b}</g>', scale, angle)


def _seat(x, y, scale=1):
    # 座面与坐姿膝部同高；两侧背条之间留翼位，不画整块压翼的靠背。
    b = path('M-23 -24 H34 L36 -20 H-23Z', TERRA, INK, 1.5)
    b += path('M-21 -20 L-24 0 M31 -20 L35 0 M-24 -24 L-29 -73 L-21 -75 L-16 -33 M33 -24 L37 -73 L45 -72 L44 -24', stroke=INK, width=2.5)
    b += path('M-22 -9 H32', stroke=MUTED, width=1)
    return group(x, y, b, scale)


def _table(x, floor, w=130):
    b = path(f'M{x} {floor-50} H{x+w} V{floor-43} H{x}Z', SAND, INK, 1.5)
    b += path(f'M{x+8} {floor-43} L{x+4} {floor} M{x+w-8} {floor-43} L{x+w-4} {floor}', stroke=INK, width=2.5)
    return b


def _window(x, y, w=42, h=52, curtain=False):
    b = rect(x, y, w, h, GLASS, MUTED, 1, 1.4)
    b += rect(x-3, y+h, w+6, 4, CUT, INK, 0, 1)
    b += path(f'M{x+w*.5} {y} V{y+h} M{x} {y+h*.57} H{x+w}', stroke=LINE, width=1)
    b += path(f'M{x+7} {y+10} l{w*.18} {-4} M{x+w*.65} {y+h*.8} l{w*.15} {-5}', stroke=WHITE, width=2)
    if curtain:
        b += path(f'M{x+3} {y+3} h{w*.23} Q{x+w*.12} {y+h*.6} {x+3} {y+h-3}Z M{x+w-3} {y+3} h{-w*.23} Q{x+w*.88} {y+h*.6} {x+w-3} {y+h-3}Z', SAND, MUTED, 1)
    return b


def _stairs(x, y, width=85, rise=95, steps=7, facing=1):
    tread = width / steps
    r = rise / steps
    d = f'M{x} {y}'
    for _ in range(steps):
        d += f' h{facing*tread} v{-r}'
    d += f' v{r+7} L{x} {y+8}Z'
    b = path(d, CUT, INK, 1.7)
    b += path(f'M{x} {y-24} L{x+facing*width} {y-rise-24}', stroke=MUTED, width=2)
    for i in (0, 2, 4, 7):
        xx = x + facing*tread*i
        yy = y-r*i
        b += line(xx, yy-24, xx, yy-3, MUTED, 1)
    return b


def _lift(x, roof, base, width=82, car_bottom=None, car_h=82, people=True, freight=False, floors=()):
    """剖开的井壁、导轨、悬索、轿厢底板与开口，屋顶有实在门槛。"""
    bottom = base if car_bottom is None else car_bottom
    top = roof-max(64, car_h+24)
    b = rect(x, top, 7, base-top+6, CUT, INK, 0, 1.6)
    b += rect(x+width-7, top, 7, base-top+6, CUT, INK, 0, 1.6)
    b += rect(x, top, width, 9, CUT, INK, 0, 1.6)
    b += path(f'M{x+12} {top+19} V{base-4} M{x+width-12} {top+19} V{base-4}', stroke=MUTED, width=1.2)
    b += ellipse(x+width*.5, top+16, 7, 7, WHITE, INK, 1.2)
    b += path(f'M{x+width*.5-4} {top+23} V{bottom-car_h} M{x+width*.5+4} {top+23} V{bottom-car_h}', stroke=MUTED, width=1)
    for yy in (roof,) + tuple(floors):
        b += path(f'M{x-14} {yy} H{x+9} M{x+width-9} {yy} H{x+width+14}', stroke=INK, width=4)
        b += path(f'M{x-13} {yy-53} V{yy-5} M{x+width+12} {yy-53} V{yy-5}', stroke=LINE, width=1.8)
    b += path(f'M{x+16} {bottom-car_h} H{x+width-16} V{bottom-5} H{x+16}Z', GLASS, INK, 1.8)
    b += rect(x+15, bottom-5, width-30, 8, CUT, INK, 0, 1.2)
    b += path(f'M{x+21} {bottom-car_h+7} H{x+width-21} M{x+width-23} {bottom-car_h+22} v15', stroke=MUTED, width=1)
    if freight:
        b += _box(x+22, bottom-31, 31, 26)
        b += _box(x+width-47, bottom-56, 26, 51)
    elif people:
        b += _person(x+width*.5, bottom-7, min(62, car_h-14, (width-34)*118/96))
    return b


def _building(x, base, w, levels=3, step=100, car_level=1, windows=True):
    roof = base-levels*step
    sx = x+w-83
    b = path(f'M{x} {roof} L{x+25} {roof-19} H{x+w+24} V{base-17} L{x+w} {base} H{x}Z', SAND, INK, 1.8)
    b += path(f'M{x+w} {roof} l24 -19 V{base-17} l-24 17Z', CUT, INK, 1.4)
    b += rect(x, roof, 9, base-roof+10, CUT, INK, 0, 1.6)
    for i in range(levels+1):
        yy = base-i*step
        b += rect(x, yy, w-83, 8, CUT, INK, 0, 1.5)
        if i < levels and windows:
            for xx in (x+23, x+83):
                if xx+43 < sx-5:
                    b += _window(xx, yy-step+20, 40, min(47, step-35), i > 0)
    b += _lift(sx, roof, base, 83, base-car_level*step, min(85, step-12), floors=tuple(base-i*step for i in range(levels)))
    b += path(f'M{x-7} {base+9} H{x+w+9} V{base+26} H{x-7}Z', CUT, INK, 1.5)
    for xx in (x+8, x+w-42):
        b += path(f'M{xx} {base+13} l-7 9 M{xx+14} {base+13} l-7 9', stroke=MUTED, width=.8)
    return b


def _shelter(x, floor, w=160, h=105):
    b = path(f'M{x} {floor-h} L{x+17} {floor-h-12} H{x+w+12} L{x+w} {floor-h}Z', GREEN, INK, 1.6)
    b += rect(x, floor-h, 6, h, CUT, INK, 0, 1.5)
    b += rect(x+w-6, floor-h, 6, h, CUT, INK, 0, 1.5)
    b += rect(x+6, floor-h+5, w-12, h-6, GLASS, LINE, 0, 1)
    b += path(f'M{x+8} {floor-2} H{x+w-8} M{x+w-40} {floor-h+7} V{floor-3}', stroke=MUTED, width=1.3)
    return b


def _water(x, floor, scale=1):
    b = path('M-17 -52 H15 V-6 H-17Z', GLASS, INK, 1.5)
    b += path('M-20 -52 Q-20 -67 -9 -68 H11 Q19 -63 18 -52Z', WHITE, INK, 1.3)
    b += path('M-19 -30 H17 L11 -23 H-12Z M-8 -47 h7 v6 M-10 -9 h17', stroke=INK, width=1.3)
    b += cup(8, -25, .22)
    return group(x, floor, b, scale)


def _windsock(x, floor, scale=1, side=1):
    b = path('M0 0 V-94 M-8 0 H8 M0 -84 L12 -89', stroke=MUTED, width=2)
    b += path('M12 -100 Q30 -99 59 -84 L62 -78 Q33 -86 12 -81Z', TERRA, INK, 1.4)
    for xx in (23, 35, 47):
        b += path(f'M{xx} {-98+(xx-12)*.28} l-2 15', stroke=WHITE, width=2.8)
    b += ellipse(12, -91, 3, 10, WHITE, INK, 1)
    return group(x, floor, f'<g transform="scale({side} 1)">{b}</g>', scale)


def _box(x, y, w=42, h=35):
    b = path(f'M{x} {y} H{x+w} V{y+h} H{x}Z', SAND, INK, 1.5)
    b += path(f'M{x+w*.43} {y} v{h} M{x+4} {y+6} h{w-8} M{x+4} {y+h-6} h{w-8}', stroke=MUTED, width=1)
    return b


def _case(x, floor, w=34, h=48):
    b = path(f'M{x} {floor-h} Q{x-3} {floor-h} {x-3} {floor-h+7} V{floor-7} Q{x-3} {floor-3} {x+3} {floor-3} H{x+w-3} Q{x+w+3} {floor-3} {x+w+3} {floor-9} V{floor-h+7} Q{x+w+3} {floor-h} {x+w-3} {floor-h}Z', TERRA, INK, 1.5)
    b += path(f'M{x+8} {floor-h} v-13 h{w-16} v13 M{x+8} {floor-h+7} V{floor-10} M{x+w-8} {floor-h+7} V{floor-10}', stroke=MUTED, width=1)
    b += ellipse(x+4, floor-1, 3, 3, INK)+ellipse(x+w-4, floor-1, 3, 3, INK)
    return b


def _coach(x, floor, width=190, cut=False, train=False):
    b = path('M0 -18 V-93 Q1 -109 18 -111 H221 Q246 -108 251 -88 V-18Z', PALE if train else GREEN, INK, 2)
    b += path('M9 -101 H210 V-57 H9Z M220 -96 L239 -83 V-25 H220Z', GLASS, INK, 1.3)
    for xx in (52, 96, 140, 184):
        b += path(f'M{xx} -101 V-58', stroke=MUTED, width=1)
    b += path('M2 -34 H215 M226 -51 h8 M0 -17 H252', stroke=MUTED, width=1.4)
    for xx in (37, 207):
        b += ellipse(xx, -12, 15, 15, INK)+ellipse(xx, -12, 6, 6, WHITE)
    if cut:
        b += path('M14 -50 H209 V-20 H14Z', PAPER, LINE, 1)
        for xx, color in ((65, TERRA), (139, BLUE)):
            b += _seat(xx, -23, .62)
            b += _person(xx, -23, 72, 'sit', color)
        b += path('M8 -109 H213 M13 -19 H214', stroke=CUT, width=4)
    return group(x, floor, b, width/251)


def _phone(x, y, scale=1, status=False):
    b = path('M0 0 Q0 -3 4 -3 H38 Q42 -3 42 1 V65 Q42 69 38 69 H4 Q0 69 0 65Z', MUTED, INK, 1)
    b += path('M3 5 H39 V60 H3Z', WHITE, LINE, .7)
    b += path('M15 1 H27 M15 64 H27', stroke=LINE, width=1)
    if status:
        b += text(6, 16, '天气', 6.3, MUTED)
        b += path('M27 11 q5 -5 10 1 M27 16 q5 -5 9 0', stroke=BLUE, width=.9)
        b += text(6, 33, '开放', 6.3, MUTED)
        b += path('M29 29 l3 3 l5 -7', stroke=GREEN, width=1.5)
        b += text(6, 50, '拥挤', 6.3, MUTED)
        b += path('M29 47 h6 M29 51 h9', stroke=TERRA, width=1.3)
        b += path('M6 21 H35 M6 38 H35', stroke=LINE, width=.5)
    else:
        b += path('M7 14 q10 -4 23 0 M7 29 h24 M7 41 h17', stroke=BLUE, width=1.5)
    return group(x, y, b, scale)


def _notice(x, y, w=76, h=64):
    b = path(f'M{x} {y} H{x+w} V{y+h} H{x}Z', SAND, MUTED, 1.5)
    b += path(f'M{x+w*.09} {y+h*.1} H{x+w*.91} V{y+h*.9} H{x+w*.09}Z', WHITE, LINE, 1)
    b += path(f'M{x+w*.2} {y+h*.32} q{w*.1} {-h*.1} {w*.22} 0 M{x+w*.2} {y+h*.43} q{w*.1} {-h*.1} {w*.22} 0 M{x+w*.2} {y+h*.64} h{w*.6} M{x+w*.2} {y+h*.77} h{w*.46}', stroke=BLUE, width=1.4)
    b += ellipse(x+w*.75, y+h*.35, min(w, h)*.06, min(w, h)*.06, GREEN)
    return b


def _scene(key, title, body, notes, question, height=740, caption=None):
    return make(key, title, body, caption or '淡彩剖切与动作速写；设施形制和位置为示例，不按比例，不规定统一布局或工程参数。', notes, question, height)


def _city():
    b = cloud(178, 103, 115)+cloud(720, 70, 94)
    b += path('M35 612 Q235 608 440 615 T864 612 L864 704 Q430 695 35 704Z', '#F0E8DA', LINE, 1.2)
    b += _building(91, 609, 350, 3, 108, 1)
    b += _building(536, 609, 282, 4, 89, 2)
    b += _stairs(108, 501, 74, 108)
    b += _person(229, 501, 70, 'sit')+_seat(229, 501, 70/118)
    b += _table(567, 431, 84)+book(591, 386, 22)
    b += _person(670, 431, 66, 'stand', BLUE)
    b += _shelter(105, 285, 105, 83)
    b += _seat(148, 285, .48)+_person(148, 285, 56, 'sit', BLUE)
    b += _water(224, 285, .52)+_windsock(94, 285, .57, -1)
    b += _person(281, 285, 61, 'run', GREEN, True)
    b += _shelter(551, 253, 73, 81)
    b += _person(589, 253, 55, 'drink', TERRA)+_water(636, 253, .5)
    b += _person(679, 253, 53, 'land', GREEN, True)
    b += _coach(302, 685, 179, True)
    b += _box(670, 650, 45, 33)+_box(720, 653, 38, 30)
    b += path('M658 685 H771 V644 H750 M671 685 l-5 7 M757 685 l8 7', stroke=MUTED, width=2)
    b += _person(602, 660, 63, 'walk', GREEN)
    b += _person(104, 654, 64, 'walk', TERRA, elder=True)
    b += _person(173, 651, 69, 'walk', BLUE)+_person(216, 651, 44, 'walk', GREEN)
    b += tree(843, 617, 115)+plant(67, 611, 34)
    b += curve_arrow('M221 670 Q270 644 312 656 Q497 705 558 649 Q626 622 726 607', (726, 607), -.1, GROUND_ROUTE, 3.2, '8 6')
    b += curve_arrow('M295 265 C366 115 487 108 563 170 Q614 198 680 238', (680, 238), .5, AIR_ROUTE, 3.2, '8 6')
    b += _flyer(438, 161, .62, -5)
    b += pin(1, 58, 665, 367, 679)+pin(2, 476, 473, 399, 501)
    b += pin(3, 60, 199, 143, 267)+pin(4, 842, 163, 679, 253)
    b += pin(5, 532, 95, 493, 145)+pin(6, 471, 576, 589, 601)
    return _scene('city', '同一城市里的地面网与空中网', b, [
        ('赭色地面线', '步行、公交和箱货沿街面接续，儿童与高龄居民同样参与日常生活。'),
        ('公共电梯', '剖开的井壁、导轨和载人轿厢把实际楼层与屋顶门槛连在一起。'),
        ('屋顶出发节点', '坐等、补水和助跑发生在同一座接地建筑的屋顶。'),
        ('到达与恢复', '成人在另一座楼的平台制动落地，再补水或进入楼内。'),
        ('蓝色空中线', '轻装飞行者沿弯曲路线连接两个公共节点，不在空中定点排队。'),
        ('共享建筑与服务', '街面入口、楼层生活和屋顶入口属于同一城市，不按通行方式分人群。'),
    ], '观察两条不同颜色的路径：它们在哪里借公共电梯接入同一座楼？')


def _city_section():
    b = cloud(665, 73, 120)
    b += _building(173, 678, 552, 4, 112, 2, False)
    for i, xx in enumerate((235, 342, 252, 396)):
        yy = 678-i*112
        b += _window(190, yy-88, 42, 59, i > 0)
        if i == 0:
            b += _person(xx, yy, 77, 'walk', TERRA)
            b += _person(340, yy, 48, 'walk', GREEN)
        elif i == 1:
            b += _seat(xx, yy, .63)+_person(xx, yy, 74, 'sit', BLUE)
            b += _table(411, yy, 100)+book(441, yy-45, 28)+cup(491, yy-45, .35)
        elif i == 2:
            b += _person(xx, yy, 76, 'prepare')+_water(415, yy, .72)
        else:
            b += _table(257, yy, 106)+book(283, yy-46, 30)
            b += _person(xx, yy, 76, 'stand', TERRA)
        if i < 3:
            b += _stairs(516, yy, 106, 112)
    b += _shelter(183, 230, 231, 111)
    b += _seat(245, 230, .61)+_person(245, 230, 72, 'sit', BLUE)
    b += _water(381, 230, .62)+_person(345, 230, 70, 'drink', GREEN)
    b += _person(504, 230, 76, 'run', TERRA, True)+_windsock(167, 230, .63, -1)
    b += _flyer(646, 102, .68, -12)
    b += curve_arrow('M545 207 Q629 35 799 116', (799, 116), .42, BLUE, 2.6, '7 6')
    b += ground(63, 704, 772)+_coach(445, 716, 138, True)
    b += _box(96, 685, 39, 27)+plant(799, 689, 43)
    b += pin(1, 72, 659, 277, 681)+pin(2, 77, 441, 363, 454)
    b += pin(3, 80, 180, 278, 230)+pin(4, 799, 57, 684, 100)
    b += pin(5, 808, 430, 683, 454)+pin(6, 799, 610, 586, 568)
    return _scene('city-section', '四层空间与四个实际楼层的生活剖面', b, [
        ('地面层', '街面运输和入口接到建筑基础，儿童随成人从地面参与。'),
        ('建筑层', '图中楼板分别承托走动、阅读、整羽与工作，生活活动在稳定空间中完成。'),
        ('屋顶层', '候风厅、补水与助跑的位置示例位于最上层楼板之上。'),
        ('通行空域', '屋顶外的成人正在前进，路线不等于统一固定航层。'),
        ('电梯到屋顶', '可见轿厢、竖井和各层门槛，机械连接一直到屋顶入口。'),
        ('楼梯与生活', '实体踏步连接相邻楼板，但楼梯不替代所有人的机械到达。'),
    ], '沿井壁向上观察：四块楼板和屋顶怎样与轿厢相接？', 770)


def _platform():
    b = path('M86 325 L571 182 L837 329 L346 510Z', SAND, INK, 2)
    b += path('M86 325 V561 L346 731 V510Z M346 510 V731 L837 550 V329Z', CUT, INK, 1.8)
    b += path('M110 351 V550 M155 382 V579 M379 537 V695 M748 389 V575', stroke=MUTED, width=2)
    b += path('M87 325 L346 510 L837 329 M86 334 L346 519 L837 338', stroke=INK, width=2)
    b += path('M196 294 L453 452 M309 259 L574 408 M419 227 L684 367', stroke=LINE, width=1)
    b += _shelter(125, 341, 207, 126)
    b += _seat(193, 341, .66)+_person(193, 341, 78, 'sit', BLUE)
    b += _person(277, 341, 73, 'prepare', GREEN)
    b += _notice(145, 234, 73, 47)
    b += _lift(436, 365, 648, 103, 365, 99, floors=(505, 640))
    b += _water(354, 374, .8)+_person(386, 375, 78, 'drink', TERRA)
    b += _windsock(590, 272, .7)
    b += _person(366, 455, 64, 'run', GREEN, True)
    b += _person(728, 346, 80, 'land', BLUE, True)
    b += curve_arrow('M394 434 Q476 402 569 354', (569, 354), -.4, GREEN, 2.5, '6 6')
    b += curve_arrow('M818 145 C845 219 819 290 769 347', (769, 347), 2.25, BLUE, 2.5, '7 6')
    b += _flyer(792, 190, .57, 22)
    b += path('M630 290 Q695 247 758 264 M625 297 Q698 253 760 271', stroke=LINE, width=1.2)
    b += _window(130, 441, 43, 65)+_window(206, 495, 43, 65)+_window(645, 487, 48, 64)
    b += pin(1, 61, 247, 193, 337)+pin(2, 393, 206, 486, 355)
    b += pin(3, 281, 426, 357, 360)+pin(4, 388, 544, 366, 445)
    b += pin(5, 849, 407, 728, 344)+pin(6, 685, 103, 733, 265)
    return _scene('platform', '屋顶平台上的真实位置示例', b, [
        ('候风与检查', '坐等和整羽留在遮蔽厅内，不占正在使用的起降空间。'),
        ('电梯厅', '屋顶门槛与可见轿厢相接，街面来访者同样能够抵达。'),
        ('补水与恢复', '饮水设施紧靠步行通道，落地后能停留而不必立刻再飞。'),
        ('助跑动作', '成人的脚仍在承重屋面上，手臂与展开的双翼各自独立。'),
        ('制动落地', '来向另一侧的成人已接触平台，等待者没有站在其进近位置。'),
        ('示例净空', '空出的屋面与上方空间说明进近需求，不给统一分区尺寸或永久方向。'),
    ], '寻找六个位置：哪些人在稳定地面，哪里留给进近与制动？', 790)


def _waiting():
    b = rect(75, 162, 575, 292, GLASS, LINE, 0, 1.6)
    b += path('M75 162 L102 141 H670 L650 162Z', GREEN, INK, 1.8)
    b += rect(75, 162, 8, 298, CUT, INK, 0, 1.6)
    b += path('M75 454 H650 L810 563 H236Z M236 563 V575 L810 575 V563', SAND, INK, 1.7)
    b += path('M87 460 L248 563 M206 455 L366 561 M373 455 L531 561 M540 455 L697 561', stroke=LINE, width=1)
    b += _window(107, 203, 132, 109)+_window(275, 203, 104, 109)
    b += _notice(420, 225, 112, 85)
    b += _seat(197, 483, .94)+_person(197, 483, 111, 'sit', GREEN)
    b += _seat(350, 490, .87)+_person(350, 490, 103, 'sit', TERRA, elder=True)
    b += _person(520, 457, 105, 'stand', BLUE)
    b += _water(587, 494, .92)+_person(642, 488, 101, 'drink', GREEN)
    b += _lift(719, 478, 694, 102, 478, 112, floors=(687,))
    b += path('M650 454 H710 M650 463 H710 M702 478 H735', stroke=INK, width=3)
    b += _stairs(237, 673, 127, 105)
    b += _stairs(85, 565, 125, 105)
    b += path('M93 454 V337 H140 V453 M115 384 v31 M108 406 l7 9 l7 -9', stroke=INK, width=1.6)
    b += _person(113, 453, 84, 'walk', TERRA)
    b += _coach(477, 700, 161, True)+ground(45, 706, 804)
    b += _windsock(677, 221, .75)+cloud(796, 132, 83)
    b += curve_arrow('M661 526 Q691 519 719 493', (719, 493), -.7, TERRA, 2.4, '7 5')
    b += pin(1, 142, 542, 196, 461)+pin(2, 378, 158, 468, 272)
    b += pin(3, 563, 548, 593, 467)+pin(4, 851, 455, 769, 478)
    b += pin(5, 41, 389, 123, 454)
    return _scene('waiting', '收翼坐等、查看公告与返回地面', b, [
        ('厅内坐等', '两位居民收翼坐在留翼位的椅子上，等待不是空中悬停。'),
        ('现场公告', '站在厅内查看公告与窗外风向，再结合个人状态决定是否出发。'),
        ('补水', '喝水的人保持稳定站位，手中杯子不替代手臂或羽翼。'),
        ('电梯回街面', '可见轿厢与下接街面的竖井，使放弃飞行仍能继续行程。'),
        ('地面出口', '门、实体踏步与街面公交构成另一个可观察的退出方向。'),
    ], '观察收翼的坐姿、公告和出口：不想起飞的人可以去哪里？', 760)


def _vertical():
    b = path('M124 202 L150 179 H771 V680 H124Z', SAND, INK, 1.8)
    b += rect(124, 202, 9, 487, CUT, INK, 0, 1.6)
    for yy in (202, 322, 442, 562, 682):
        for xx, ww in ((124, 175), (436, 138), (721, 50)):
            b += rect(xx, yy, ww, 8, CUT, INK, 0, 1.5)
        if yy > 202:
            b += _window(141, yy-94, 41, 66)
        if yy in (442, 562, 682):
            b += _stairs(193, yy, 94, 120)
    b += _lift(300, 202, 682, 135, 562, 111, people=False, floors=(322, 442, 562, 682))
    b += _person(345, 555, 72, 'stand', GREEN)+_person(398, 555, 45, 'stand', TERRA)
    b += _lift(576, 202, 682, 144, 442, 112, people=False, freight=True, floors=(322, 442, 562, 682))
    b += _person(486, 682, 85, 'walk', BLUE, elder=True)
    b += _person(508, 442, 83, 'stand', TERRA)
    b += path('M531 442 H564 M538 438 v-19 h15 M545 443 v8 M560 443 v8', stroke=INK, width=2)
    b += _box(540, 398, 27, 30)
    b += _shelter(145, 202, 131, 90)
    b += _seat(200, 202, .6)+_person(200, 202, 70, 'sit', BLUE)
    b += _water(477, 202, .66)+_person(532, 202, 71, 'drink', GREEN)
    b += _windsock(777, 202, .66)
    b += _person(487, 322, 79, 'prepare', BLUE)
    b += ground(55, 710, 793)+_coach(681, 712, 123, True)
    b += path('M128 695 H772 M304 688 l-4 7 M712 688 l8 7', stroke=MUTED, width=1.1)
    b += pin(1, 66, 520, 349, 555)+pin(2, 810, 386, 646, 421)
    b += pin(3, 500, 70, 476, 202)+pin(4, 76, 644, 242, 626)
    b += pin(5, 832, 624, 491, 682)
    return _scene('vertical', '载人轿厢与箱货轿厢分别接续楼层', b, [
        ('公共客梯', '成人与孩子在可见的载人轿厢内，双翼收拢而双手仍独立。'),
        ('箱货另行', '另一座竖井中的轿厢承托箱货，地面搬运接到楼层交接。'),
        ('真实屋顶门槛', '两座井壁和导轨一直到屋顶，公共生活不是只有飞行才能进入。'),
        ('楼梯并存', '连续踏步与各层楼板相接，不把楼梯画成所有人唯一的替代办法。'),
        ('街面接驳', '高龄居民与公交从同一个建筑入口参与，不被分配到次等空间。'),
    ], '比较两个剖开的轿厢：什么在承托人，什么在承托箱货？', 760)


def _dual_entry():
    b = path('M269 400 L294 375 H805 V649 H269Z', GLASS, INK, 1.8)
    b += path('M269 649 H805 L855 694 H321Z', SAND, INK, 1.6)
    b += rect(794, 400, 10, 256, CUT, INK, 0, 1.6)
    b += rect(269, 400, 525, 9, CUT, INK, 0, 1.5)
    b += path('M80 300 H269 V658 H80Z', SAND, INK, 1.8)
    b += rect(80, 300, 191, 9, CUT, INK, 0, 1.5)
    b += _window(95, 475, 43, 67)
    b += _lift(195, 300, 650, 74, 650, 100, floors=(486, 650))
    b += _person(132, 300, 50, 'land', BLUE, True)
    b += _windsock(78, 300, .57, -1)
    b += _flyer(92, 147, .66, 20)
    b += curve_arrow('M45 125 Q113 163 133 274', (133, 274), 1.4, BLUE, 2.5, '7 5')
    b += path('M275 649 V530 H337 V649 M275 530 H337 M326 583 v21', stroke=INK, width=2)
    b += path('M285 543 L304 535 V647 L285 652Z', PALE, INK, 1.4)
    b += path('M274 643 H390 M321 651 H804', stroke=INK, width=2)
    b += _person(353, 648, 93, 'walk', GREEN)
    b += _person(419, 651, 60, 'walk', TERRA)
    b += _person(477, 650, 95, 'walk', BLUE)
    b += _table(546, 631, 176)+book(583, 584, 39)+cup(651, 584, .5)
    b += _person(733, 630, 101, 'stand', TERRA)
    b += _seat(554, 657, .82)+_person(554, 657, 97, 'sit', GREEN, elder=True)
    b += _window(446, 429, 113, 99)+_window(644, 429, 107, 99)
    b += plant(785, 653, 59)+ground(31, 716, 831)+_coach(49, 715, 129, True)
    b += curve_arrow('M52 686 Q214 716 301 666 Q328 657 369 658', (369, 658), 0, TERRA, 2.8, '7 5')
    b += curve_arrow('M265 619 Q293 615 335 627 Q398 646 467 630', (467, 630), -.2, BLUE, 2.7, '7 5')
    b += pin(1, 222, 137, 132, 294)+pin(2, 81, 573, 232, 647)
    b += pin(3, 361, 736, 310, 648)+pin(4, 843, 508, 593, 598)
    return _scene('dual-entry', '两个入口进入同一大厅', b, [
        ('公共平台入口', '成人先在平台落地，再通过屋顶门槛进入公共电梯。'),
        ('楼内连接', '飞行到达者乘可见轿厢下到与街面来访者相同的大厅地板。'),
        ('街面入口', '步行、儿童随行和公交到达沿开着的门进入同一空间。'),
        ('同一大厅', '共享桌椅和服务台不按入口或个人飞行状态划分等级。'),
    ], '沿两种颜色的到达路径寻找相遇处：两边是否用了同一个大厅？', 780)


def _airspace():
    b = cloud(188, 87, 118)+cloud(605, 58, 96)
    b += _building(91, 673, 260, 3, 105, 1)
    b += _building(375, 673, 197, 4, 102, 2)
    b += _building(635, 673, 192, 3, 96, 1)
    b += _shelter(104, 358, 56, 73)+_water(647, 385, .5)
    b += _person(213, 358, 50, 'land', TERRA, True)
    b += _person(690, 385, 48, 'run', GREEN, True)
    b += _person(413, 265, 61, 'stand', BLUE)+_windsock(374, 265, .51)
    b += curve_arrow('M192 339 C121 243 224 164 368 142 S568 124 671 251 Q705 299 718 364', (718, 364), 1.3, BLUE, 3, '8 6')
    b += curve_arrow('M676 368 C604 278 659 132 729 90 C620 37 451 48 363 64 Q249 106 237 247 Q235 294 213 336', (213, 336), 2.05, TERRA, 3, '8 6')
    b += _flyer(348, 173, .59, -7)
    b += _flyer(678, 167, .57, -15, -1)
    b += path('M360 447 Q366 389 365 319 M605 372 Q624 336 621 298', stroke=LINE, width=1.7, dash='4 7')
    b += _person(317, 691, 71, 'walk', GREEN)+_coach(429, 713, 147, True)
    b += tree(61, 681, 106)+ground(33, 716, 827)
    b += pin(1, 324, 72, 367, 146)+pin(2, 807, 225, 778, 312)
    b += pin(3, 314, 736, 211, 414)+pin(4, 557, 77, 591, 206)
    return _scene('airspace', '避窗、转弯与分开的进近路线', b, [
        ('弯曲通行', '一条示例路线绕过几座接地楼，而不是把天空画成一根直线。'),
        ('进近分开', '到达两处平台的路径从不同方向弯入，各自留下制动空间。'),
        ('避开近窗', '路线与真实窗、外墙保持可观察的分离，私人窗口不是公共入口。'),
        ('非固定航层', '两条曲线是不同通行示例，随楼体和进近改变位置，不表示固定航层或同时占用交汇处。'),
    ], '观察两条曲线在哪里改变方向：它们为什么没有贴着窗经过？', 760)


def _wind():
    b = _building(355, 654, 215, 3, 112, 1)
    b += _building(674, 654, 161, 2, 91, 1)
    b += _shelter(85, 600, 180, 126)
    b += _seat(150, 600, .69)+_person(150, 600, 82, 'sit', GREEN)
    b += _person(228, 600, 80, 'stand', BLUE)+_notice(108, 491, 71, 46)
    b += _windsock(331, 318, .83)+_windsock(675, 472, .6, -1)
    b += _water(689, 472, .57)+_person(723, 472, 50, 'drink', TERRA)
    b += cloud(150, 130, 128)+ground(45, 694, 811)+_coach(298, 704, 128, True)
    b += curve_arrow('M46 264 C151 250 219 266 285 306 Q312 334 333 387', (333, 387), 1.18, BLUE, 2.8)
    b += curve_arrow('M51 306 C154 290 247 332 270 411 Q286 447 333 448', (333, 448), .08, BLUE, 2.1, '8 6')
    b += curve_arrow('M579 202 C652 269 631 339 611 425 Q598 507 632 575', (632, 575), 1.12, BLUE, 3)
    b += curve_arrow('M603 191 C678 288 669 367 647 417', (647, 417), 1.99, BLUE, 1.8, '8 7')
    b += curve_arrow('M608 560 C668 609 666 536 654 518 C629 494 605 527 622 546 Q639 563 650 549', (655, 549), -.5, TERRA, 2.6)
    b += curve_arrow('M836 465 Q867 501 836 551 Q809 572 796 558', (796, 558), -2.3, TERRA, 2, '6 6')
    b += path('M281 361 q14 -8 29 2 M606 488 q15 -8 28 3', stroke=LINE, width=1.2)
    b += pin(1, 90, 213, 287, 308)+pin(2, 751, 231, 613, 386)
    b += pin(3, 747, 626, 662, 542)+pin(4, 88, 660, 176, 574)
    return _scene('wind', '建筑旁的侧风、下洗与局部涡流', b, [
        ('侧风弯曲', '迎风侧的气流沿建筑边缘偏转，曲线只是作用示意而非固定风轨。'),
        ('下洗', '楼体旁的气流向下弯入邻近空间，楼越高不等于越适合起飞。'),
        ('涡流', '背风位置的小范围回旋说明不稳定扰动，不标风速或统一危险距离。'),
        ('落地观察与等待', '居民在候风厅和补水处稳定停留，结合风向标与公告改变选择。'),
    ], '沿弯曲箭头观察：哪些气流向下走，哪些在建筑旁回旋？', 750,
        '建筑形制与气流作用为淡彩示例，不按比例；气流不是航路或永久风轨，不提供风速阈值。')


def _commute():
    b = path('M37 271 Q222 265 368 271 T849 271 M38 555 Q267 549 448 555 T850 555', stroke=LINE, width=2)
    b += path('M46 252 V137 H192 M46 145 H70 M62 252 H191', stroke=INK, width=2)
    b += _window(56, 156, 47, 50)+_table(87, 254, 97)+cup(112, 208, .34)+book(154, 208, 26)
    b += _person(128, 255, 93, 'prepare', GREEN)
    b += _person(287, 255, 94, 'walk', GREEN)+plant(231, 263, 29)
    b += _lift(418, 256, 362, 102, 256, 107, floors=(355,))
    b += _shelter(644, 255, 173, 115)
    b += _seat(719, 255, .77)+_person(719, 255, 91, 'sit', GREEN)
    b += _notice(656, 152, 76, 48)+_windsock(815, 255, .6)
    b += _person(130, 535, 90, 'run', GREEN, True)
    b += path('M51 535 H205 L215 546 H51Z', CUT, INK, 1.4)
    b += _flyer(340, 432, .73, -8)
    b += _person(543, 535, 100, 'land', GREEN, True)
    b += path('M466 535 H623 V546 H466Z', CUT, INK, 1.4)
    b += _person(728, 547, 86, 'drink', GREEN)+_water(678, 550, .65)
    b += _table(777, 549, 75)+book(805, 504, 29)
    b += path('M771 550 V403 H854 M779 411 H853', stroke=INK, width=1.7)
    b += curve_arrow('M183 270 Q209 254 244 268', (244, 268), .35, TERRA, 2, '6 5')
    b += curve_arrow('M326 272 Q362 255 407 272', (407, 272), .2, TERRA, 2, '6 5')
    b += curve_arrow('M530 271 Q575 257 626 270', (626, 270), .15, TERRA, 2, '6 5')
    b += curve_arrow('M187 510 Q261 370 373 391 Q470 406 522 505', (522, 505), 1.07, BLUE, 2.5, '7 6')
    b += curve_arrow('M587 550 Q631 533 672 549', (672, 549), .3, TERRA, 2, '6 5')
    b += curve_arrow('M278 288 Q21 302 23 409 V654 Q371 694 847 654 L848 574', (848, 574), -math.pi/2, TERRA, 2.8, '9 6')
    b += _coach(359, 665, 182, True)+ground(71, 696, 747)
    b += pin(1, 48, 94, 126, 215)+pin(2, 373, 107, 465, 251)
    b += pin(3, 843, 104, 718, 239)+pin(4, 246, 377, 334, 430)
    b += pin(5, 603, 380, 541, 532)+pin(6, 637, 695, 467, 644)
    return _scene('commute', '八个生活动作与明确的公交支路', b, [
        ('家中准备', '早餐、羽面检查和轻装准备发生在出门之前，飞行者没有背大包。'),
        ('步行与电梯', '上带从家门步行到可见的公共轿厢，再到屋顶候风厅。'),
        ('收翼候风', '坐等与查看公告接续起飞前判断，未出发的人站在稳定空间。'),
        ('助跑与前进', '下带从助跑接到横向飞行，两手始终独立于背后的双翼。'),
        ('制动与恢复入工作', '脚触平台后再补水、收翼并进入旁边的工作空间。'),
        ('赭色公交支路', '步行后的另一条线沿街面公交直达同一工作入口，不必绕回屋顶。'),
    ], '先从左向右看上带，再看下带；找出不需要起飞的公交支路。', 760,
        '八步观察带与地面替代路线示例，不按比例、不规定耗时；不是漫画分格或统一通勤安排。')


def _landing_chain():
    b = _building(60, 666, 218, 2, 108, 1)
    b += _building(351, 666, 205, 3, 107, 1)
    b += _building(683, 666, 158, 2, 118, 1)
    b += _shelter(73, 450, 110, 85)
    b += _seat(113, 450, .54)+_person(113, 450, 63, 'sit', GREEN)
    b += _water(171, 450, .54)
    b += _seat(392, 345, .55)+_person(392, 345, 64, 'sit-drink', BLUE)
    b += _water(437, 345, .5)
    b += _person(730, 430, 50, 'prepare', GREEN)+_water(691, 430, .47)
    b += _windsock(352, 345, .55)+_windsock(842, 430, .52)
    b += _stairs(361, 666, 97, 107)
    b += _person(603, 693, 71, 'walk', BLUE)+_coach(453, 713, 129, True)
    b += _person(126, 690, 67, 'walk', TERRA, elder=True)
    b += tree(310, 680, 97)+plant(656, 682, 33)+ground(35, 716, 827)
    b += curve_arrow('M190 429 C253 265 324 274 385 326', (385, 326), .72, BLUE, 2.8, '8 6')
    b += curve_arrow('M456 323 C539 184 658 251 715 408', (715, 408), 1.15, BLUE, 2.8, '8 6')
    b += _flyer(301, 280, .57, 3)+_flyer(578, 248, .55, 9)
    b += curve_arrow('M535 681 Q566 668 598 681', (598, 681), .35, TERRA, 2.4, '7 5')
    b += curve_arrow('M798 681 Q710 713 631 688', (631, 688), -2.85, TERRA, 2.4, '7 5')
    b += pin(1, 49, 335, 111, 443)+pin(2, 371, 221, 438, 326)
    b += pin(3, 850, 306, 721, 427)+pin(4, 582, 607, 519, 664)
    b += pin(5, 648, 118, 583, 248)
    return _scene('landing-chain', '几个可休息、补给和退出的落点', b, [
        ('遮蔽休息', '第一处平台有座椅与补水，停留不保证马上恢复下一段能力。'),
        ('途中补给', '另一处实际屋顶供落地饮水和休息，服务形制并非节点统一模板。'),
        ('重新判断', '居民在第三处平台收翼检查，而不是把上一段顺利当作返程保证。'),
        ('多处退出地面', '每处节点都画出下接街面的电梯，中央另有楼梯与公交接续。'),
        ('间距不统一', '曲线路段和节点高低只表示接续关系，不是地图或等距航线。'),
    ], '在每个小平台找到休息或补水，再找出至少两处退出空中路线的办法。', 770,
        '落点接续与建筑形制示例，不按比例、不统一间距；不是实际区域地图，也不表示可以无限连续飞行。')


def _bicycle(x, floor, scale=1):
    b = ''
    for xx in (-62, 57):
        b += ellipse(xx, 0, 31, 31, WHITE, INK, 2)
        b += ellipse(xx, 0, 3, 3, MUTED)
        for dx, dy in ((28, 0), (0, 28), (20, 20), (20, -20)):
            b += line(xx-dx, -dy, xx+dx, dy, LINE, .8)
    b += path('M-62 0 L-32 -22 L10 -13 L57 0 M-32 -22 L-25 -47 M10 -13 L38 -38 L57 0 M38 -38 L43 -61 L61 -61 M-39 -47 H-13', stroke=MUTED, width=3)
    b += path('M-58 0 Q-10 17 10 -13 M-9 -13 l21 12 M5 -1 h13', stroke=INK, width=1.8)
    b += _limb('left-wing', path('M-34 -78 Q-61 -79 -59 -54 Q-54 -28 -35 -29 L-26 -61Z', SAND, INK, 1.5)+path('M-50 -71 Q-58 -48 -37 -34 M-42 -71 Q-49 -47 -32 -36', stroke=MUTED, width=1))
    b += _limb('right-wing', path('M-25 -78 Q-43 -75 -41 -53 L-24 -33 L-15 -60Z', SAND, INK, 1.5)+path('M-32 -70 Q-37 -51 -24 -39', stroke=MUTED, width=1))
    b += path('M-32 -82 Q-15 -89 -4 -79 L-8 -50 H-31Z', GREEN, INK, 1.8)
    b += ellipse(-18, -99, 12, 14, SKIN, INK, 1.5)
    b += path('M-30 -103 Q-18 -119 -7 -105 L-6 -97 Q-16 -105 -29 -98Z', MUTED, INK, 1)
    b += ellipse(-12, -99, 1.5, 1.5, INK)
    b += _limb('left-arm', path('M-25 -79 L4 -65 L48 -60', stroke=SKIN, width=5.5))
    b += _limb('right-arm', path('M-7 -77 L16 -58 L57 -60', stroke=SKIN, width=5.5))
    b += _limb('left-leg', path('M-26 -49 L-3 -29 L5 -4', stroke=INK, width=6))
    b += _limb('right-leg', path('M-13 -49 L19 -29 L27 -10', stroke=INK, width=6))
    b += path('M4 -3 h14 M27 -9 h13 M48 -60 l6 -3 M57 -60 l6 -2', stroke=INK, width=2)
    return group(x, floor, b, scale)


def _transport():
    b = _coach(64, 326, 392, True)
    b += path('M450 330 H831 M450 338 H831', stroke=MUTED, width=2)
    b += _shelter(507, 319, 208, 131)+_notice(680, 211, 33, 44)
    b += _person(533, 312, 85, 'walk', BLUE)+_person(590, 312, 55, 'walk', GREEN)
    b += _case(649, 315, 33, 45)
    b += _bicycle(205, 639, 1.35)+ground(62, 684, 312)
    b += _coach(457, 653, 384, False, True)
    # 铁路车厢前侧剖开，行李有独立位置，不让旅客背着大箱飞行。
    b += path('M471 626 H776 V638 H471Z', PAPER, LINE, 1)
    b += _seat(553, 627, .67)+_person(553, 627, 79, 'sit', BLUE)
    b += _seat(647, 627, .67)+_person(647, 627, 79, 'sit', TERRA, elder=True)
    b += _case(707, 634, 30, 51)+_case(745, 634, 25, 40)
    b += path('M699 575 H783 M699 636 H783 M784 575 V637', stroke=MUTED, width=1.8)
    b += path('M449 681 H850 M449 688 H850', stroke=INK, width=2)
    for xx in range(461, 842, 31):
        b += path(f'M{xx} 676 l-9 18', stroke=CUT, width=3)
    b += cloud(780, 122, 80)+plant(418, 676, 35)
    b += pin(1, 77, 135, 250, 282)+pin(2, 81, 462, 205, 546)
    b += pin(3, 836, 451, 736, 613)+pin(4, 480, 723, 579, 634)
    b += pin(5, 793, 238, 553, 310)
    return _scene('transport', '收翼乘车、低重心骑行与带行李铁路', b, [
        ('公交车内', '剖开的车身里居民收翼坐稳，座椅两侧背条留出翼位。'),
        ('低重心自行车', '骑者双翼折拢、上身不过度压翼根，两只手分别握在车把前端。'),
        ('独立行李位置', '大行李由铁路车厢承托，不被画成个人飞行载荷。'),
        ('长途机械接续', '旅客在真实车厢地板和座椅上休息，铁路不是空中能力的无限延长。'),
        ('共同地面参与', '成人与孩子在站台步行，高龄旅客也使用同一类乘坐空间。'),
    ], '观察手、翼和行李的位置：自行车与车厢怎样承托身体和物品？', 770)


def _navigation():
    b = path('M66 592 Q314 587 470 595 L838 636 M471 456 H844', stroke=LINE, width=2)
    b += _shelter(490, 458, 242, 139)
    b += _notice(512, 331, 91, 76)
    b += _person(558, 458, 81, 'stand', BLUE)
    b += _person(632, 458, 86, 'stand', GREEN)
    b += _seat(691, 458, .62)+_person(691, 458, 73, 'sit', TERRA)
    b += _lift(750, 458, 663, 103, 458, 109, floors=(654,))
    b += _windsock(678, 321, 1.02)
    b += path('M472 336 V511 M447 336 H495 V376 H447Z', SAND, INK, 1.6)
    b += path('M462 346 v18 l-6 -6 M462 364 l6 -6 M477 346 v18 M474 350 h6 M474 355 h6', stroke=BLUE, width=1.8)
    b += _water(804, 665, .6)+_coach(514, 696, 146, True)
    # 前景人物真正握持终端；界面只有三项状态词，不编读数、时间或阈值。
    p = _limb('left-wing', wing(False, SAND, -1))+_limb('right-wing', wing(False, SAND, 1))
    p += ellipse(0, -100, 13, 16, SKIN, INK, 1.8)
    p += path('M-13 -105 Q-5 -121 10 -110 L13 -101 Q1 -108 -11 -101Z', MUTED, INK, 1)
    p += ellipse(6, -100, 1.5, 1.8, INK)+path('M6 -94 l5 -1', stroke=INK, width=1)
    p += path('M-12 -80 Q0 -85 12 -80 L18 -42 Q0 -35 -18 -42Z', GREEN, INK, 1.8)
    p += _limb('left-leg', path('M-9 -42 L-11 0', stroke=INK, width=6.5))
    p += _limb('right-leg', path('M10 -42 L13 0', stroke=INK, width=6.5))
    p += path('M-11 1 h-12 M12 1 h14', stroke=INK, width=3.7)
    p += _phone(36, -96, .87, True)
    p += _limb('left-arm', path('M-13 -73 Q-24 -48 3 -48 L46 -62', stroke=SKIN, width=6))
    p += _limb('right-arm', path('M13 -73 L27 -53 L36 -44', stroke=SKIN, width=6))
    p += path('M36 -44 l3 -4 M46 -62 l3 -2', stroke=INK, width=1)
    b += group(218, 586, p, 2.35)
    b += cloud(801, 155, 99)+plant(81, 592, 45)
    b += pin(1, 390, 275, 337, 399)+pin(2, 429, 439, 469, 359)
    b += pin(3, 602, 169, 682, 243)+pin(4, 847, 340, 690, 433)
    b += pin(5, 839, 712, 800, 455)
    return _scene('navigation', '手持状态示例与现场基本标识', b, [
        ('三项状态', '手持界面仅示例天气、平台开放和拥挤信息，没有未知数字或全程安全承诺。'),
        ('现场方向', '实体指示牌把入口和向下连接留在现场，不只留在手机里。'),
        ('风向设施', '窗外的风向袋提供可观察提示，数字信息不能消除阵风。'),
        ('收翼等候', '现场居民在厅内站稳或坐等，开放不代表每个人都应当起飞。'),
        ('可退出的连接', '公共电梯与公交支持等待或改走地面，界面不显示个人永久轨迹。'),
    ], '把手中的三项提示与现场风向、公告和入口对应起来，哪里还能改走地面？', 770,
        '终端界面、建筑和标识形制为示例，不按比例；未规定更新频率、拥挤读数或气象阈值。')


def _privacy():
    b = _building(80, 680, 345, 3, 135, 1, False)
    b += _building(617, 680, 220, 3, 110, 1)
    b += _shelter(632, 350, 98, 82)+_person(671, 350, 57, 'stand', BLUE)
    b += _windsock(840, 350, .57)+_notice(635, 285, 49, 38)
    # 窗是有窗框、玻璃、窗台和帘子的住宅实物，室内人不从窗起飞。
    b += rect(128, 332, 143, 150, GLASS, MUTED, 0, 1.6)
    b += _seat(198, 479, .8)+_person(198, 479, 94, 'sit', GREEN)
    b += book(217, 443, 35)
    b += path('M128 332 H271 V482 H128Z M199 332 V482 M128 403 H271', stroke=MUTED, width=2.3)
    b += path('M131 335 H159 Q154 394 132 477Z M269 335 H242 Q247 394 268 477Z', SAND, MUTED, 1.2)
    b += path('M138 342 Q151 384 137 421 M263 342 Q250 384 264 421', stroke=WHITE, width=1)
    b += rect(123, 482, 154, 7, CUT, INK, 0, 1.4)
    b += _window(111, 546, 59, 71, True)+_window(219, 548, 57, 70, True)
    b += path('M87 279 H341 M94 287 H335', stroke=MUTED, width=1.7)
    b += curve_arrow('M44 159 C243 114 456 86 615 137 Q725 166 755 328', (755, 328), 1.4, BLUE, 2.9, '8 6')
    b += _flyer(485, 139, .69, 2)
    b += path('M444 217 Q451 287 486 346 M459 219 Q468 284 500 342', stroke=LINE, width=1.6, dash='5 7')
    b += _person(485, 700, 72, 'walk', TERRA)+_coach(276, 722, 142, True)
    b += ground(39, 726, 820)+tree(573, 701, 107)
    b += pin(1, 64, 372, 166, 405)+pin(2, 351, 80, 482, 139)
    b += pin(3, 797, 214, 678, 321)+pin(4, 376, 384, 466, 284)
    return _scene('privacy', '真实窗前与公共飞行路线分开', b, [
        ('住宅窗与窗帘', '窗内居民稳定阅读，真实窗框、窗台和帘子界定私人生活界面。'),
        ('公共通行另走', '成人沿远离窗前的弯曲路线前进，不在私人窗或屋顶随意停落。'),
        ('公共节点', '飞行路线接到有入口与电梯的公共平台，而不是把住宅窗口当作入口。'),
        ('空间与记录边界', '示意留开窗前空间，不规定距离，也不把平台运行信息画成全局个人记录。'),
    ], '比较窗内阅读者和公共平台：蓝色路线在哪里留开了窗前空间？', 780)


DIAGRAMS = {
    'city': _city(),
    'city-section': _city_section(),
    'platform': _platform(),
    'waiting': _waiting(),
    'vertical': _vertical(),
    'dual-entry': _dual_entry(),
    'airspace': _airspace(),
    'wind': _wind(),
    'commute': _commute(),
    'landing-chain': _landing_chain(),
    'transport': _transport(),
    'navigation': _navigation(),
    'privacy': _privacy(),
}
