"""生活百科线描淡彩插图；所有具体器物和空间均为示例形制。"""

import math

if __package__:
    from . import common as c
else:
    import common as c


INK, MUTED, PAPER = c.INK, c.MUTED, c.PAPER
WHITE, GREEN, TERRA = c.WHITE, c.GREEN, c.TERRA
GOLD, BLUE, PALE, SAND, LINE = c.GOLD, c.BLUE, c.PALE, c.SAND, c.LINE
SKIN = '#E9C6A4'


def _person(x, y, h=140, pose='stand', color=GREEN, opened=False,
            back=False, bound=False, elder=False, helmet=False, facing=1):
    """衣着完整；翼、袖与手、裤与鞋分别绘制，不把手臂当翼。"""
    b = c.group(0, -12, c.wing(opened, SAND, -1) + c.wing(opened, SAND, 1))
    if bound:
        for side in (-1, 1):
            b += c.path(f'M{side * 15} -75 Q{side * 31} -83 {side * 43} -66 '
                        f'L{side * 40} -60 Q{side * 26} -71 {side * 15} -68Z', TERRA, INK, 1.2)
    b += c.path('M-16 -98 Q0 -108 16 -98 L20 -53 Q0 -46 -20 -53Z', color)
    if back:
        b += c.path('M-9 -100 Q0 -95 9 -100 M-17 -91 Q-24 -79 -15 -62 M17 -91 Q24 -79 15 -62', stroke=MUTED, width=1)
    else:
        b += c.path('M-9 -100 L0 -89 L9 -100 M0 -88 V-53 M-12 -68 h8 v10 h-8Z', stroke=MUTED, width=1)
    b += c.ellipse(0, -121, 14, 17, SKIN, INK, 1.5)
    hair = '#A5A49C' if elder else MUTED
    b += c.path('M-14 -122 Q-16 -145 5 -140 Q18 -136 14 -119 '
                'L9 -127 Q-1 -131 -11 -122Z', hair, INK, 1)
    if not back:
        b += c.path('M3 -119 h3 M8 -113 l3 2 M3 -106 q4 2 8 -1', stroke=INK, width=.9)
    else:
        b += c.path('M-6 -104 Q0 -101 6 -104', stroke=MUTED, width=1)
    if helmet:
        b += c.path('M-18 -129 Q-17 -151 3 -150 Q22 -148 20 -130Z', GOLD, INK, 1.5)
        b += c.path('M-21 -129 h44 M0 -148 v14', stroke=INK, width=1.3)
    if pose == 'sit':
        legs = ['M-16 -53 L-17 -34 L15 -31 L18 -6 L29 -6 L29 -42 L2 -50Z',
                'M2 -53 L7 -42 L35 -38 L38 -6 L49 -6 L49 -49 L19 -55Z']
        shoes = ['M17 -7 h13 l8 7 H16Z', 'M37 -7 h13 l8 7 H36Z']
    elif pose in ('walk', 'run'):
        legs = ['M-16 -53 L-21 -29 L-37 -7 L-28 -2 L-7 -29 L1 -50Z',
                'M1 -53 L24 -36 L39 -17 L48 -23 L28 -47 L17 -55Z']
        shoes = ['M-37 -8 l12 6 l-2 7 h-19Z', 'M38 -19 l10 -6 l13 6 l-16 7Z']
    elif pose in ('fly', 'land'):
        legs = ['M-16 -53 Q-26 -26 -18 -8 L-8 -9 Q-17 -28 1 -50Z',
                'M1 -53 L25 -35 L35 -19 L44 -25 L30 -47 L17 -55Z']
        shoes = ['M-19 -10 h12 l9 8 h-21Z', 'M34 -21 l10 -7 l14 7 l-16 7Z']
    elif pose == 'crouch':
        legs = ['M-16 -53 L-27 -30 L-13 -12 L-35 -9 L-35 0 H1 L0 -16 L-12 -32 L3 -49Z',
                'M3 -53 L32 -33 L37 -7 L49 -7 L47 -41 L20 -57Z']
        shoes = ['M-36 -9 h24 l5 9 h-31Z', 'M36 -8 h14 l9 8 H35Z']
    else:
        legs = ['M-17 -53 L-17 -7 L-5 -7 L1 -50Z',
                'M1 -52 L7 -7 L19 -7 L18 -54Z']
        shoes = ['M-17 -8 h13 l1 8 h-25 l2 -5Z', 'M7 -8 h13 l10 5 v3 H6Z']
    for shape in legs:
        b += c.path(shape, BLUE, INK, 1.6)
    for shape in shoes:
        b += c.path(shape, MUTED, INK, 1.3)
    arms = {
        'stand': [(-15, -95, -29, -73, -27, -51), (15, -95, 30, -73, 28, -52)],
        'walk': [(-15, -95, -33, -80, -44, -93), (15, -95, 30, -76, 43, -72)],
        'run': [(-15, -95, -32, -81, -43, -95), (15, -95, 30, -78, 42, -84)],
        'fly': [(-15, -95, -32, -88, -48, -76), (15, -95, 33, -85, 48, -88)],
        'land': [(-15, -95, -34, -88, -47, -79), (15, -95, 33, -86, 49, -78)],
        'sit': [(-15, -95, -26, -74, 5, -62), (15, -95, 34, -77, 37, -58)],
        'operate': [(-15, -95, -30, -74, 11, -73), (15, -95, 35, -80, 52, -84)],
        'point': [(-15, -95, -30, -74, -29, -55), (15, -95, 39, -99, 61, -110)],
        'groom': [(-15, -95, -31, -76, -20, -53), (15, -95, 43, -101, 56, -84)],
        'crouch': [(-15, -95, -30, -70, -10, -39), (15, -95, 36, -68, 53, -48)],
    }[pose]
    for ax, ay, ex, ey, hx, hy in arms:
        b += c.path(f'M{ax} {ay} L{ex} {ey} L{hx} {hy}', stroke=INK, width=12)
        b += c.path(f'M{ax} {ay} L{ex} {ey} L{hx} {hy}', stroke=color, width=9)
        b += c.ellipse(hx, hy, 4, 5, SKIN, INK, .9)
        b += c.path(f'M{hx - 1} {hy - 2} l3 3', stroke=MUTED, width=.7)
    b += c.path('M-17 -52 Q0 -48 18 -53', stroke=INK, width=1.5)
    return c.group(x, y, f'<g transform="scale({facing} 1)">{b}</g>', h / 140)


def _chair(x, y, scale=1):
    """两侧背板之间是真实留空，不以印在椅背上的线充当翼槽。"""
    b = c.path('M-69 -123 Q-57 -139 -44 -130 L-43 -57 L-63 -54Z', SAND)
    b += c.path('M44 -130 Q57 -139 69 -123 L64 -54 L43 -57Z', SAND)
    b += c.path('M-62 -116 L-49 -120 M49 -120 L62 -116 '
                'M-60 -86 L-48 -89 M48 -89 L60 -86', stroke=MUTED, width=1)
    b += c.path('M-64 -54 L57 -54 L73 -42 L-48 -39Z', TERRA)
    b += c.path('M-48 -39 H73 V-30 H-48Z', GOLD, INK, 1.3)
    b += c.path('M-57 -51 L-59 -9 M57 -50 L63 -8 M-43 -30 L-40 0 M67 -30 L71 0',
                stroke=INK, width=3)
    b += c.path('M-63 -55 L-69 -75 L-46 -75 M62 -55 L68 -75 L45 -75',
                stroke=INK, width=2.5)
    return c.group(x, y, b, scale)


def _pallet(x, y, scale=1, loaded=True):
    b = c.path('M0 -8 L88 -8 L112 -22 L24 -22Z', GOLD)
    b += c.path('M0 -8 V0 H88 L112 -14 V-22 M88 -8 V0', stroke=INK, width=1.5)
    for xx in (9, 37, 69):
        b += c.rect(xx, -5, 12, 5, MUTED, INK, 0, .7)
    for xx in (15, 40, 65):
        b += c.line(xx, -9, xx + 23, -21, MUTED, .9)
    if loaded:
        for xx, yy, ww, hh in ((6, -61, 42, 44), (49, -69, 37, 52), (28, -103, 49, 33)):
            b += c.crate(xx, yy, ww, hh)
            b += c.path(f'M{xx} {yy} l18 -10 h{ww} l-18 10 '
                        f'M{xx + ww} {yy} l18 -10 v{hh} l-18 10', SAND, INK, 1.2)
        b += c.path('M23 -105 V-22 M66 -106 V-24', stroke=BLUE, width=2)
    return c.group(x, y, b, scale)


def _pallet_jack(x, y, scale=1):
    b = c.path('M0 -8 L69 -8 L89 -18 M12 -2 L77 -2 L95 -12', stroke=INK, width=4)
    b += c.path('M-4 -14 L-10 -71 Q-12 -82 -24 -79 H-36', stroke=INK, width=4)
    b += c.path('M-9 -14 L9 -14 L17 -1 H-13Z', TERRA)
    b += c.ellipse(-6, 0, 7, 7, MUTED, INK, 1)
    b += c.ellipse(75, -1, 4, 4, MUTED, INK, 1)
    return c.group(x, y, b, scale)


def _freight_truck(x, y, scale=1):
    b = c.path('M0 -110 L204 -110 L235 -132 L31 -132Z', SAND)
    b += c.path('M0 -110 H204 V-20 H0Z', SAND)
    b += c.path('M204 -110 L235 -132 V-42 L204 -20Z', GOLD)
    b += c.path('M205 -89 H255 L282 -61 V-19 H205Z', TERRA)
    b += c.path('M217 -82 H251 L269 -62 H217Z', PALE, INK, 1.3)
    b += c.path('M216 -54 H270 M217 -43 h14 M3 -27 h276', stroke=INK, width=1.4)
    for xx in (18, 43, 68, 93, 118, 143, 168, 191):
        b += c.line(xx, -105, xx, -33, LINE, 1)
    for xx in (36, 165, 251):
        b += c.ellipse(xx, -15, 17, 17, MUTED, INK, 1.5)
        b += c.ellipse(xx, -15, 7, 7, WHITE, INK, 1)
    return c.group(x, y, b, scale)


def _lift(x, y, w=130, h=220, freight=False):
    b = c.rect(x, y, w, h, '#F1EDE5', INK, 0, 2.5)
    b += c.path(f'M{x + 10} {y + 10} V{y + h - 9} M{x + w - 10} {y + 10} V{y + h - 9}',
                stroke=MUTED, width=2)
    b += c.ellipse(x + w / 2, y + 19, 11, 11, SAND, INK, 1.4)
    b += c.path(f'M{x + w / 2 - 4} {y + 9} V{y + 52} '
                f'M{x + w / 2 + 4} {y + 9} V{y + 52}', stroke=INK, width=1)
    b += c.rect(x + 15, y + 52, w - 30, h - 69, WHITE, INK, 0, 1.8)
    b += c.path(f'M{x + 15} {y + h - 17} h{w - 30} l10 8 h{-w + 10}Z', SAND, INK, 1)
    if freight:
        b += _pallet(x + 24, y + h - 25, (w - 49) / 112)
    else:
        b += _person(x + w / 2, y + h - 20, min(h - 82, 130), back=True)
    b += c.rect(x + w + 7, y + h - 80, 13, 38, WHITE, INK, 1, 1)
    b += c.ellipse(x + w + 13, y + h - 69, 2, 2, BLUE)
    b += c.ellipse(x + w + 13, y + h - 54, 2, 2, GOLD)
    return b


def _bowl(x, y, scale=1, contents=True):
    b = c.path('M-43 -17 Q-37 20 0 22 Q36 20 43 -17Z', WHITE, INK, 1.6)
    b += c.ellipse(0, -17, 43, 13, SAND, INK, 1.4)
    if contents:
        for i in range(18):
            xx = -29 + (i * 17) % 59
            yy = -24 + (i * 7) % 15
            b += c.ellipse(xx, yy, 3, 1.7, GOLD, MUTED, .5)
    b += c.path('M-29 1 Q0 16 29 1', stroke=LINE, width=1)
    return c.group(x, y, b, scale)


def _meal(x, y, scale=1, return_meal=False):
    b = c.ellipse(0, 11, 87, 27, PALE, 'none')
    b += _bowl(-25, 0, .9)
    b += c.cup(54, -4, 1.05)
    b += c.path('M-84 -6 Q-70 -39 -47 -29 Q-33 -20 -48 -8 Q-64 4 -84 -6Z', GOLD, INK, 1.3)
    b += c.path('M-70 -24 l-7 11 M-59 -28 l-8 13', stroke=MUTED, width=1)
    b += c.path('M11 0 Q11 -18 26 -22 Q44 -10 35 7 Q20 15 11 0Z', TERRA, INK, 1.3)
    b += c.path('M25 -22 q-2 -9 6 -11', stroke=GREEN, width=2)
    b += c.path('M-66 25 H47 M-63 29 H49', stroke=INK, width=1.3)
    if return_meal:
        b += c.path('M72 -26 L75 -70 Q87 -83 99 -70 L102 -26Z', WHITE, INK, 1.5)
        b += c.path('M77 -52 H97 V-28 H77Z', PALE, BLUE, 1)
        b += c.rect(81, -79, 12, 7, BLUE, INK, 1, 1)
    return c.group(x, y, b, scale)


def _fan(x, y, scale=1):
    b = c.path('M-23 0 H25 M0 -3 V-36', stroke=INK, width=3)
    b += c.ellipse(0, -64, 29, 29, WHITE, INK, 1.8)
    for a in (0, 120, 240):
        b += c.group(0, -64, c.path('M0 0 Q-8 -17 8 -23 Q22 -14 8 2Z', PALE, BLUE, 1), rotate=a)
    b += c.ellipse(0, -64, 5, 5, SAND, INK, 1)
    b += c.ellipse(0, -64, 22, 22, 'none', LINE, 1)
    b += c.path('M-27 -64 H27 M0 -91 V-37 M-19 -83 L19 -45 M19 -83 L-19 -45',
                stroke=LINE, width=.8)
    b += c.path('M18 -9 Q47 -9 43 0 H66', stroke=MUTED, width=1.5)
    b += c.path('M65 -4 v8 M69 -4 v8', stroke=INK, width=1.8)
    return c.group(x, y, b, scale)


def _terminal(x, y, scale=1):
    b = c.rect(-29, -94, 58, 94, MUTED, INK, 6, 1.5)
    b += c.rect(-23, -85, 46, 66, PALE, INK, 2, 1)
    b += c.cloud(-9, -70, 22)
    b += c.path('M-16 -48 h31 M-16 -39 h21 M-16 -30 h14', stroke=BLUE, width=2)
    b += c.path('M9 -72 l4 5 l7 -10', stroke=GREEN, width=2)
    b += c.ellipse(0, -9, 4, 4, WHITE, INK, .8)
    return c.group(x, y, b, scale)


def _coat(x, y, scale=1, back=False, opened=False):
    b = c.path('M-22 -123 L-47 -109 L-75 -47 L-50 -37 L-32 -81 '
                'L-35 0 H35 L32 -81 L50 -37 L75 -47 L47 -109 L22 -123Z', GREEN)
    b += c.path('M-22 -123 Q0 -109 22 -123 M-50 -39 l-21 -8 M50 -39 l21 -8 '
                'M-33 -7 H33', stroke=MUTED, width=1.2)
    if back:
        b += c.path('M0 -112 V-7 M-20 -110 Q-38 -84 -24 -61 '
                    'M20 -110 Q38 -84 24 -61', stroke=INK, width=1.5)
        for side in (-1, 1):
            b += c.path(f'M{side * 21} -108 Q{side * 42} -95 {side * 24} -65 '
                        f'Q{side * 12} -84 {side * 21} -108Z', SAND, INK, 1.3)
            if opened:
                b += c.path(f'M{side * 24} -107 L{side * 49} -98 '
                            f'L{side * 37} -58 L{side * 23} -65Z', PALE, INK, 1.2)
    else:
        b += c.path('M-17 -120 L0 -97 L17 -120 M0 -96 V0 '
                    'M-25 -57 h17 v19 h-17 M9 -57 h17 v19 H9Z', stroke=INK, width=1.2)
        for yy in (-81, -60, -39, -18):
            b += c.ellipse(3, yy, 1.8, 1.8, GOLD, INK, .7)
    return c.group(x, y, b, scale)


def _bicycle(x, y, scale=1):
    b = ''
    for xx in (-84, 87):
        b += c.ellipse(xx, -38, 38, 38, 'none', INK, 3)
        b += c.ellipse(xx, -38, 32, 32, 'none', LINE, 1)
        for a in range(0, 360, 45):
            b += c.line(xx, -38, xx + 32 * math.cos(math.radians(a)),
                        -38 + 32 * math.sin(math.radians(a)), MUTED, .7)
    b += c.path('M-84 -38 L-44 -72 L-10 -36 L45 -74 L87 -38 '
                'M-44 -72 L-24 -80 M-10 -36 L-69 -36 L-44 -72 '
                'M-10 -36 L41 -39 L45 -74', stroke=GREEN, width=5)
    b += c.path('M-29 -80 h-24 M45 -74 L40 -99 H60 M-41 -73 L-35 -105 '
                'M-50 -105 h33', stroke=INK, width=3)
    b += c.ellipse(-10, -36, 9, 9, WHITE, INK, 1.5)
    b += c.path('M-10 -36 l13 12 h13 M-10 -36 l-13 -11 h-10', stroke=INK, width=2)
    b += c.path('M-77 -54 Q-87 -66 -102 -56 M71 -62 Q95 -70 115 -54 '
                'M-12 -25 H39', stroke=MUTED, width=1.5)
    b += c.path('M-24 -31 l-8 29', stroke=INK, width=2)
    return c.group(x, y, b, scale)


def _shoe(x, y, scale=1):
    b = c.path('M-60 -34 L-23 -51 L1 -32 Q20 -21 47 -19 Q64 -13 65 0 '
                'H-61 Q-70 -18 -60 -34Z', SAND)
    b += c.path('M-63 -4 Q0 5 64 -3 L66 6 H-64Z', MUTED, INK, 1.3)
    b += c.path('M-46 -31 L-20 -41 L6 -23 M-19 -33 l16 -7 M-11 -27 l15 -6 '
                'M-3 -21 l15 -5 M-53 -17 h22 M27 -17 q12 -8 23 0', stroke=INK, width=1.2)
    for xx in (-51, -29, -7, 16, 40, 57):
        b += c.line(xx, 1, xx - 3, 5, GOLD, 1)
    return c.group(x, y, b, scale)


def _ladder(x, y, scale=1):
    b = c.path('M-56 0 L-25 -166 H10 L50 0 M-25 -166 L-4 0 '
                'M10 -166 L44 -3', stroke=INK, width=4)
    for i in range(6):
        yy = -22 - i * 23
        left = -52 + i * 4
        right = -6 - i * 3
        b += c.path(f'M{left} {yy} H{right} l8 -5 H{left + 8}Z', SAND, INK, 1.1)
    b += c.path('M-39 -74 H29 M-40 -70 H30 M-58 0 h16 M-10 0 h16 M41 0 h16',
                stroke=MUTED, width=3)
    b += c.path('M-23 -164 H10 V-156 H-25Z', GOLD, INK, 1.5)
    return c.group(x, y, b, scale)


def _net(x, y, w=190, h=110):
    b = c.path(f'M{x} {y + h + 12} V{y - 18} M{x + w} {y + h + 12} V{y - 18}',
               stroke=INK, width=3)
    b += c.path(f'M{x} {y} Q{x + w / 2} {y + 10} {x + w} {y} '
                f'L{x + w} {y + h} Q{x + w / 2} {y + h - 7} {x} {y + h}Z', PALE, GREEN, 2)
    for xx in range(12, int(w), 15):
        b += c.path(f'M{x + xx} {y + 4} V{y + h - 4}', stroke=GREEN, width=.8)
    for yy in range(14, int(h), 15):
        b += c.path(f'M{x + 2} {y + yy} Q{x + w / 2} {y + yy + 5} '
                    f'{x + w - 2} {y + yy}', stroke=GREEN, width=.8)
    b += c.path(f'M{x} {y} Q{x + w / 2} {y + 10} {x + w} {y}', stroke=TERRA, width=5)
    for xx in range(13, int(w), 35):
        b += c.path(f'M{x + xx} {y + 4} l5 19 l9 -5 l-5 -16Z', GOLD, INK, .7)
    return b


def _window(x, y, w, h):
    return (c.rect(x, y, w, h, '#EDF1EC', INK, 0, 1.5)
            + c.path(f'M{x + w / 2} {y} V{y + h} M{x} {y + h / 2} H{x + w}',
                     stroke=LINE, width=2)
            + c.path(f'M{x - 5} {y + h} h{w + 10} l8 5 h{-w - 10}Z', SAND, INK, 1))


def _sack(x, y, scale=1):
    b = c.path('M-24 -82 Q0 -89 24 -82 L18 -68 Q44 -32 31 -4 '
                'Q0 11 -31 -4 Q-43 -32 -18 -68Z', SAND)
    b += c.path('M-22 -73 Q0 -66 22 -73 M-20 -79 Q0 -74 20 -79 '
                'M-22 -42 q-6 20 3 32 M21 -52 q8 22 4 37', stroke=MUTED, width=1)
    b += c.path('M-5 -39 q-9 -10 -4 -15 q11 2 9 12 q11 -10 15 -2 '
                'q-6 11 -15 8 v17', stroke=GREEN, width=1.5)
    return c.group(x, y, b, scale)


def _railcar(x, y, scale=1, passenger=False):
    b = c.path('M0 -104 Q0 -117 17 -117 H248 Q267 -116 267 -96 '
                'V-19 H0Z', PALE if passenger else SAND)
    if passenger:
        for xx in (15, 67, 119, 171):
            b += c.rect(xx, -99, 40, 38, WHITE, INK, 3, 1.3)
            b += c.line(xx, -75, xx + 40, -75, LINE, 1)
        b += c.rect(226, -99, 30, 78, WHITE, INK, 1, 1.3)
        b += c.rect(232, -93, 18, 33, PALE, INK, 1, 1)
        b += c.line(3, -43, 218, -43, BLUE, 3)
    else:
        for xx in range(13, 258, 22):
            b += c.line(xx, -106, xx, -31, MUTED, .8)
        b += c.rect(101, -106, 66, 83, GOLD, INK, 0, 1.2)
        b += c.path('M134 -105 V-24 M119 -63 h8 M140 -63 h8', stroke=INK, width=1.2)
    for xx in (36, 68, 199, 231):
        b += c.ellipse(xx, -13, 12, 12, MUTED, INK, 1)
        b += c.ellipse(xx, -13, 4, 4, WHITE, INK, .8)
    b += c.path('M-10 -24 H0 M267 -24 h12 M-12 2 H281 M-12 8 H281', stroke=INK, width=2)
    for xx in range(-8, 280, 22):
        b += c.line(xx, 4, xx + 5, 12, GOLD, 3)
    return c.group(x, y, b, scale)


def _stretcher(x, y, scale=1, patient=True):
    b = c.path('M-81 -52 H66 L83 -41 H-64Z', SAND)
    b += c.path('M-64 -41 H83 V-34 H-64 M-79 -54 h160', stroke=INK, width=2.2)
    if patient:
        b += c.ellipse(-56, -67, 12, 11, SKIN, INK, 1.3)
        b += c.path('M-45 -75 Q-18 -84 18 -71 L65 -57 V-46 H-46Z', PALE)
        b += c.path('M-34 -65 Q0 -59 40 -59 M-35 -75 Q-8 -82 17 -69', stroke=GREEN, width=1)
        b += c.path('M-67 -72 Q-59 -84 -47 -74', MUTED, INK, 1)
    b += c.path('M-51 -35 L52 -11 M65 -35 L-40 -11 M-44 -10 H58', stroke=INK, width=3)
    for xx in (-43, 56):
        b += c.ellipse(xx, -5, 8, 8, MUTED, INK, 1)
        b += c.ellipse(xx, -5, 3, 3, WHITE)
    b += c.path('M-65 -39 V-63 H-43 M64 -37 V-57 H79', stroke=BLUE, width=2)
    return c.group(x, y, b, scale)


def _vehicle(x, y, scale=1):
    b = c.path('M-131 -114 Q-128 -125 -112 -125 H76 L125 -85 '
                'V-19 H-131Z', WHITE)
    b += c.path('M69 -115 L112 -83 H69Z', PALE, INK, 1.3)
    b += c.rect(-115, -111, 47, 36, PALE, INK, 2, 1.3)
    b += c.rect(-55, -110, 57, 78, '#F2F2EB', INK, 1, 1.3)
    b += c.path('M-27 -108 V-34 M-40 -68 h6 M-18 -68 h6 M15 -31 V-107 '
                'M22 -65 h19 M-125 -45 H120', stroke=BLUE, width=2)
    b += c.path('M-112 -127 h27 v-7 h-27Z', GOLD, INK, 1)
    for xx in (-83, 81):
        b += c.ellipse(xx, -15, 18, 18, MUTED, INK, 1.5)
        b += c.ellipse(xx, -15, 7, 7, WHITE, INK, 1)
    return c.group(x, y, b, scale)


def _pins(items):
    return ''.join(c.pin(i + 1, *point) for i, point in enumerate(items))


def _figure(key, title, body, notes, pins, question, scope, height=650):
    assert len(notes) == len(pins) and 2 <= len(notes) <= 6
    caption = f'形制示例，示意不按比例；{scope}。具体结构、摆放与人物外观不是固定设定。'
    return c.make(key, title, body + _pins(pins), caption, notes, question, height)


def _logistics():
    b = c.path('M395 267 H860 L881 286 H395Z', SAND)
    b += c.path('M455 327 H860 L881 344 H455Z', SAND, INK, 1.5)
    b += c.path('M455 267 V139 M859 267 V143 M456 139 H859', stroke=INK, width=3)
    b += _window(683, 157, 76, 60)
    b += c.rect(480, 176, 111, 91, PALE, INK, 1, 2)
    for yy in (180, 218):
        for xx in (485, 522, 558):
            b += c.rect(xx, yy, 29, 33, WHITE, INK, 1, 1)
            b += c.line(xx + 22, yy + 13, xx + 22, yy + 20, MUTED, 1)
    b += c.path('M522 218 L546 218 L546 251 L522 251 L505 241 V210Z', SAND, INK, 1.3)
    b += _person(442, 266, 116, 'operate')
    b += c.parcel(462, 189, 20)
    b += _person(163, 190, 112, 'fly', opened=True)
    b += c.path('M146 111 L139 135 L154 137 L158 112Z', GREEN, INK, 1.2)
    b += c.curve_arrow('M248 111 Q324 97 381 190', (381, 190), 1.1, BLUE, 2.5)
    b += c.arrow([(585, 244), (627, 244), (627, 327), (751, 327)], BLUE, 2.3)
    b += c.rect(457, 344, 315, 220, '#F1EDE5', INK, 0, 2)
    b += c.path('M458 345 l34 -27 H772 V344 M493 344 V563 M458 563 H881 '
                'M457 389 H573 M457 437 H573', stroke=INK, width=2)
    for xx in (461, 513):
        for yy in (361, 409):
            b += c.crate(xx, yy, 45, 26)
    b += _lift(614, 349, 146, 212, freight=True)
    b += c.path('M614 349 V272 M760 349 V272 M615 294 H760', stroke=MUTED, width=2)
    b += c.rect(771, 281, 88, 41, WHITE, INK, 1, 1.5)
    b += c.parcel(784, 280, 20)
    b += c.crate(823, 274, 30, 25)
    b += _freight_truck(48, 560, .94)
    b += _pallet(374, 553, .82)
    b += _pallet_jack(367, 557, .8)
    b += _person(353, 557, 120, 'operate', color=TERRA)
    b += c.arrow([(325, 593), (459, 593), (568, 593), (568, 538)], BLUE, 2.5)
    b += c.arrow([(780, 449), (780, 331), (820, 331)], BLUE, 2.3)
    b += c.ground(29, 566, 844)
    return _figure('logistics', '轻件与箱货：两条链路进入同一交付处', b,
                   [('轻包裹交柜', '轻件随短程飞行到达后落地交柜，不在空中等待交接。'),
                    ('箱货与托盘', '成批箱货占据真实装载空间，由货车和地面搬运设备承担。'),
                    ('仓库与货梯', '仓库接到地面货运，货梯轿厢沿井道把物资送到楼层。'),
                    ('同一交付处', '小件与批量物资经各自链路抵达交付处，人的飞行不代替重货运输。')],
                   [(315, 184, 474, 198), (152, 371, 181, 464),
                    (822, 494, 696, 493), (823, 85, 811, 293)],
                   '比较包裹、人的手、托盘和货车：哪些东西能随人携带，哪些必须沿地面和货梯移动？',
                   '上下链路是功能对照，不表示固定物流布局、载重量或运量', 650)


def _energy():
    b = c.desk(51, 271, 202) + _meal(148, 215, .9)
    b += _person(410, 267, 132, 'run', color=TERRA)
    b += c.ground(294, 273, 208)
    b += _person(681, 240, 136, 'fly', opened=True)
    b += c.path('M563 273 H832 M572 280 h36 M770 281 h48', stroke=LINE, width=1.5)
    b += c.arrow([(252, 202), (326, 202)], TERRA, 3)
    b += c.arrow([(492, 187), (565, 163)], TERRA, 3)
    b += c.path('M52 316 Q436 327 845 316', stroke=LINE, width=1.5)
    b += c.rect(65, 421, 104, 155, SAND, INK, 3, 2)
    b += c.rect(78, 438, 79, 56, WHITE, INK, 1, 1)
    b += c.ellipse(117, 466, 16, 16, PALE, INK, 1.1)
    b += c.path('M105 468 l11 -10 l11 10 M117 459 v18 M77 516 h78 M78 536 h77 '
                'M88 568 v18 M144 568 v18', stroke=INK, width=1.5)
    b += c.path('M168 519 H220 M220 392 V588 M220 392 H299 '
                'M220 497 H564 M220 588 H755', stroke=BLUE, width=2)
    b += c.arrow([(261, 392), (305, 392)], BLUE, 2.6)
    b += c.arrow([(520, 497), (562, 497)], BLUE, 2.6)
    b += c.arrow([(706, 588), (758, 588)], BLUE, 2.6)
    b += _lift(308, 356, 128, 251)
    b += c.arrow([(454, 565), (454, 402)], BLUE, 2)
    b += _chair(607, 597, .6)
    b += _person(599, 597, 91, 'sit', back=True)
    b += _fan(516, 587, .95)
    for yy in (511, 531, 551):
        b += c.path(f'M550 {yy} q19 -8 35 0', stroke=BLUE, width=1.1)
    b += _terminal(785, 539, 1.08)
    b += c.path('M773 541 v38 h-18 M796 541 v23 h17', stroke=MUTED, width=1.4)
    return _figure('energy', '供能分两路：餐食支持身体，电力运行设备', b,
                   [('餐食输入', '食物经身体利用，支持包括步行和飞行在内的肌肉活动。'),
                    ('身体活动', '助跑和拍翼需要能量，图中的活动不是发电端点。'),
                    ('设施供电', '电力沿单向用途线供给电梯、低温通风干羽和导航设备。'),
                    ('不同消耗端', '设备从供电获得运行能量，电梯上升后再滑降不会创造额外能源。')],
                   [(89, 99, 132, 206), (436, 73, 412, 180),
                    (73, 364, 116, 466), (711, 386, 784, 467)],
                   '沿两种颜色的箭头找到真实端点：哪里是身体活动，哪里是用电设备？有没有箭头返回能源来源？',
                   '供电柜仅代表外来供电，不规定发电方式、线路配置、功率或食谱', 660)


def _housing():
    b = c.path('M52 371 L212 273 H598 L727 353 L545 469 H184Z', '#EFE9DF')
    b += c.path('M52 371 V155 L212 65 V273 M212 65 H598 V273 '
                'M598 65 L727 145 V353 M52 155 L212 65', stroke=INK, width=3)
    b += c.path('M55 153 L214 64 H599 L730 144', stroke=GOLD, width=7)
    b += _window(251, 106, 93, 89)
    b += c.path('M75 270 V202 L140 165 V307 M75 202 l-34 -11 V311 L75 334 '
                'M47 251 l17 -8', SAND, INK, 1.5)
    b += c.ellipse(163, 352, 64, 29, PALE, GREEN, 1.1)
    b += c.curve_arrow('M111 356 Q143 324 187 339 Q218 353 197 373', (197, 373), 2.7,
                       BLUE, 2, '5 5')
    b += _person(159, 355, 94, 'walk')
    b += c.path('M73 357 L92 346 L111 357 L94 367Z', TERRA, INK, 1)
    b += _shoe(92, 348, .24)
    b += _chair(334, 386, .67)
    b += _person(326, 386, 100, 'sit', back=True)
    b += c.desk(358, 368, 115) + c.book(408, 318, 50) + c.cup(453, 314, .5)
    b += c.path('M476 232 L577 201 L670 258 L564 292Z', WHITE)
    b += c.path('M476 232 V254 L564 318 L670 281 V258 M564 292 V318 '
                'M484 254 V285 M659 281 V314', SAND, INK, 1.7)
    b += c.path('M503 228 L535 218 L574 242 L542 253Z', PALE, INK, 1.1)
    b += c.group(637, 273, _person(0, 0, 102, color=BLUE), rotate=-58)
    b += c.path('M586 248 Q605 254 638 266 L607 279 Q582 270 577 262', PALE, GREEN, 1.2)
    b += _fan(617, 384, .79)
    b += c.path('M559 363 H660 M569 360 v-58 M649 360 v-58', stroke=INK, width=2)
    b += c.feather(584, 315, 52, SAND, -14) + c.feather(616, 316, 52, SAND, 12)
    for yy in (327, 344):
        b += c.path(f'M635 {yy} q-18 -8 -41 0', stroke=BLUE, width=1.2)
    b += c.path('M695 236 V331 H670 M696 263 h13', stroke=MUTED, width=1.2)
    b += c.path('M334 304 Q663 394 718 464', stroke=MUTED, width=1.1, dash='3 6')
    b += _chair(770, 614, 1.1)
    b += c.path('M490 547 H647 V568 H490Z M490 568 V584 H647 V568 '
                'M497 584 v28 M640 584 v28', SAND, INK, 1.7)
    b += c.path('M491 546 Q508 530 528 546 Q546 562 565 545 '
                'Q584 532 603 546 H647', WHITE, INK, 1.5)
    b += c.path('M527 530 Q547 507 570 524 L589 535 Q568 550 548 545Z', PALE, INK, 1.4)
    b += c.path('M528 529 Q513 493 488 503 Q498 527 527 538 M571 525 Q598 496 618 511 Q602 532 584 539', SAND, INK, 1.2)
    b += c.path('M520 509 L529 527 M593 515 L580 533', stroke=MUTED, width=.8)
    b += c.path('M564 291 Q616 396 566 516', stroke=MUTED, width=1.1, dash='3 6')
    return _figure('housing', '住宅剖开：从玄关到坐卧与干羽', b,
                   [('玄关回转', '开门后的空地容纳舒适收翼与转身，地面连到室内生活区。'),
                    ('中央翼空间', '椅背由两侧支撑，中间真实留空，让收翼不被整块背板挤压。'),
                    ('休息支撑示例', '床旁细部仅示例避开翼根长期受压的支撑，不规定统一床垫结构。'),
                    ('低温通风', '风扇、干羽位置与通风口是维护实物，不表示高温烘烤或自动治疗。')],
                   [(52, 430, 160, 351), (822, 466, 770, 506),
                    (411, 560, 554, 548), (787, 292, 617, 354)],
                   '不看图例，能否从门走到椅子和床？放大的椅背哪里是空的，床旁翼根位置是否被整块硬面压住？',
                   '开放剖切与图旁细部不规定户型、邻接、门宽、通风参数或私有起降场', 660)


def _objects():
    b = _chair(165, 287, 1.47)
    b += c.feather(151, 143, 109, SAND, -6) + c.feather(183, 142, 108, SAND, 8)
    b += _coat(428, 277, 1.17, back=True, opened=True)
    b += c.path('M407 128 Q430 106 451 128 M428 107 V94 q0 -14 12 -8', stroke=INK, width=2)
    b += _bicycle(723, 289, .99)
    b += _shoe(143, 579, 1.12)
    b += _shoe(186, 523, .82)
    b += _ladder(423, 596, 1.35)
    b += c.path('M442 370 v-32 M421 336 h40 M434 344 h18', stroke=INK, width=2)
    b += _net(624, 424, 215, 150)
    b += c.path('M634 594 h198 M68 301 h219 M342 291 h165 M592 302 h259 '
                'M73 602 h191 M337 611 h171', stroke=LINE, width=1.5)
    return _figure('objects', '适配器物图鉴：留翼、开合与稳定支撑', b,
                   [('翼槽椅', '两侧背板之间容纳收翼，椅面和四脚提供稳定支撑。'),
                    ('翼口外衣', '衣身、袖子与背部翼口各自独立，开合只是剪裁示例。'),
                    ('低重心自行车', '车轮、低跨车架、座位与踏板构成地面通行实物，不由翼承载行李。'),
                    ('鞋与接地', '鞋底和系合结构示例稳定的步行与落地接触，不规定性能参数。'),
                    ('工具梯', '踏面、支脚与工具托位支持稳定作业，抵达高处不等于可以悬停维修。'),
                    ('醒目防护网', '网眼、加色边缘和垂挂标识使材料可见，不把透明细线当作安全屏障。')],
                   [(53, 102, 165, 163), (344, 77, 453, 172), (808, 107, 718, 244),
                    (54, 452, 143, 567), (345, 389, 419, 476), (788, 370, 733, 429)],
                   '找出六件器物真正留空、接地、开合或提高可见性的部位；哪一处只有颜色变化，哪一处改变了结构？',
                   '器物图鉴是独立放大样稿，彼此不是同一尺寸或标准产品', 660)


def _clothing():
    b = _person(174, 338, 230, color=GREEN)
    b += c.path('M135 257 h19 v21 h-19 M185 257 h22 v21 h-22', stroke=INK, width=1.1)
    b += _person(445, 338, 230, back=True)
    b += c.path('M420 179 Q403 209 413 237 M470 179 Q488 210 478 237 '
                'M443 186 V264', stroke=INK, width=1.4)
    b += c.path('M402 338 h87 M130 338 h87', stroke=LINE, width=1.3)
    b += _coat(711, 339, 1.38, back=True, opened=True)
    b += c.path('M698 145 Q710 126 724 145 M711 127 V115 q0 -13 11 -9', stroke=INK, width=2)
    b += c.path('M520 233 Q565 280 626 271', stroke=MUTED, width=1.2, dash='4 5')
    b += c.path('M73 455 Q118 428 153 441 L149 557 Q111 585 77 558Z', GREEN)
    b += c.path('M93 456 Q103 474 97 516 Q123 510 132 481 Q130 456 118 450Z', SAND, INK, 1.3)
    b += c.path('M137 442 L173 459 L166 530 L143 554Z', PALE)
    b += c.path('M143 462 L152 469 M139 483 l12 7 M137 506 l12 7', stroke=MUTED, width=1.2)
    b += c.arrow([(181, 485), (216, 485)], BLUE, 2)
    b += c.path('M237 450 Q280 426 316 442 L313 559 Q275 582 240 560Z', GREEN)
    b += c.path('M259 449 Q241 481 260 531 Q288 527 297 483 Q287 455 277 447Z', SAND, INK, 1.3)
    b += c.path('M259 449 Q242 481 260 531 M260 451 Q250 484 264 530', stroke=INK, width=1.3)
    b += c.path('M525 447 Q546 418 569 440 Q594 485 571 565 '
                'L543 595 Q509 555 509 485Z', BLUE)
    b += c.path('M536 450 Q551 440 566 449 M533 456 Q525 505 544 560 '
                'M552 460 Q569 511 556 570', stroke=WHITE, width=1)
    b += c.path('M527 447 l-9 12 M569 445 l9 11 M541 592 l14 -4', stroke=INK, width=1.3)
    b += _chair(744, 594, .8)
    b += _person(734, 594, 135, 'sit', back=True, color=TERRA)
    b += c.path('M703 511 Q719 483 726 500 M752 500 Q768 481 779 511', stroke=BLUE, width=2)
    return _figure('clothing', '完全着衣的翼口样稿：正面、背面与开合细部', b,
                   [('前后穿着', '躯干、手臂和双腿保持着衣，翼从背部独立伸出，不把袖口当翼口。'),
                    ('翼口开合', '放大的是衣料开合，不是裸体翼根；分片与闭合线只是结构示例。'),
                    ('翼罩样稿', '罩体与收翼轮廓分开表示条件防护，不赋予雨雾中飞行能力。'),
                    ('坐姿留翼', '坐下时衣身、收翼和椅背中央留空仍须互相容纳。')],
                   [(282, 82, 441, 212), (65, 391, 146, 487),
                    (516, 383, 550, 511), (829, 442, 746, 517)],
                   '正面与背面的袖子、翼和裤腿能否分别找出来？翼口打开的是哪片衣料，坐下后翼落在哪里？',
                   '服装前后视、开合与罩体均为示例，不规定地域服式、装具锁扣或防护等级', 650)


def _agriculture():
    b = c.path('M38 334 Q250 239 424 289 Q545 254 850 335 '
                'L850 614 H40Z', '#F0EDDB', LINE, 1.2)
    b += c.path('M48 372 Q246 323 434 347 M42 408 Q225 364 434 387 '
                'M41 446 Q222 410 432 427', stroke=GREEN, width=1.2)
    for row in range(3):
        for xx in range(70, 413, 44):
            b += c.plant(xx, 381 + row * 39, 24)
    b += c.path('M51 340 Q176 314 280 331 L309 345 M334 350 Q382 354 432 368',
                stroke=BLUE, width=5)
    b += c.path('M308 345 l9 -9 l12 14 l-10 6 M312 351 q-6 16 -21 21', stroke=BLUE, width=1.8)
    b += c.ellipse(313, 370, 24, 9, '#DCE8E8', BLUE, 1)
    b += _person(197, 208, 132, 'fly', opened=True)
    b += c.curve_arrow('M299 156 Q388 162 429 223', (429, 223), .9, BLUE, 2.3)
    b += c.path('M258 212 Q305 255 316 339', stroke=MUTED, width=1.2, dash='3 6')
    b += _person(353, 462, 137, 'crouch', color=TERRA)
    b += c.path('M398 414 L331 358 M395 414 l12 4', stroke=INK, width=3)
    b += c.path('M324 350 l13 1 l-4 13 l-13 -3Z', MUTED, INK, 1)
    for xx, yy in ((532, 351), (684, 326), (809, 365)):
        b += c.tree(xx, yy, 151)
        for dx, dy in ((-26, -107), (17, -98), (35, -82)):
            b += c.ellipse(xx + dx, yy + dy, 5, 6, GOLD, INK, .7)
    b += _net(481, 274, 351, 92)
    b += c.path('M470 511 L832 438 M467 522 L835 450', stroke=INK, width=2.6)
    for i in range(12):
        xx = 478 + i * 30
        yy = 518 - i * 6
        b += c.line(xx, yy - 9, xx + 5, yy + 10, GOLD, 3)
    b += c.path('M587 468 L694 448 L715 459 L607 481Z', SAND)
    b += c.path('M607 481 V491 L715 471 V459 M609 489 l-5 12 M696 473 l-5 11',
                stroke=INK, width=2)
    b += c.crate(598, 411, 54, 47) + c.crate(654, 400, 43, 47)
    for xx, yy in ((615, 494), (688, 480)):
        b += c.ellipse(xx, yy, 8, 8, MUTED, INK, 1)
    b += _person(767, 531, 121, 'operate', color=BLUE)
    b += c.arrow([(552, 556), (701, 526)], BLUE, 2.2)
    return _figure('agriculture', '田间分工：巡视看见问题，地面处理和搬运', b,
                   [('轻装巡视', '掠过田块的观察者看见灌溉断点，巡视不等于悬停耕作。'),
                    ('灌溉与处理', '水路断点与湿地可见，地面人员站稳处理，图不提供具体维修教程。'),
                    ('醒目遮网', '果园遮网有清楚的边缘与垂挂标识，巡视路径不穿过网面。'),
                    ('窄轨搬运', '果园箱货落在有轮子的窄轨货台上，沿接地轨道移动。')],
                   [(66, 75, 203, 163), (231, 554, 316, 352),
                    (761, 156, 737, 280), (616, 591, 652, 468)],
                   '从空中观察线找到灌溉断点，再找地面处理者；果园重箱的轮子实际落在哪条轨道上？',
                   '田块、水路、果树、遮网和窄轨均为示例，不命名作物或规定产量与喷洒流程', 650)


def _industry():
    b = c.path('M53 315 V72 H843 V315 M54 315 H844 M53 77 l47 -29 H800 l44 29',
               stroke=INK, width=2.5)
    b += _window(80, 97, 147, 74)
    b += c.path('M264 74 V190 H345 M268 78 V194 H345', stroke=MUTED, width=3)
    b += c.rect(360, 128, 189, 171, SAND, INK, 0, 2)
    b += c.rect(376, 142, 157, 106, PALE, INK, 1, 1.7)
    b += c.path('M386 173 H525 M387 222 H524 M408 150 V220 '
                'M426 187 H502 V213 H426Z', stroke=INK, width=2)
    b += c.ellipse(490, 181, 22, 22, GOLD, INK, 1.5)
    b += c.ellipse(490, 181, 7, 7, WHITE, INK, 1)
    b += c.path('M382 232 L530 152 M392 242 L533 163', stroke=LINE, width=1.2)
    b += c.rect(554, 182, 38, 51, WHITE, INK, 1, 1.3)
    for xx, yy in ((564, 195), (581, 195), (564, 218)):
        b += c.ellipse(xx, yy, 3, 3, TERRA if yy == 218 else GREEN, INK, .8)
    b += _person(647, 312, 139, 'operate', bound=True, helmet=True, facing=-1)
    b += c.path('M698 228 h16 v21 h-16', WHITE, INK, 1.2)
    b += c.path('M306 305 V231 M309 231 H347 M309 239 H347', stroke=INK, width=2.5)
    for yy in range(245, 295, 14):
        b += c.line(310, yy, 347, yy - 11, GOLD, 2)
    b += _pallet(141, 307, .77)
    b += c.path('M60 355 Q436 366 839 355', stroke=LINE, width=1.2)
    b += c.path('M481 614 V398 H827 V614 M487 400 H825 M508 460 H805 '
                'M508 485 H805 M508 577 H805 M508 611 H805 '
                'M521 402 L788 611 M789 402 L520 611', stroke=MUTED, width=2.1)
    b += c.path('M500 488 H810 V497 H500Z', SAND, INK, 1.8)
    b += c.path('M510 488 V426 H804 V488 M511 453 H804', stroke=INK, width=2)
    b += c.rect(725, 378, 75, 74, WHITE, INK, 1, 1.8)
    b += c.path('M735 390 h53 M735 405 h53 M735 420 h53 M730 440 h61', stroke=LINE, width=2)
    b += _person(655, 488, 131, 'operate', bound=True, helmet=True, color=TERRA)
    b += c.path('M702 409 l17 -8 l8 6 M717 401 l4 -8', stroke=INK, width=2.5)
    b += c.path('M617 412 Q576 371 548 399 V428', stroke=BLUE, width=1.8)
    b += _ladder(837, 613, .87)
    b += c.rect(528, 466, 50, 18, GOLD, INK, 2, 1.2)
    b += c.path('M539 466 v-6 h29 v6 M536 474 h34', stroke=INK, width=1)
    b += _person(170, 602, 121, 'operate', color=BLUE)
    b += c.desk(209, 602, 153)
    b += c.parcel(242, 539, 27) + c.parcel(294, 535, 34)
    b += c.notebook(362, 532, 31)
    b += c.ground(51, 616, 815)
    return _figure('industry', '稳定作业：隔离机器、接地分拣与脚手架检修', b,
                   [('收翼操作', '工人收翼并使用示例束翼装具，双手操作与双翼保持独立。'),
                    ('设备隔离', '危险机械位于实体护罩后，束翼不代替隔离设施。'),
                    ('落在脚手架', '检修者双脚站在有栏杆的踏面上，工具和安全连接不靠悬停维持。'),
                    ('接地岗位', '分拣桌与记录提供地面任务示例，不能飞行不等于不能参与工作。')],
                   [(756, 98, 673, 241), (321, 104, 470, 204),
                    (469, 441, 652, 488), (69, 479, 256, 549)],
                   '机器旋转部件与人的翼之间有什么实体隔离？检修者脚下的踏面如何连到脚手架支柱和地面？',
                   '设备、束翼带、脚手架和岗位均为示例，不规定工业门类、释放结构或资格要求', 660)


def _resilience():
    b = c.cloud(109, 71, 142) + c.cloud(286, 86, 137)
    b += c.path('M37 156 Q247 132 455 155 M62 174 Q236 150 426 169', stroke=LINE, width=2)
    b += c.path('M75 355 V208 L196 161 L320 208 V355Z', SAND)
    b += c.path('M70 208 L197 155 L326 208 M198 163 V355', stroke=INK, width=2)
    b += c.rect(133, 255, 121, 100, WHITE, INK, 0, 1.5)
    for xx, yy in ((153, 344), (196, 346), (232, 344), (173, 291), (216, 294)):
        b += _sack(xx, yy, .55)
    b += _freight_truck(355, 358, .87)
    b += _pallet(296, 350, .57)
    b += c.arrow([(258, 377), (418, 377)], BLUE, 2.3)
    b += c.path('M38 399 H866', stroke=LINE, width=1.7)
    b += c.bus(80, 601, 280)
    b += c.path('M347 600 H413 M353 591 H414 M375 593 V509 H439 V594 '
                'M387 516 h40 M387 529 h27', stroke=INK, width=1.7)
    b += _person(418, 600, 125, 'walk', elder=True, color=TERRA)
    b += _person(474, 600, 84, color=BLUE)
    b += c.path('M433 533 L483 553', stroke=INK, width=2)
    b += c.rect(511, 441, 180, 165, WHITE, INK, 0, 2)
    b += c.path('M510 441 l28 -23 H692 V441 M535 461 V604 M692 440 V604', stroke=INK, width=2)
    b += _chair(562, 598, .54)
    b += _person(556, 598, 88, 'sit', back=True)
    b += _lift(728, 400, 116, 205)
    b += c.rect(683, 461, 30, 25, WHITE, INK, 1, 1)
    b += c.arrow([(690, 474), (707, 474)], BLUE, 1.5)
    b += c.path('M698 486 V566', stroke=INK, width=2)
    b += c.rect(708, 553, 13, 29, SAND, INK, 1, 1)
    b += c.path('M711 563 h7 M711 571 h7 M714 553 v-13 h13', stroke=MUTED, width=1)
    b += c.arrow([(359, 631), (521, 631), (725, 631)], BLUE, 2.2)
    b += c.ground(41, 609, 815)
    return _figure('resilience', '停飞接续：储粮、接驳与机械到达', b,
                   [('粮仓到货车', '粮袋从粮仓进入地面货运，停飞时仍需要仓储和运输条件。'),
                    ('地面接驳', '车辆、儿童与高龄行人的接地通道连接等候空间，不要求所有人先飞行。'),
                    ('基本标识', '现场方向牌独立于掌上数字信息，示例箭头指向可用机械连接。'),
                    ('机械转运', '轿厢、井道和示例备用供电表示高处接续的设施基础，不保证全天候运行。')],
                   [(63, 112, 180, 281), (62, 435, 229, 562),
                    (630, 377, 698, 474), (859, 330, 785, 539)],
                   '从粮仓和公交各走一条接地路径，能否到达等待空间与电梯？手机失灵时，哪件实物仍能指方向？',
                   '供应与接驳小景不是灾害现场复原，不规定储备量、停电时长或备用设备标准', 670)


def _food():
    b = c.path('M50 214 Q250 225 453 214', stroke=LINE, width=1.5)
    b += c.plant(95, 191, 89)
    for xx in (74, 98, 124):
        b += c.path(f'M{xx} 168 Q{xx - 7} 129 {xx + 5} 101', stroke=GREEN, width=1.5)
        for yy in (114, 124, 134):
            b += c.ellipse(xx + 3, yy, 5, 2, GOLD, INK, .6)
    b += _bowl(216, 179, .92)
    for dx, dy in ((-17, -9), (3, -16), (16, -6)):
        b += c.ellipse(216 + dx, 164 + dy, 6, 3, GREEN, INK, .7)
    b += c.path('M286 182 Q279 159 298 145 Q320 137 332 155 Q338 178 315 190Z', GOLD, INK, 1.4)
    b += c.path('M296 154 l6 6 M312 166 l7 4', stroke=MUTED, width=.8)
    b += c.ellipse(384, 171, 13, 9, SAND, INK, 1.2)
    b += c.ellipse(408, 183, 14, 10, GOLD, INK, 1.2)
    b += c.path('M437 177 V126 Q448 118 460 126 V177Z', WHITE, INK, 1.3)
    b += c.rect(441, 117, 15, 10, GOLD, INK, 1, 1)
    b += c.path('M440 156 h17 v18 h-17Z', SAND, INK, .8)
    b += c.tree(686, 214, 148)
    b += c.ellipse(674, 113, 6, 7, GOLD, INK, .8)
    b += c.ellipse(719, 140, 6, 7, TERRA, INK, .8)
    b += c.path('M515 211 Q525 178 544 177 Q560 183 557 201 '
                'Q533 220 515 211Z', TERRA, INK, 1.2)
    b += c.arrow([(385, 243), (316, 294)], BLUE, 2.3)
    b += c.arrow([(488, 244), (561, 294)], BLUE, 2.3)
    b += c.desk(66, 438, 310) + _meal(219, 376, 1.38)
    b += c.desk(497, 438, 318) + _meal(631, 376, 1.32, return_meal=True)
    b += c.path('M66 485 V548 H291 V485 L179 454Z', SAND, INK, 1.6)
    b += c.rect(111, 505, 133, 63, WHITE, INK, 0, 1.2)
    b += _sack(145, 561, .53) + _sack(190, 562, .61) + _sack(229, 561, .48)
    b += _railcar(409, 607, .93)
    b += _pallet(729, 603, .79)
    b += _pallet_jack(722, 605, .69)
    b += c.arrow([(296, 591), (389, 591)], BLUE, 2.3)
    b += c.ground(51, 610, 800)
    return _figure('food', '从食物来源到启程、归台餐与储粮运输', b,
                   [('多类来源', '谷物、豆类、薯类、坚果、油脂和水果等已知来源共同支持饮食。'),
                    ('启程餐静物', '碗、食物与杯示例出发前的餐食用途，不规定精确搭配和食用量。'),
                    ('归台餐静物', '水杯、容器与餐食提示补水补能，吃完不等于体力立刻完全恢复。'),
                    ('粮仓与铁路', '粮袋、仓门和有轮的货车厢表示储粮运输基础，而不是个人飞运成批食物。')],
                   [(45, 70, 216, 166), (94, 290, 215, 372),
                    (798, 273, 739, 360), (314, 480, 544, 560)],
                   '找出来源静物、两张餐桌和储粮货运；杯子出现在哪些用途里，粮袋为什么没有挂在飞行者身上？',
                   '食物外观和餐具为示例，未规定作物品种、食谱、营养数值或储量，不表示即时恢复效果', 660)


def _rescue():
    b = c.path('M50 272 Q147 244 254 269 L341 291 H525 L563 318 '
               'H48Z', PALE, INK, 1.7)
    b += c.path('M49 317 H562 M69 272 l23 -21 l34 9 M379 291 h108 '
                'M342 293 V317 M527 295 V318', stroke=MUTED, width=1.3)
    b += _person(170, 190, 125, 'fly', opened=True, color=TERRA)
    b += c.curve_arrow('M270 127 Q352 125 384 209', (384, 209), 1.15, BLUE, 2.4)
    b += c.path('M207 209 Q278 233 321 256', stroke=MUTED, width=1.2, dash='3 6')
    b += _person(323, 293, 130, 'point', color=BLUE)
    b += _terminal(359, 220, .34)
    b += c.path('M641 311 H839 M646 311 V155 H839 V311 M646 155 l25 -15 H839',
                stroke=INK, width=2)
    b += _person(682, 309, 122, 'crouch', color=BLUE)
    b += _stretcher(785, 307, .68)
    b += c.path('M751 253 Q774 247 803 258 M758 273 H811', stroke=BLUE, width=2)
    b += c.path('M67 390 Q180 365 287 383 L379 451 H618 L675 482 H854',
                stroke=INK, width=2)
    b += c.path('M64 400 Q180 375 284 393 L376 461 H615 L672 492 H854',
                stroke=LINE, width=5)
    b += _person(277, 575, 127, 'operate', color=TERRA)
    b += _stretcher(405, 574, 1.13)
    b += _person(549, 574, 133, 'operate', color=BLUE, facing=-1)
    b += _vehicle(740, 576, .81)
    b += c.path('M615 546 L641 538 V570 H612Z', SAND, INK, 1.2)
    b += c.arrow([(113, 604), (584, 604), (663, 604)], BLUE, 2.5)
    b += c.ground(53, 583, 801)
    return _figure('rescue', '定位之后：安全固定、落地交接与机械转运', b,
                   [('定位与引导', '轻装人员移动观察并落地引导，空中任务不包括抱着成人飞走。'),
                    ('保护状态示意', '被照护者在稳定支撑上等待专业处理，只表示安全固定目标而不画操作步骤。'),
                    ('落地交接', '人员与担架均在地面接续，展开的轮架承担被照护者的重量。'),
                    ('担架与车辆', '非血腥的被照护者经机械担架进入车辆链路，不要求受伤后自行飞回。')],
                   [(74, 74, 177, 150), (808, 97, 776, 267),
                    (184, 435, 405, 535), (794, 410, 744, 499)],
                   '谁负责定位，什么真正承载被照护者？沿轮子和地面通道，能否找到车辆而不需要任何人吊着伤者飞？',
                   '任务分工与转运器材形制为示例，不是急救、安全固定或搬运操作教程', 650)


def _medicine():
    b = c.path('M52 300 V83 H399 V300 M399 83 H851 V300 M52 300 H851 '
               'M414 300 V191 M473 300 V191 M415 191 H473', stroke=INK, width=2)
    b += _window(82, 108, 97, 65)
    b += _chair(155, 295, .87) + _person(145, 295, 128, 'sit', back=True)
    b += _chair(309, 295, .87) + _person(299, 295, 124, 'sit', color=TERRA, elder=True)
    b += c.cup(345, 223, .47)
    b += c.path('M193 278 Q208 267 229 278', stroke=BLUE, width=1.3, dash='4 4')
    b += _chair(577, 295, .79) + _person(567, 295, 128, 'sit', back=True, color=BLUE)
    b += _person(666, 295, 141, 'groom', color=WHITE, facing=-1)
    b += c.path('M637 241 L629 249', stroke=INK, width=2)
    b += c.desk(766, 295, 74) + c.notebook(779, 216, 27)
    b += c.path('M604 215 q7 8 8 19', stroke=MUTED, width=1)
    b += c.path('M81 367 H824 M104 365 V348 M800 365 V348', stroke=LINE, width=1.7)
    b += c.path('M182 563 V451 H438 V563 M183 453 H437 M185 485 H437', stroke=BLUE, width=3)
    b += _person(281, 566, 140, 'walk', color=TERRA)
    b += _person(431, 566, 143, 'point', color=WHITE)
    b += c.path('M281 566 h18 M323 555 l15 3', stroke=GOLD, width=3)
    b += _chair(642, 578, .7) + _person(634, 578, 112, 'sit', color=BLUE, elder=True)
    b += c.desk(680, 574, 117) + c.book(724, 524, 63)
    b += c.cup(778, 518, .56)
    b += c.path('M545 575 V424 H845 V575 M557 574 V434 H833 V574', stroke=LINE, width=1.7)
    b += c.path('M510 566 H549 M510 574 H549', stroke=INK, width=1.8)
    b += c.ground(56, 580, 801)
    return _figure('medicine', '留翼候诊、专业评估与地面康复参与', b,
                   [('候诊留翼位', '翼槽座椅之间保留收翼空间，等候者稳定落座而不是悬停排队。'),
                    ('检查与评估', '专业人员在地面观察羽面与状态，检查不等于手术或立刻准许复飞。'),
                    ('地面康复', '扶栏和陪同示例支持接地活动，康复不强迫伤者尝试飞行。'),
                    ('日常参与', '阅读、相聚与舒适落座同样是恢复独立和参与生活的目标。')],
                   [(68, 53, 203, 212), (815, 64, 605, 221),
                    (111, 437, 292, 518), (790, 383, 721, 524)],
                   '候诊椅之间和背后留下了哪些空间？从检查处到扶栏，再到阅读桌，哪些活动不以飞行为前提？',
                   '候诊、检查与康复空间是并置示例，不规定诊断、疗程、手术线路或复飞标准', 650)


def _education():
    b = c.path('M52 326 V70 H449 V326 M52 326 H449 M449 326 V226 '
               'M448 70 H849', stroke=INK, width=2)
    b += c.rect(90, 91, 188, 88, PALE, INK, 1, 1.8)
    b += c.path('M110 115 h41 M110 127 h65 M110 142 h53 '
                'M212 112 L243 149 H198Z M212 111 V148', stroke=MUTED, width=1.4)
    b += c.path('M101 185 h163 M183 179 v6', stroke=INK, width=2)
    b += _person(346, 317, 142, 'point', color=TERRA)
    b += _chair(134, 320, .57) + _person(128, 320, 89, 'sit', back=True)
    b += c.desk(104, 268, 81) + c.book(140, 212, 39)
    b += _chair(254, 320, .57) + _person(248, 320, 87, 'sit', back=True, color=BLUE)
    b += c.desk(224, 269, 81) + c.book(260, 213, 39)
    b += _window(378, 90, 48, 101)
    b += c.tree(795, 312, 126)
    b += c.path('M488 325 H849 M495 315 H552', stroke=LINE, width=1.8)
    b += c.path('M60 551 L208 502 L292 526 L446 553 H628 L735 561 H853 '
               'V604 H60Z', PALE, GREEN, 1.7)
    b += c.path('M62 550 L209 501 L292 526 M64 557 L209 509', stroke=GOLD, width=3)
    b += _person(265, 493, 88, 'land', opened=True, color=BLUE)
    b += c.curve_arrow('M180 419 Q249 423 325 478 Q361 505 395 534',
                       (395, 534), .7, BLUE, 2.2)
    b += c.ellipse(408, 552, 47, 12, SAND, GREEN, 1.3)
    b += _person(414, 551, 94, 'land', opened=True)
    b += _person(611, 570, 138, 'point', color=TERRA)
    b += c.path('M472 594 H701 M483 592 V580 M684 592 V580', stroke=LINE, width=1.5)
    b += c.bus(745, 608, 105)
    b += c.desk(495, 377, 111) + c.cup(520, 323, .5) + _bowl(568, 331, .43)
    b += c.path('M722 370 Q736 357 753 371 L749 386 H726Z', GOLD, INK, 1.2)
    b += c.path('M718 394 H760 M724 395 V425 M754 395 V425', stroke=INK, width=2)
    return _figure('education', '并行学习：文化课堂与低坡监督练习', b,
                   [('文化课堂', '孩子稳定落座读写，普通学科学习不由飞行成绩替代。'),
                    ('低坡短通道', '练习从低坡进入软地，箭头表示短程移动与制动而非高台试飞。'),
                    ('地面监督', '教师站在可观察的位置，孩子不需要跳下高楼证明能力。'),
                    ('学习支撑', '餐具、护具和接驳车示例支持参与，两类学习并行而不是职业晋级阶梯。')],
                   [(54, 39, 185, 130), (91, 409, 219, 508),
                    (666, 420, 610, 506), (822, 360, 745, 374)],
                   '课堂椅子和低坡各支持什么学习？观察孩子脚下的坡与软地，教师能看见整个短通道吗？',
                   '课堂、低坡、护具与接驳均为示例，不规定课表、训练年龄、评分或统一晋级顺序', 660)


def _sports():
    b = c.path('M54 295 H849 M59 286 L172 255 H262 L302 280 '
               'H438 L510 296', stroke=LINE, width=1.7)
    b += c.path('M73 283 L174 255 H219 V276 L95 307 H73Z', SAND, INK, 1.5)
    b += c.ellipse(403, 290, 69, 19, PALE, GREEN, 1.2)
    b += c.ellipse(403, 290, 40, 10, 'none', GREEN, 1)
    b += _person(212, 252, 91, 'land', opened=True, color=BLUE)
    b += _person(395, 289, 98, 'land', opened=True)
    b += c.curve_arrow('M250 196 Q314 204 353 256', (353, 256), 1, BLUE, 2.2)
    b += _person(571, 310, 146, 'point', color=TERRA)
    b += c.path('M759 314 V160 M753 160 L777 171 L756 183Z', GOLD, INK, 1.5)
    b += _person(717, 220, 80, 'fly', opened=True, color=BLUE)
    b += c.curve_arrow('M645 205 Q694 131 769 127 Q815 141 815 194 '
                       'Q811 226 790 243', (790, 243), 2.4, BLUE, 2.2)
    b += c.path('M62 381 Q439 395 838 381', stroke=LINE, width=1.4)
    b += c.path('M80 579 L212 451 H730 L846 579Z', PALE, GREEN, 1.6)
    b += c.path('M467 451 V579 M118 552 H810 M204 471 H748', stroke=WHITE, width=2)
    b += c.ellipse(467, 524, 73, 22, 'none', WHITE, 2)
    b += _person(263, 557, 130, 'run', color=BLUE)
    b += _person(632, 557, 130, 'run', color=TERRA)
    b += c.ellipse(397, 542, 16, 16, WHITE, INK, 1.5)
    b += c.path('M397 527 l8 8 l-4 10 h-10 l-4 -10Z M385 549 l8 -4 '
                'M401 545 l10 4', stroke=INK, width=1)
    b += c.arrow([(365, 555), (485, 555)], BLUE, 2)
    b += c.path('M127 579 V503 H178 V579 M128 503 h50 M140 507 V578 M154 507 V578 '
                'M127 524 H178 M127 546 H178 M127 567 H178', stroke=INK, width=1.4)
    b += c.cup(760, 620, .65) + c.path('M727 627 H808', stroke=LINE, width=1.3)
    return _figure('sports', '近地运动观察：低台制动、绕标与地面球类', b,
                   [('低台与制动', '儿童在低台和软地之间练习短程制动，不从高处冒险跃下。'),
                    ('监督绕标', '一瞬间的移动姿态沿标杆外侧绕行，不表示定点悬停。'),
                    ('地面监督', '监督者脚踏稳定地面，观察通道与落点；示例不规定训练评分或极限纪录。'),
                    ('收翼球类', '球、鞋、场线与立在地面的球门构成地面运动，双翼收起但双手与双腿独立。')],
                   [(79, 104, 184, 271), (834, 85, 758, 171),
                    (554, 112, 571, 238), (98, 407, 399, 542)],
                   '找出低台的真实高度关系、软地落点和绕标方向；地面球类中球、鞋与收起的翼怎样分工？',
                   '低台、软地、标杆与球场是运动形制示例，不规定尺寸、安全阈值或竞技规则', 660)


def _travel():
    b = _railcar(52, 300, 1.26, passenger=True)
    b += c.path('M45 324 H492 V337 H45Z', SAND, INK, 1.5)
    b += c.path('M66 341 H479 M69 348 H479', stroke=LINE, width=1)
    b += _person(447, 323, 135, 'walk', color=TERRA)
    b += c.rect(494, 273, 36, 47, GOLD, INK, 4, 1.3)
    b += c.path('M506 273 v-15 h14 v15 M500 281 v30 M523 281 v30', stroke=INK, width=1.2)
    b += c.ellipse(501, 321, 4, 4, MUTED, INK, 1)
    b += c.ellipse(523, 321, 4, 4, MUTED, INK, 1)
    b += c.path('M468 254 L510 257', stroke=INK, width=1.8)
    b += c.path('M562 324 V183 H668 V324 M562 183 l29 -16 H668 V183', stroke=INK, width=2)
    b += c.rect(578, 223, 69, 101, WHITE, INK, 0, 1.4)
    b += c.rect(585, 280, 22, 37, SAND, INK, 2, 1)
    b += c.path('M590 280 v-9 h12 v9', stroke=INK, width=1)
    b += _person(717, 323, 124, 'walk', color=BLUE)
    b += c.tree(811, 330, 162)
    b += c.arrow([(487, 366), (632, 366), (708, 366)], BLUE, 2.3)
    b += c.path('M65 590 H841 M69 600 H841 M75 587 V467 H187 V586 '
               'M80 467 H189', stroke=INK, width=1.8)
    b += _lift(91, 426, 90, 163)
    b += c.path('M187 468 H313 M189 477 H315 M199 467 V424 H295 V467 '
               'M199 446 H295', stroke=INK, width=2)
    b += _person(261, 467, 103, 'stand', back=True)
    b += c.tree(422, 563, 121)
    b += c.path('M314 484 Q375 449 443 473 Q490 482 519 477 '
               'M525 471 Q582 436 624 459', stroke=LINE, width=2)
    b += _person(481, 453, 105, 'fly', opened=True, color=BLUE)
    b += c.curve_arrow('M321 397 Q402 359 474 366 Q575 376 630 433',
                       (630, 433), .75, BLUE, 2.2)
    b += c.path('M647 517 H845 V527 H647 M663 517 V472 H831 V517 '
               'M663 491 H831 M665 527 V590 M829 527 V590', stroke=INK, width=2)
    b += _person(742, 516, 118, back=True, color=TERRA)
    b += c.path('M320 559 Q481 575 646 548', stroke=GOLD, width=3)
    b += _person(408, 568, 99, 'walk', color=GREEN, elder=True)
    b += c.cup(803, 510, .45)
    b += c.arrow([(293, 610), (506, 610), (654, 610)], GOLD, 2.2)
    return _figure('travel', '旅行抵达之后：寄存、轻装探索与机械观景', b,
                   [('带行李乘铁路', '有体积的行李随铁路到达，旅客在站台步行接续而不是飞运大箱。'),
                    ('当地轻装', '行李可在示例寄存空间留下，当地探索仍受可用落点、补给与天气影响。'),
                    ('步行与电梯', '接地步道和电梯通到有栏杆的观景平台，不能飞者也有到达方式。'),
                    ('停下观景', '到达后可在稳定位置落座或站立观景，旅途不依赖无限接力飞行。')],
                   [(53, 103, 512, 296), (702, 109, 604, 297),
                    (58, 397, 137, 539), (822, 386, 742, 471)],
                   '大行李在铁路之后留在哪里？沿轻装空中线与接地步道、电梯，都能找到稳定的观景终点吗？',
                   '站台、寄存和观景连接为示例，不是实际地图、景点、航线或固定间距', 670)


def _daily():
    b = _window(57, 65, 154, 110)
    b += _chair(124, 303, .72) + _person(116, 303, 117, 'sit', back=True)
    b += _person(203, 303, 117, 'groom', color=TERRA, facing=-1)
    b += c.desk(282, 303, 114) + _meal(334, 250, .63)
    b += c.path('M149 225 q8 9 7 23', stroke=MUTED, width=1)
    b += c.path('M53 305 H404 M58 313 h338', stroke=LINE, width=1.4)
    b += _window(528, 66, 131, 98)
    b += _chair(580, 302, .71) + _person(570, 302, 116, 'sit', color=BLUE)
    b += c.desk(602, 299, 221) + c.book(670, 248, 62)
    b += c.parcel(746, 222, 37) + c.notebook(789, 214, 29)
    b += c.path('M525 306 H849', stroke=LINE, width=1.4)
    b += c.bus(52, 583, 213)
    b += _person(322, 584, 128, 'walk', color=TERRA)
    b += _person(264, 584, 83, 'walk', color=BLUE)
    b += c.path('M276 600 h24 M317 601 h29', stroke=LINE, width=1.1)
    b += c.path('M48 593 H371 M70 600 H348', stroke=LINE, width=1.5)
    b += c.path('M415 555 H597 M416 555 V409 H597 V555 '
               'M424 435 H590 M424 459 H590', stroke=INK, width=1.6)
    b += _chair(453, 551, .56) + _person(446, 551, 91, 'sit', elder=True)
    b += _chair(540, 551, .56) + _person(533, 551, 91, 'sit', elder=True, color=TERRA)
    b += c.desk(482, 541, 53) + c.cup(504, 487, .44)
    b += c.path('M392 555 V473 H408 V555 M393 481 h14 M393 493 h14', stroke=BLUE, width=1.5)
    b += _chair(722, 581, .71) + _person(713, 581, 114, 'sit', back=True, color=BLUE)
    b += _person(800, 581, 119, 'groom', color=TERRA, facing=-1)
    b += c.path('M745 505 q9 9 7 25', stroke=MUTED, width=1)
    b += _fan(647, 580, .69)
    b += c.path('M632 595 H856 M640 602 H844', stroke=LINE, width=1.5)
    b += c.path('M671 450 V398 H834 V450 M673 398 l19 -13 H834 '
               'M694 412 h26 M737 412 h26 M778 412 h25', stroke=LINE, width=1.5)
    return _figure('daily', '不同状态的生活观察：整羽、工作、接驳与照护', b,
                   [('整羽与早餐', '维护与餐食支持日常生活，图中地面协助以获得同意为前提。'),
                    ('落地工作', '收翼读写与分拣不依赖持续飞行，身体状态可以改变出行而不取消工作参与。'),
                    ('儿童接驳', '孩子自己站在地面，由成人陪同走向车辆，不抱婴儿飞行。'),
                    ('高龄相聚', '老人稳定落座、补水和相聚，地面与机械连接支持共同参与。'),
                    ('家庭照护', '坐姿检查、整理羽面与低温通风示例照护，不将维护画成治疗。')],
                   [(58, 39, 155, 232), (798, 44, 670, 248),
                    (68, 392, 291, 541), (415, 361, 503, 485),
                    (819, 361, 752, 505)],
                   '分别观察孩子、老人、劳动人员和被照护者脚下的支撑：哪件家具、交通或照护器物让他们继续参与生活？',
                   '五处小景是不同状态的并置观察，不是同一人物的固定二十四小时故事或家庭设定', 650)


DIAGRAMS = {
    'logistics': _logistics(),
    'energy': _energy(),
    'housing': _housing(),
    'objects': _objects(),
    'clothing': _clothing(),
    'agriculture': _agriculture(),
    'industry': _industry(),
    'resilience': _resilience(),
    'food': _food(),
    'rescue': _rescue(),
    'medicine': _medicine(),
    'education': _education(),
    'sports': _sports(),
    'travel': _travel(),
    'daily': _daily(),
}
