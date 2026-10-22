"""文化百科线描淡彩插图；器物、场地与动作均为例示，不增补正典。"""
from common import *


__all__ = ['DIAGRAMS']


def _adult(x, y, h=130, pose='stand', shirt=GREEN, opened=False,
           back=False, facing=1):
    # 分别画双翼、双臂双手和双腿；衣物接缝仅为翼口形制草稿。
    b = '<g data-part="wing-left">' + wing(opened, SAND, -1) + '</g>'
    b += '<g data-part="wing-right">' + wing(opened, SAND, 1) + '</g>'
    b += ellipse(0, -101, 12, 15, '#E9C6A4', INK, 1.6)
    b += path('M-12 -105 Q-8 -119 5 -117 Q15 -113 12 -102 Q1 -110 -12 -105Z', MUTED, INK, 1)
    if not back:
        b += ellipse(5, -103, 1.4, 1.4, INK)
        b += ellipse(5, -94, 2.2, 3.1, INK) if pose == 'sing' else path('M3 -95 q4 2 7 -1', stroke=MUTED, width=.8)
    b += path('M-12 -82 Q0 -87 12 -82 L18 -42 Q0 -36 -18 -42Z', shirt, INK, 1.8)
    b += path('M-8 -81 Q0 -75 8 -81 M-14 -75 q-4 13 2 22 M14 -75 q4 13 -2 22', stroke=WHITE, width=1.2)
    b += line(-15, -46, 15, -46, MUTED, .8)
    if pose == 'sit':
        legs = [('M-9 -42 L-11 -24 L18 -22 L22 -2', (22, -1)),
                ('M9 -42 L15 -32 L34 -29 L35 -2', (35, -1))]
        arms = [('M-13 -74 Q-25 -57 -13 -42 L7 -37', (7, -37)),
                ('M13 -74 Q29 -58 28 -47 L19 -36', (19, -36))]
    elif pose == 'step':
        legs = [('M-9 -42 L-20 -21 L-32 -1', (-32, 0)),
                ('M9 -42 L23 -28 L36 -10', (36, -9))]
        arms = [('M-13 -74 L-27 -56 L-35 -68', (-35, -68)),
                ('M13 -74 L27 -55 L39 -51', (39, -51))]
    elif pose == 'glide':
        legs = [('M-9 -42 Q-19 -25 -14 -10', (-14, -9)),
                ('M9 -42 L23 -25 L32 -18', (32, -17))]
        arms = [('M-13 -74 L-29 -67 L-42 -59', (-42, -59)),
                ('M13 -74 L29 -65 L42 -67', (42, -67))]
    else:
        legs = [('M-9 -42 L-10 -21 L-11 -2', (-11, -1)),
                ('M9 -42 L11 -21 L13 -2', (13, -1))]
        if pose == 'care':
            arms = [('M-13 -74 Q-26 -55 -14 -44 L-1 -42', (-1, -42)),
                    ('M13 -74 Q36 -83 63 -75', (63, -75))]
        elif pose == 'offer':
            arms = [('M-13 -74 Q-27 -57 -22 -39', (-22, -39)),
                    ('M13 -74 L28 -57 L45 -61', (45, -61))]
        elif pose == 'read':
            arms = [('M-13 -74 Q-28 -56 -12 -48', (-12, -48)),
                    ('M13 -74 Q29 -56 12 -48', (12, -48))]
        elif pose == 'sweep':
            arms = [('M-13 -74 L-24 -58 L13 -47', (13, -47)),
                    ('M13 -74 L28 -56 L25 -35', (25, -35))]
        else:
            arms = [('M-13 -74 Q-26 -57 -23 -39', (-23, -39)),
                    ('M13 -74 Q28 -57 25 -39', (25, -39))]
    for side, (d, (xx, yy)) in zip(('left', 'right'), legs):
        b += '<g data-part="leg-' + side + '">'
        b += path(d, stroke=INK, width=8)
        b += path(f'M{xx-4} {yy-2} L{xx+5} {yy-2} L{xx+12} {yy+2} L{xx-5} {yy+2}Z', MUTED, INK, 1)
        b += '</g>'
    for side, (d, (xx, yy)) in zip(('left', 'right'), arms):
        b += '<g data-part="arm-' + side + '">'
        b += path(d, stroke='#E9C6A4', width=6)
        sleeve = 'M-13 -74 L-17 -66' if side == 'left' else 'M13 -74 L17 -66'
        b += path(sleeve, stroke=shirt, width=9)
        b += '<g data-part="hand-' + side + '">' + ellipse(xx, yy, 4, 3.5, '#E9C6A4', INK, .8) + '</g></g>'
    return (f'<g data-figure="adult" data-pose="{pose}" transform="translate({x} {y}) scale({h/118})">'
            f'<g transform="scale({facing} 1)">{b}</g></g>')


def _deck(x, y, w, drop=95):
    b = path(f'M{x} {y} l18 -11 h{w} l-18 11Z', SAND, INK, 1.8)
    b += path(f'M{x} {y} v9 h{w} v-9 M{x+w} {y} l18 -11 v9 l-18 11', PALE, INK, 1.5)
    for xx in (x+20, x+w-20):
        b += path(f'M{xx} {y+9} v{drop-9} h8 v{-drop+9}', SAND, INK, 1.5)
        b += line(xx, y+drop-15, xx+8, y+drop-15, MUTED, 1)
    b += path(f'M{x+30} {y+15} L{x+w-25} {y+drop-15} M{x+w-25} {y+15} L{x+30} {y+drop-15}', stroke=LINE, width=2)
    for xx in range(int(x+16), int(x+w), 22):
        b += line(xx, y, xx+18, y-11, MUTED, .8)
    return b


def _sack(x, y, w=38, h=56):
    b = path(f'M{x+8} {y} Q{x+w/2} {y+4} {x+w-8} {y} L{x+w-11} {y+9} Q{x+w+7} {y+h*.65} {x+w-3} {y+h} Q{x+w/2} {y+h+6} {x+3} {y+h} Q{x-7} {y+h*.65} {x+11} {y+9}Z', SAND, INK, 1.5)
    b += line(x+8, y+9, x+w-8, y+9, MUTED, 1.4)
    b += path(f'M{x+10} {y+19} q-4 14 0 24 M{x+w-9} {y+22} q4 12 0 20', stroke=MUTED, width=.8)
    return b


def _granary(x, y, w=180, h=170):
    b = path(f'M{x} {y} V{y-h} L{x+w} {y-h} V{y}Z', SAND, INK, 1.8)
    b += path(f'M{x-10} {y-h} L{x+w*.5} {y-h-30} L{x+w+10} {y-h}Z', PALE, INK, 1.8)
    b += rect(x+20, y-92, w-40, 92, '#F4EBDC', INK, 0, 1.6)
    b += path(f'M{x+17} {y-96} h{w-34} M{x+16} {y} h{w-32}', stroke=MUTED, width=3)
    for xx in (x+26, x+w-51):
        b += rect(xx, y-h+22, 24, 26, PALE, INK, 0, 1)
        for yy in range(int(y-h+27), int(y-h+44), 6):
            b += line(xx+3, yy, xx+21, yy, MUTED, .8)
    b += _sack(x+31, y-60, 34, 53) + _sack(x+67, y-68, 35, 61)
    b += _sack(x+104, y-56, 32, 49)
    for yy in (y-h+65, y-15):
        b += path(f'M{x+3} {yy} h13 M{x+w-16} {yy} h13', stroke=GOLD, width=1)
    return b


def _railway(x, y, w=300):
    b = path(f'M{x} {y-8} H{x+w} M{x} {y+3} H{x+w}', stroke=INK, width=2)
    for xx in range(int(x+8), int(x+w-4), 17):
        b += line(xx, y-13, xx-7, y+10, MUTED, 2)
    return b


def _train(x, y, scale=1):
    b = rect(12, -70, 90, 48, PALE, INK, 3, 1.7)
    b += path('M7 -71 Q55 -87 109 -71 M12 -23 H109 M96 -69 L114 -66 L114 -23', stroke=INK, width=2)
    for xx in (23, 49, 75):
        b += rect(xx, -60, 18, 23, WHITE, INK, 2, 1.2)
        b += line(xx+9, -60, xx+9, -37, LINE, .8)
    b += path('M123 -25 V-68 H146 V-51 H193 Q212 -51 217 -29 V-25Z', TERRA, INK, 1.8)
    b += rect(129, -63, 12, 16, WHITE, INK, 0, 1)
    b += rect(190, -81, 13, 31, SAND, INK, 0, 1.4)
    b += path('M185 -82 h24 M217 -25 l9 10 h-22 M107 -21 h16 M125 -29 h78', stroke=INK, width=2)
    for xx in (28, 86, 139, 172, 204):
        b += ellipse(xx, -13, 10, 10, MUTED, INK, 1.5)
        b += ellipse(xx, -13, 3, 3, SAND, INK, 1)
    b += line(139, -13, 204, -13, GOLD, 3)
    return group(x, y, b, scale)


def _filter(x, y, w=60, h=96):
    b = rect(x, y, w, h, PALE, INK, 3, 1.6)
    b += rect(x+8, y+10, w-16, h-27, WHITE, INK, 1, 1)
    for yy in range(int(y+17), int(y+h-18), 9):
        b += path(f'M{x+12} {yy} l8 -4 l8 4 l8 -4 l8 4', stroke=LINE, width=1.2)
    b += line(x+12, y+h-11, x+w-13, y+h-11, MUTED, 1)
    b += ellipse(x+w-9, y+h-10, 2.2, 2.2, GREEN)
    return b


def _factory(x, y, scale=1):
    # 排气收集、隔离作业与室内过滤画成不同实物，不表示工程设计标准。
    b = path('M0 0 V-150 L48 -181 V-150 L96 -181 V-150 H240 V0Z', SAND, INK, 1.8)
    for xx in (12, 62, 112):
        b += rect(xx, -130, 31, 32, PALE, INK, 0, 1.2)
        b += line(xx+15, -130, xx+15, -98, LINE, 1)
    b += path('M15 -66 H82 L73 -87 H24Z', MUTED, INK, 1.7)
    b += path('M45 -87 V-189 H143 V-209', stroke=INK, width=11)
    b += path('M45 -87 V-189 H143 V-209', stroke=SAND, width=7)
    b += _filter(122, -266, 45, 57)
    b += path('M144 -266 V-290 H164 M138 -286 h26', stroke=INK, width=5)
    b += rect(23, -50, 57, 42, TERRA, INK, 2, 1.5)
    b += ellipse(52, -30, 15, 15, SAND, INK, 1.4)
    b += ellipse(52, -30, 4, 4, MUTED)
    b += path('M12 -4 V-77 H93 V-4 M12 -63 H93', stroke=BLUE, width=3)
    for xx in (17, 37, 57, 77):
        b += path(f'M{xx} -77 l8 9', stroke=GOLD, width=3)
    b += _filter(173, -99, 49, 77)
    b += _adult(131, -1, 103, pose='read', shirt=GREEN)
    b += rect(116, -53, 28, 17, WHITE, INK, 1, 1)
    b += path('M123 -48 h14 M123 -43 h10', stroke=LINE, width=1)
    b += ground(-5, 7, 252)
    return group(x, y, b, scale)


def _service(x, y, scale=1, lamps=False):
    # 剖开的是同一栋接地建筑；两条入口线在同一柜台前结束。
    b = path('M30 0 V-277 H292 V0 M30 -277 h292 M25 5 h298', stroke=INK, width=2.2)
    b += path('M30 -277 H292 V-244 H127 V-20 H292 V0 H30Z', SAND, 'none')
    b += _deck(130, -280, 188, 30)
    b += path('M312 -241 V0 M130 -247 V-108', stroke=INK, width=3)
    b += rect(59, -271, 59, 269, PALE, INK, 0, 1.5)
    b += line(65, -263, 65, -4, MUTED, 1)
    b += line(112, -263, 112, -4, MUTED, 1)
    b += rect(67, -92, 43, 88, WHITE, INK, 1, 1.3)
    b += line(89, -90, 89, -4, LINE, 1)
    b += path('M67 -254 V-217 H110 V-254 M30 -96 H55 V0 M123 -82 V0 M292 -99 V0', stroke=INK, width=2)
    b += _adult(226, -1, 104, shirt=GREEN)
    b += rect(171, -49, 91, 8, GOLD, INK, 1, 1.4)
    b += path('M178 -41 V-1 M256 -41 V-1', stroke=INK, width=3)
    b += book(235, -57, 31)
    b += _adult(148, -1, 87, pose='read', shirt=TERRA)
    b += _adult(18, -1, 85, pose='step', shirt=BLUE)
    b += _adult(244, -282, 86, shirt=TERRA)
    b += path('M21 -108 V-140 H48 V-108 M22 -124 h24', stroke=MUTED, width=1.6)
    b += arrow([(26, -123), (44, -123)], GREEN, 1.6)
    b += path('M137 -281 V-316 H158 V-281', stroke=MUTED, width=1.6)
    b += arrow([(155, -302), (138, -302)], GREEN, 1.6)
    b += arrow([(8, 17), (44, 17), (45, -15), (136, -15), (165, -25)], BLUE, 2, '5 5')
    b += arrow([(221, -271), (122, -271), (91, -244), (91, -112)], TERRA, 2, '5 5')
    b += arrow([(91, -99), (91, -15), (136, -15), (165, -25)], TERRA, 2, '5 5')
    if lamps:
        for xx in (173, 280, 316):
            b += path(f'M{xx} -280 v-22 l8 -4', stroke=MUTED, width=1.5)
            b += path(f'M{xx+3} -306 h12 l-2 7 h-8Z', GOLD, INK, 1)
            b += ellipse(xx+9, -296, 9, 3, SAND)
    b += ground(0, 24, 330)
    return group(x, y, b, scale)


def _weather_device(x, y, scale=1):
    b = rect(-33, -74, 66, 104, MUTED, INK, 8, 1.8)
    b += rect(-27, -66, 54, 84, WHITE, INK, 3, 1)
    b += cloud(0, -47, 31)
    b += path('M-17 -27 h34 M-17 -14 h23', stroke=LINE, width=2)
    b += ellipse(-13, 1, 4, 4, GREEN, INK, 1)
    b += path('M-2 -2 h18 M-2 5 h10', stroke=BLUE, width=1.5)
    b += ellipse(0, 24, 2.5, 2.5, WHITE)
    return group(x, y, b, scale)


def _history():
    # 六幅无框的小景按阅读顺序排布，场景间不用线性进步箭头。
    a = path('M4 223 Q45 199 84 199 L111 145 L183 138 L201 75 L239 68 L248 221Z', SAND, MUTED, 1.6)
    a += path('M28 223 L59 207 M99 173 l18 -23 M170 160 l19 -28 M218 126 l15 -27', stroke=GOLD, width=1)
    a += _deck(111, 148, 67, 73)
    a += path('M115 148 Q103 131 113 118 Q142 102 178 117 L184 146', PALE, INK, 1.6)
    a += path('M115 137 q32 -13 62 2 M125 122 q25 -8 44 2', stroke=MUTED, width=.9)
    a += path('M-4 155 Q23 115 77 126 L88 153 M8 155 V220', PALE, INK, 1.6)
    a += ellipse(67, 219, 23, 8, SAND, INK, 1.3)
    for xx, yy, rr in ((50, 218, 5), (61, 225, 5), (75, 225, 4), (86, 217, 5)):
        a += ellipse(xx, yy, rr, 3, LINE, INK, .8)
    a += path('M57 215 Q58 204 65 199 Q63 211 71 214 Q69 201 76 198 Q85 211 79 217Z', TERRA, INK, 1)
    a += path('M3 202 Q15 193 29 202 L33 220 H1Z M98 202 Q112 194 125 202 L128 220 H96Z', SAND, INK, 1.2)
    a += _adult(19, 221, 64, pose='sit', facing=1, shirt=BLUE)
    a += _adult(111, 221, 62, pose='sit', facing=-1, shirt=GREEN)
    a += ground(0, 236, 257)
    a += pin(1, 20, 40, 133, 148)

    b = path('M0 92 Q65 56 109 71 Q195 22 250 85', stroke=LINE, width=1.5)
    b += path('M-1 208 Q94 196 151 207 T267 203 M1 220 Q97 209 155 220 T267 218', stroke=BLUE, width=2)
    b += _granary(56, 194, 151, 132)
    b += _deck(80, 69, 86, 124)
    b += path('M86 58 V23 H160 V58 M83 23 L121 3 L166 23', PALE, INK, 1.4)
    b += path('M81 87 h95 M86 104 h85', stroke=MUTED, width=.9)
    b += _adult(239, 200, 79, pose='stand', shirt=TERRA)
    b += _sack(215, 166, 28, 35)
    b += path('M5 207 h47 l-9 11 h-26Z', SAND, INK, 1.4)
    b += _sack(16, 188, 22, 18)
    b += ground(0, 233, 266) + pin(2, 8, 37, 66, 132)

    c = _deck(21, 147, 206, 80)
    c += path('M32 137 V49 H109 V137 M27 49 L71 27 L116 49', PALE, INK, 1.5)
    c += rect(43, 69, 48, 56, SAND, INK, 1, 1.3)
    c += desk(40, 144, 59) + book(69, 97, 35)
    c += _adult(136, 146, 91, pose='offer', shirt=BLUE)
    c += _adult(205, 146, 91, shirt=TERRA, facing=-1)
    c += parcel(169, 96, 15)
    c += cup(101, 128, .45)
    c += path('M225 147 V93 M224 94 l29 -7 l-10 11Z', SAND, INK, 1.3)
    c += path('M146 219 h31 M153 210 h18', stroke=LINE, width=1.5)
    c += ground(0, 235, 270) + pin(3, 10, 24, 70, 97)

    d = _railway(0, 224, 264) + _train(3, 219, 1.08)
    d += path('M17 119 V68 L71 47 L130 68 V119 M10 68 h126', PALE, INK, 1.5)
    d += rect(33, 79, 65, 40, SAND, INK, 1)
    d += ellipse(58, 105, 11, 11, WHITE, INK, 1.2)
    d += path('M57 94 v22 M46 105 h23 M86 96 v22', stroke=MUTED, width=1.3)
    d += desk(166, 130, 74) + book(200, 77, 62)
    d += path('M181 63 h15 M206 61 h15 M181 72 h11 M206 70 h13', stroke=BLUE, width=.8)
    d += pin(4, 13, 25, 159, 193)

    e = _service(0, 236, .76)
    e += bus(130, 252, 94)
    e += _railway(2, 269, 258)
    e += pin(5, 13, 9, 161, 32)

    f = path('M8 239 V136 H259 V239 M6 135 H263', SAND, INK, 1.7)
    f += rect(18, 156, 64, 79, PALE, INK, 1, 1.2)
    f += path('M50 156 v79 M18 192 h64', stroke=LINE, width=1)
    f += _adult(132, 238, 99, pose='read', shirt=BLUE)
    f += _weather_device(132, 188, .31)
    f += chair(198, 239, .65) + _adult(198, 239, 74, pose='sit', shirt=GREEN)
    f += desk(185, 241, 64) + cup(217, 187, .5)
    f += path('M221 135 V71 M219 75 h34 M236 64 v21 M229 68 l14 13 M229 81 l14 -13', stroke=INK, width=1.5)
    f += path('M220 94 l-24 -7 l8 10Z', GOLD, INK, 1)
    f += cloud(49, 65, 68) + path('M74 82 q20 10 35 0', stroke=BLUE, width=1.2)
    f += ground(0, 254, 265) + pin(6, 16, 20, 132, 172)
    return (group(28, 60, a) + group(319, 60, b) + group(610, 60, c)
            + group(28, 445, d) + group(319, 430, e) + group(610, 435, f))


def _events():
    a = _granary(15, 249, 214, 154)
    a += _railway(12, 280, 387) + truck(241, 265, 153)
    a += crate(217, 215, 45, 36) + crate(239, 179, 42, 34)
    a += _adult(447, 269, 101, pose='step', shirt=BLUE)
    a += _adult(544, 269, 91, pose='sit', shirt=TERRA) + chair(544, 269, .77)
    a += path('M470 145 V69 H624 V145 M480 69 h134 M475 129 h144', stroke=MUTED, width=1.8)
    a += path('M470 145 H624 V153 H470Z M474 153 V269 M620 153 V269', PALE, INK, 1.6)
    a += path('M602 69 V31 H627 V69', PALE, INK, 1.2)
    a += path('M605 40 l19 20 M624 40 l-19 20', stroke=TERRA, width=2)
    for xx, yy, ww in ((87, 46, 165), (253, 75, 143), (458, 42, 157), (659, 100, 153)):
        a += group(xx, yy, path(f'M{-ww/2} 0 q{ww*.24} -12 {ww*.49} 0 t{ww*.51} 0 M{-ww/2+13} 14 q{ww*.3} -9 {ww*.7} 0', stroke=BLUE, width=2, opacity=.45))
    a += arrow([(181, 261), (227, 261)], BLUE, 2)
    a += ground(9, 287, 809) + pin(1, 30, 33, 111, 181) + pin(2, 694, 43, 610, 52)

    b = _factory(28, 313, .97)
    b += path('M340 311 V206 H585 V311 M335 206 H592', PALE, INK, 1.6)
    b += _filter(521, 223, 52, 74)
    b += chair(414, 312, .85) + _adult(414, 312, 101, pose='sit', shirt=BLUE)
    b += path('M470 310 V233 M462 232 h27 M477 242 v41', stroke=MUTED, width=1.8)
    b += path('M475 253 q-10 9 0 17 M487 253 q-10 9 0 17', stroke=BLUE, width=1.3)
    b += feather(682, 139, 137, SAND, -19)
    for xx, yy in ((678, 160), (670, 183), (695, 197), (704, 219), (684, 207)):
        b += ellipse(xx, yy, 3.4, 2.8, MUTED)
    b += path('M678 173 Q695 166 700 181 Q689 190 678 185Z', GOLD, MUTED, 1, opacity=.6)
    b += ground(4, 328, 810)
    b += pin(3, 23, 24, 165, 65) + pin(4, 747, 100, 682, 182)

    c = _service(160, 316, .94)
    c += _adult(88, 315, 103, pose='step', shirt=GREEN)
    c += bus(16, 318, 130)
    c += _adult(664, 316, 101, pose='sit', shirt=BLUE) + chair(664, 316, .86)
    c += tree(749, 319, 138)
    c += ground(7, 340, 816) + pin(5, 25, 46, 413, 47) + pin(6, 577, 140, 352, 278)
    return group(38, 10, a) + group(38, 331, b) + group(38, 683, c)


def _governance():
    a = path('M28 260 V65 H209 V260 M23 64 H216', SAND, INK, 1.8)
    a += rect(71, 96, 92, 110, PALE, INK, 1, 1.6)
    a += rect(77, 102, 80, 98, WHITE, MUTED, 0, 1)
    a += path('M118 101 v99 M78 155 h78 M72 212 h89', stroke=INK, width=1.5)
    a += path('M78 104 q22 34 7 88 M156 104 q-22 34 -7 88', stroke=LINE, width=4)
    a += chair(123, 198, .48) + _adult(123, 198, 57, pose='sit', shirt=GREEN)
    a += book(136, 173, 26)
    a += path('M248 260 L314 202 L408 176 M258 269 L324 212 L408 187', stroke=BLUE, width=1.4, dash='6 6')
    a += _adult(335, 187, 81, pose='glide', opened=True, shirt=BLUE)
    a += arrow([(310, 209), (370, 190), (405, 184)], BLUE, 1.7)
    a += ground(17, 273, 398) + pin(1, 24, 27, 97, 137) + pin(2, 388, 35, 347, 202)

    b = _deck(472, 228, 326, 70)
    b += path('M493 225 V131 H561 V225 M487 131 h81', PALE, INK, 1.5)
    b += rect(503, 143, 48, 76, WHITE, INK, 1, 1.2)
    b += line(527, 143, 527, 219, LINE, 1)
    b += _adult(618, 227, 128, pose='read', shirt=TERRA)
    b += rect(599, 166, 39, 25, WHITE, INK, 1, 1.2)
    b += path('M606 174 h22 M606 182 h13', stroke=LINE, width=1.3)
    b += _adult(733, 227, 109, shirt=GREEN)
    b += path('M765 228 V151 H788 V228', PALE, INK, 1.3)
    b += arrow([(770, 168), (783, 168)], BLUE, 1.4)
    b += ellipse(777, 187, 4, 4, GREEN, INK, 1)
    b += path('M690 225 h22 M696 217 h16 M704 206 h12', stroke=BLUE, width=1.4)
    b += ground(460, 309, 369) + pin(3, 485, 31, 620, 179)

    c = _service(25, 347, .91)
    c += _weather_device(427, 227, .82)
    c += path('M421 321 H499 M439 321 V293 M481 321 V293', stroke=MUTED, width=2)
    c += _adult(598, 346, 119, pose='read', shirt=BLUE)
    c += book(598, 287, 40)
    c += tree(761, 347, 170)
    c += ground(8, 368, 815)
    c += path('M383 203 Q359 201 353 241 M480 203 Q542 232 560 279', stroke=LINE, width=1.6, dash='4 5')
    c += pin(4, 44, 23, 226, 93) + pin(5, 471, 114, 427, 191)
    return group(28, 24, a+b) + group(28, 345, c)


def _culture():
    a = _deck(46, 235, 221, 155) + _deck(285, 308, 189, 82)
    a += path('M48 232 V180 M260 232 V180 M48 180 h29 M231 180 h29', stroke=MUTED, width=1.8)
    a += path('M287 305 V262 M468 305 V262 M287 262 h20 M448 262 h20', stroke=MUTED, width=1.6)
    a += _adult(113, 233, 125, pose='sing', shirt=BLUE)
    a += _adult(203, 233, 122, pose='sing', shirt=TERRA)
    a += _adult(340, 306, 119, pose='sing', shirt=GREEN)
    a += _adult(421, 306, 114, pose='sing', shirt=BLUE)
    a += path('M17 390 V246 H45 V390 M17 266 h28 M17 304 h28 M17 342 h28', PALE, INK, 1.5)
    a += path('M4 390 H491', stroke=LINE, width=2)
    for xx, yy, col in ((90, 439, GREEN), (191, 459, BLUE), (302, 448, TERRA), (412, 472, GREEN)):
        a += chair(xx, yy, .81) + _adult(xx, yy, 96, pose='sit', shirt=col)
    a += ground(25, 480, 463)
    a += pin(1, 51, 36, 117, 234) + pin(2, 411, 130, 342, 305)
    a += pin(3, 39, 528, 192, 455)

    b = path('M557 376 Q623 353 788 376 L815 398 Q683 421 541 399Z', PALE, INK, 1.7)
    b += path('M557 400 v12 Q702 433 815 410 v-12', SAND, INK, 1.3)
    b += path('M574 377 q10 -5 25 -5 M752 389 q12 -4 25 -3', stroke=BLUE, width=2)
    b += _adult(657, 272, 101, pose='glide', opened=True, shirt=TERRA)
    b += curve_arrow('M558 212 Q569 192 596 194', (596, 194), .08, BLUE, 1.8, '5 5')
    b += curve_arrow('M722 271 Q772 311 752 364', (752, 364), 1.94, BLUE, 1.8, '5 5')
    b += ground(540, 434, 289) + pin(4, 801, 164, 752, 383)

    c = path('M28 647 L283 630 L361 684 L99 706Z', SAND, INK, 1.5)
    c += path('M99 706 v8 l262 -22 v-8 M45 650 v77 M336 693 v34', stroke=INK, width=2)
    c += path('M63 650 l66 -5 l35 31 l-67 6Z', PALE, INK, 1.2)
    for i in range(6):
        c += line(69+i*9, 650, 101+i*9, 678, GREEN, .9)
        c += line(76+i*3, 653+i*4, 133+i*3, 649+i*4, LINE, .9)
    c += feather(190, 650, 65, SAND, -58) + feather(235, 646, 52, PALE, 43)
    c += ellipse(285, 665, 15, 9, WHITE, INK, 1.2)
    c += path('M272 664 q14 -8 25 1 M275 669 q10 -6 17 0 M260 679 q-14 15 -29 6', stroke=GOLD, width=1.2)
    c += pin(5, 20, 586, 163, 665)

    d = path('M472 653 L751 632 L817 681 L528 707Z', SAND, INK, 1.5)
    d += book(620, 644, 161)
    d += path('M565 614 q28 -7 41 0 M565 624 q25 -7 39 0 M636 613 q25 -7 45 0 M636 624 q28 -7 40 0', stroke=LINE, width=1.3)
    d += path('M720 654 l25 -27 l5 4 l-27 25Z', GOLD, INK, 1.2)
    d += cup(775, 659, .67)
    d += path('M526 708 v8 l291 -27 M490 656 v68 M797 690 v34', stroke=INK, width=2)
    d += pin(6, 481, 582, 624, 646)
    return group(29, 29, a+b+c+d)


def _etiquette():
    a = path('M35 435 V92 H202 V435 M30 91 H212 M43 99 H193 V434', SAND, INK, 1.8)
    a += path('M44 434 V146 H177 V434 M44 145 H177', WHITE, INK, 1.7)
    a += path('M177 146 L213 165 V435 L177 435Z', PALE, INK, 1.4)
    a += ellipse(205, 302, 3, 3, MUTED)
    a += path('M29 435 H429 M36 447 H422 M236 371 H393 M270 398 H411', stroke=LINE, width=1.6)
    a += _adult(270, 432, 157, shirt=BLUE)
    a += _adult(130, 434, 147, pose='step', shirt=TERRA)
    a += path('M230 338 q-9 19 -2 38 M316 338 q9 19 2 38', stroke=BLUE, width=1.6)
    a += arrow([(213, 470), (165, 470), (118, 468)], BLUE, 2, '5 5')
    a += ground(30, 480, 401) + pin(1, 37, 47, 266, 370) + pin(2, 413, 217, 133, 432)

    b = path('M471 438 V245 H814 V438 M461 244 H824', PALE, INK, 1.6)
    b += path('M488 438 H817 M514 451 H799', stroke=LINE, width=1.5)
    b += _adult(575, 440, 162, pose='care', shirt=GREEN)
    b += _adult(718, 440, 173, back=True, shirt=BLUE)
    b += path('M549 380 q13 -13 24 -4 l8 18 l-30 5Z', WHITE, INK, 1.2)
    b += path('M555 385 l18 -5 M554 391 l22 -5', stroke=LINE, width=.9)
    b += desk(744, 448, 79) + cup(781, 394, .61)
    b += path('M680 319 q17 -8 27 1 M678 328 q16 -8 27 1', stroke=MUTED, width=.9)
    b += ground(456, 480, 376)
    b += feather(597, 543, 104, SAND, -34)
    b += path('M596 568 q16 1 25 12 M605 597 q10 0 18 10', stroke=BLUE, width=1.1)
    b += path('M688 563 L819 563 M701 570 L806 570 M707 574 V625 M801 574 V625', stroke=INK, width=2)
    b += path('M722 536 q30 -13 53 0 l10 24 l-69 0Z', WHITE, INK, 1.2)
    b += path('M725 543 q20 -8 42 0 M726 551 h46', stroke=LINE, width=1)
    b += pin(3, 504, 67, 651, 337) + pin(4, 486, 574, 608, 600)
    return group(22, 24, a+b)


def _festivals():
    a = _service(225, 370, .96, lamps=True)
    a += _adult(123, 370, 111, pose='step', shirt=BLUE)
    a += path('M605 371 H801 M620 375 V316 H788 V375', PALE, INK, 1.6)
    a += chair(676, 371, .81) + _adult(676, 371, 95, pose='sit', shirt=TERRA)
    a += chair(776, 371, .78) + _adult(776, 371, 92, pose='sit', shirt=GREEN)
    a += book(699, 320, 45)
    a += tree(72, 376, 139)
    a += ground(17, 400, 818)
    a += pin(1, 246, 37, 507, 78) + pin(2, 29, 168, 390, 351)

    b = path('M348 325 V181 H590 V325 M340 181 H599', SAND, INK, 1.7)
    b += path('M361 325 V210 H426 V325 M440 202 H575 V293', WHITE, INK, 1.3)
    b += path('M444 247 H573 M507 203 V290', stroke=LINE, width=1.2)
    b += tree(65, 329, 186) + tree(784, 329, 178)
    b += path('M155 312 Q427 285 710 313 L736 353 Q419 376 127 352Z', PALE, GREEN, 1.4)
    for xx, yy, col in ((203, 328, BLUE), (332, 334, TERRA), (533, 337, GREEN), (657, 335, BLUE)):
        b += chair(xx, yy, .8) + _adult(xx, yy, 94, pose='sit', shirt=col)
    b += desk(375, 350, 124) + cup(403, 298, .6) + cup(467, 298, .6)
    b += book(440, 294, 44)
    b += _adult(105, 329, 94, pose='read', shirt=GREEN)
    b += book(105, 281, 36)
    b += _adult(734, 330, 105, pose='step', shirt=TERRA, facing=-1)
    b += ground(16, 384, 818)
    b += pin(3, 36, 49, 329, 336) + pin(4, 714, 58, 440, 294)
    return group(24, 20, a) + group(24, 442, b)


def _memorial():
    b = path('M70 370 L633 304 L823 414 L235 514Z', SAND, INK, 1.8)
    b += path('M70 370 V382 L235 527 L823 426 V414 M235 514 V527', PALE, INK, 1.4)
    b += path('M107 391 V557 M785 438 V557', stroke=INK, width=4)
    b += path('M121 392 q160 -20 291 -35 M375 478 q120 -28 227 -44 M580 332 q56 -9 97 9', stroke=GOLD, width=1)

    b += path('M132 305 L277 287 L316 382 L167 405Z', WHITE, INK, 1.4)
    b += path('M140 312 L273 295 L307 377 L172 397Z', PALE, LINE, 1)
    b += feather(192, 319, 88, SAND, -18)
    b += feather(240, 321, 57, PALE, 18)
    b += path('M166 341 l28 -3 M213 378 l23 -3', stroke=GOLD, width=3)
    b += pin(1, 103, 244, 207, 354)

    b += path('M351 183 L580 169 L606 324 L377 346Z', WHITE, INK, 1.7)
    b += path('M351 183 l19 -9 l227 -13 l-17 8 M580 169 l17 -8 l25 154 l-16 9', SAND, INK, 1.1)
    b += path('M376 204 q53 -8 83 -1 M478 196 q24 -4 53 -2', stroke=MUTED, width=1.3)
    # 墨迹线只示意手写质感，不拟造地方文字、姓名或信件内容。
    for i, yy in enumerate((224, 240, 256, 272, 288)):
        xx = 379 + i*2
        b += path(f'M{xx} {yy} q11 -8 17 -1 t18 -2 q8 6 13 -2 t17 0 q9 -5 14 -1', stroke=MUTED, width=1.1)
        b += path(f'M{xx+88} {yy-5} q8 -6 14 -1 t18 -1 q7 6 13 -1', stroke=MUTED, width=1.1)
    b += path('M414 325 L580 311 L640 355 L469 379Z', PALE, INK, 1.5)
    b += path('M414 325 L529 352 L580 311 M469 379 L500 352 M640 355 L561 346', stroke=INK, width=1.1)
    b += pin(2, 333, 126, 455, 253)

    b += path('M594 357 L725 339 L770 413 L639 436Z', WHITE, INK, 1.6)
    b += path('M604 369 L726 352 M615 387 L737 369 M626 404 L747 386', stroke=LINE, width=1.1)
    for i in range(3):
        b += ellipse(620+i*13, 374+i*17, 3, 3, BLUE, INK, .8)
        b += path(f'M{635+i*13} {373+i*17} l41 -6 M{635+i*13} {379+i*17} l24 -3', stroke=MUTED, width=1)
    b += pin(3, 792, 296, 696, 387)

    b += path('M245 398 Q331 365 402 386 Q469 355 548 368 L588 448 Q505 435 432 473 Q359 460 282 490Z', TERRA, INK, 1.7)
    b += path('M251 390 Q328 358 400 379 Q470 349 542 360 L580 438 Q505 426 429 463 Q358 451 288 479Z', WHITE, INK, 1.5)
    b += path('M400 379 L429 463 M251 390 L245 398 M542 360 L548 368', stroke=INK, width=1.2)
    for i in range(4):
        b += path(f'M{290+i*4} {404+i*13} q47 -18 91 -6', stroke=LINE, width=1.2)
        b += path(f'M{444+i*4} {388+i*13} q40 -14 73 -7', stroke=LINE, width=1.2)
    b += feather(494, 385, 68, SAND, -16)
    b += path('M483 405 l25 -5 M497 434 l20 -4', stroke=GOLD, width=3)
    b += pin(4, 170, 531, 392, 426)
    return b


def _pollution():
    a = _factory(31, 330, 1.03)
    a += path('M207 42 Q263 9 313 46 Q364 23 392 68 Q361 95 301 79 Q259 91 224 74', SAND, MUTED, 1.3, opacity=.5)
    for xx, yy in ((237, 52), (265, 38), (294, 59), (327, 43), (354, 66), (279, 71)):
        a += ellipse(xx, yy, 3.6, 2.8, MUTED)
    a += arrow([(346, 79), (442, 112)], TERRA, 2, '5 5')

    b = feather(558, 126, 214, SAND, -18) + feather(694, 142, 192, PALE, 11)
    for xx, yy, rx, ry in ((537, 163, 4, 3), (557, 193, 5, 3), (575, 224, 4, 3),
                           (604, 272, 4, 3), (680, 196, 4, 3), (702, 234, 5, 3), (681, 273, 4, 3)):
        b += ellipse(xx, yy, rx, ry, MUTED)
    b += path('M555 199 Q580 182 590 207 Q583 225 562 221Z', GOLD, MUTED, 1, opacity=.65)
    b += path('M679 227 Q703 217 713 238 Q704 249 683 243Z', GOLD, MUTED, 1, opacity=.65)
    b += path('M544 176 q14 5 20 14 M679 258 q10 5 16 12', stroke=MUTED, width=1)
    b += pin(1, 784, 45, 583, 211) + pin(2, 19, 30, 178, 71)

    c = path('M26 378 V202 H272 V378 M20 202 H278', PALE, INK, 1.5)
    c += path('M31 380 H319 M63 390 H277', stroke=LINE, width=1.5)
    c += _adult(111, 376, 139, pose='sweep', shirt=BLUE)
    c += path('M126 293 L157 376 M149 365 l29 -7 l8 23 l-32 5Z', SAND, INK, 1.6)
    for xx in range(157, 180, 5):
        c += line(xx, 366, xx+7, 383, MUTED, 1)
    c += path('M199 377 l15 -11 h37 l-5 13Z', GOLD, INK, 1.3)
    c += line(251, 365, 258, 342, MUTED, 2)
    c += feather(178, 372, 27, SAND, 57) + feather(215, 371, 22, PALE, -58)
    for xx, yy in ((175, 387), (194, 380), (235, 373), (210, 386)):
        c += ellipse(xx, yy, 2.4, 1.8, MUTED)
    c += _filter(226, 220, 56, 109)
    c += path('M282 239 h14 v67 h-14 M280 257 h15 M280 291 h15', stroke=INK, width=1.5)
    c += arrow([(304, 276), (289, 276)], BLUE, 1.5)
    c += pin(3, 20, 142, 191, 376) + pin(4, 324, 168, 251, 274)

    d = path('M422 377 V202 H792 V377 M416 202 H800', SAND, INK, 1.6)
    d += chair(526, 378, 1.05) + _adult(526, 378, 124, pose='sit', shirt=GREEN)
    d += path('M619 377 V261 H658 V377', WHITE, INK, 1.5)
    d += ellipse(638, 286, 13, 13, PALE, INK, 1.2)
    d += path('M638 276 q15 8 0 13 q-15 8 0 -13 M629 312 h17 M629 320 h17', stroke=BLUE, width=1.2)
    d += path('M604 286 Q586 291 579 306 M604 301 Q586 307 580 319', stroke=BLUE, width=1.2)
    d += desk(703, 381, 90) + cup(746, 327, .7)
    d += path('M470 385 h320 M461 396 h340', stroke=LINE, width=1.5)
    d += pin(5, 770, 148, 635, 290)
    return group(26, 16, a+b) + group(26, 340, c+d)


DIAGRAMS = {
    'history': make(
        'history', '文明分期的生活小景', _history(),
        '六分期生活器物与环境的形制示例，不按比例；场景非考古现场真实复刻，分期可交叠，不补地方年表、聚落布局或技术参数。',
        [
            ('巢台与火塘', '距今十万年至一万二千年，巢台休息与遮挡的地面火塘并存，围坐时羽翼避开火源。'),
            ('河谷储粮', '距今一万二千年至六千年，水源、住处与下层粮仓相联系，粮食搬运仍靠地面及水路。'),
            ('信使落点', '距今六千年至两千年，稳定落点、落点账簿与轻件接力支持区域联系，并非一人连续远飞。'),
            ('机械与航图', '距今约两千年至三百年，工坊、航图与铁路等机械连接发展，共同航图协议生效标志共历元年。'),
            ('双网楼与街面', '共历四百年以后，公共电梯、公交、铁路与屋顶平台连接同一城市的生活空间。'),
            ('数字天气生活', '当前资料时点为共历七二八年，掌上天气与平台信息辅助选择，仍不能取消阵风和体力限制。'),
        ],
        question='哪些年代的小景都保留了稳定地面、储粮或机械连接？', height=820),
    'events': make(
        'events', '三次转折的机制小景', _events(),
        '雾中供应、工业治理和等效入口的机制示意与设施形制示例，不按比例；不是事件现场复刻，不补地点、持续天数、伤亡或新事件结果。',
        [
            ('雾中地面供应', '长雾年约距今九百年，粮仓与机械运输说明停飞时的供应支撑，地面运行也仍受天气影响。'),
            ('停飞与稳定等待', '低能见度限制个人飞行，关闭提示与落地等待只例示路线转换，不记述某次具体停飞经过。'),
            ('排气与作业隔离', '炉灰危机约距今二百六十年，排气治理、工厂隔离与公共维护处理不同问题，不表示排放已消失。'),
            ('羽面与维护', '颗粒及油雾附着的放大草图说明受影响对象，公共干羽不能替代污染源治理。'),
            ('屋顶与地面入口', '共历六百一十四年的双入口公约强调主要城市公共建筑同时具备屋顶便利与可靠地面到达。'),
            ('同一服务', '两条示意线都到同一柜台，不把通行方式画成身份等级，也不规定公共建筑统一形制。'),
        ],
        question='三处小景里，粮仓、排气设施和电梯分别解决什么连接问题？', height=1060),
    'governance': make(
        'governance', '维护、通行与私人边界', _governance(),
        '窗口、维护者、居民及同一服务的形制示例与关系示意，不按比例；少量关联线不表示管理机构、处罚制度、统一隐私距离或工程标准。',
        [
            ('窗口与居住', '近窗空间不是公共道路，私人屋顶与住宅界面保有进入、拍摄和停落边界。'),
            ('通行与避让', '移动中的成人远离窗口并有平台作为到达方向，虚线不规定实际航路、航层或距离。'),
            ('维护与状态判断', '维护者查看实物标识与记录，平台维护不能代替居民对身体、负重和天气的判断。'),
            ('等效到达', '屋顶入口和地面入口通过内部连接到同一服务，公共可达性不以个人能飞为条件。'),
            ('有限运行信息', '终端仅例示天气与平台状态，运行信息不自动等于永久保存全部个人飞行轨迹。'),
        ],
        question='窗口、平台标识和共同柜台各自对应哪一种使用边界？', height=770),
    'culture': make(
        'culture', '站位表演、移动舞与器物', _culture(),
        '表演场地、移动瞬间和文化器物的形制示例与机制示意，不按比例；不规定曲目、声部等级、平台高度、声学参数、工艺纹样或文学作品。',
        [
            ('较高平台合唱', '合唱者双脚站在平台上，高度组织空间声部而不表示参与者价值。'),
            ('较低平台合唱', '另一组合唱者同样有稳定站位，并不需要悬停唱完整场。'),
            ('地面观众', '观众在地面座椅上观看和收听，机械连接使公共活动不只向飞行者开放。'),
            ('舞者与落点', '舞者只画移动中的一个瞬间，虚线接向空置落点，不表示持续悬停或完整安全编排。'),
            ('羽纹材料局部', '自然脱落羽片与纺织小样只示例工艺材料，来源、卫生与品质仍限制回收。'),
            ('风记器物局部', '书册与书写用具作为旅程表达的器物示例，墨线不新增文字系统或文学内容。'),
        ],
        question='合唱者、舞者和观众各自在哪里获得稳定支撑？', height=820),
    'etiquette': make(
        'etiquette', '折翼让路与背羽照护', _etiquette(),
        '两处成年人动作的形制示例与关系示意，不按比例；整羽场景以此前已征得同意为前提，不规定统一手势、交谈距离、地方礼仪或照护技术。',
        [
            ('折翼侧让', '站立者收拢双翼并退到通行侧边，为门内来人留下步行空间。'),
            ('步行通过', '另一成人收翼穿过门口，地面虚线仅说明让行方向而不是对白或通行标准。'),
            ('同意后协助', '右侧只例示已征得同意后的背羽整理，不以画中姿势替代同意，也不把协助限定为伴侣关系。'),
            ('整理不是治疗', '羽片与软布局部强调维护对象，整理不能使断裂羽轴即时恢复，也不构成医疗操作教程。'),
        ],
        question='收翼后的空隙与照护者独立的双手，分别说明了什么？', height=710),
    'festivals': make(
        'festivals', '归台夜与静翼日的共同参与', _festivals(),
        '温和平台灯、双入口与地面相聚的形制示例，不按比例；两节并置不表示同日或相邻流程，不新增日期、周期、节目、地方仪式或照明标准。',
        [
            ('归台夜温和标识', '小型遮挡灯具只例示平台温和标识，不用炫光，也不意味着夜间和坏天气必然适飞。'),
            ('两入口共用活动', '地面入口与屋顶入口经同一建筑连接到共同活动空间，不把两类来访者分为主次。'),
            ('静翼日地面相聚', '居民收翼落座、休息与相聚，静翼不是失去参与资格或飞行失败。'),
            ('阅读与恢复', '书册和补水器物只说明安静活动与休息，不规定节庆食物、统一恢复时长或固定流程。'),
        ],
        question='不飞行的来访者怎样进入同一活动，静翼时又能参加什么？', height=880),
    'memorial': make(
        'memorial', '保存羽片、信件与记忆册', _memorial(),
        '四类纪念静物的形制示例，不按比例；并置不是统一纪念套装或葬礼结构，不补地方文字、姓名、信件内容、真实航程或安置仪式。',
        [
            ('自然脱落羽片', '羽片来自自然脱落后的保存，不示例拔羽，部分家庭也可只保存其他记录。'),
            ('手写信', '纸张、信封与墨线表示手写记录，笔迹不是可辨识的地方文字或新增信件内容。'),
            ('航程卡', '卡片可承载独立落地等成长记忆，图中分栏只为纸面形制示例，不提供实际日期与路线。'),
            ('记忆册', '册页可保存羽片及经历，不据此推定所有家庭或地方有相同悼念方式。'),
        ],
        question='哪些物件保存材料，哪些物件保存记录，它们必须同时出现吗？', height=620),
    'pollution': make(
        'pollution', '羽面附着与环境维护分工', _pollution(),
        '颗粒、油雾羽面草图及设施的形制示例与因果机制示意，不按比例；箭头不是技术流程或治理达标证明，不补化学浓度、微观结构、诊断方法或工程参数。',
        [
            ('附着羽面草图', '放大的颗粒点和油雾色斑说明可见附着对象，不按真实颗粒尺度，也不能据羽色或图形诊断原因。'),
            ('源头排气治理', '排气收集设施与作业隔离处理生产环境问题，不因安装设备便推定排放已消除。'),
            ('落羽清扫', '地面清扫收集落羽及沉落物，不把公共地面当作废弃层，也不宣称能去除全部羽面污染。'),
            ('过滤与耗材', '独立过滤装置处理相关空气负担并需要维护，形制草稿不表示过滤等级或技术标准。'),
            ('干羽与恢复', '通风干羽支持湿羽维护及稳定休息，不能替代清洁、污染源治理或异常时的专业调查。'),
        ],
        question='排气治理、地面清扫、过滤和干羽为什么不能互相替代？', height=820),
}
