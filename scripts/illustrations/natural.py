"""自然史淡彩线描；形制与功能复原为示例，不增补精细解剖或地理。"""
from common import *


DIAGRAMS = {}
SKIN = '#E9C6A4'
GREY = '#ADB0AA'
BROWN = '#93745C'
BLACK = '#484641'
RUST = '#B9805A'


def _hand(x, y, side=1):
    b = path('M-3 -4 Q-7 -7 -8 -3 L-7 5 Q-4 10 2 8 L5 4 L5 -4Z', SKIN, INK, 1)
    for xx in [-3, 0, 3]:
        b += line(xx, 3, xx, 7, MUTED, .65)
    return group(x, y, b, side)


def _quill(x, y, length=150, color=SAND, angle=0, broken=False):
    """可观察的羽片外形；不命名或放大未知微观结构。"""
    b = path('M0 117 C-32 99 -39 65 -27 32 Q-16 8 0 -12 Q26 8 33 40 C43 76 27 104 0 117Z', color, INK, 1.7)
    if broken:
        b += path('M0 -5 Q4 28 3 55 M2 71 Q3 96 0 140', stroke=INK, width=2)
        b += path('M-18 55 L-5 60 L5 53 L-2 66 L12 60 L20 65 L9 74 L-3 69 L-16 75', PAPER, TERRA, 1.7)
    else:
        b += path('M0 -5 Q6 56 0 140', stroke=INK, width=2)
    for i in range(12):
        yy = 8 + i * 8
        rr = 11 + 20 * math.sin((i + 1) * math.pi / 14)
        if broken and 48 < yy < 75:
            continue
        b += path(f'M3 {yy + 8} Q{-rr * .4} {yy + 2} {-rr} {yy - 5}', stroke=MUTED, width=.8)
        b += path(f'M3 {yy + 8} Q{rr * .5} {yy + 1} {rr} {yy - 7}', stroke=MUTED, width=.8)
    b += path('M-24 35 q-5 14 -2 27 M26 51 q6 15 1 28', stroke=WHITE, width=1.3)
    return group(x, y, b, length / 152, angle)


def _down(x, y, scale=1):
    b = path('M0 58 Q5 31 0 0', stroke=MUTED, width=1.6)
    for i in range(10):
        yy = i * 4
        reach = 18 + 12 * math.sin(i * .5)
        b += path(f'M1 {yy + 7} C{-reach * .3} {yy - 11} {-reach} {yy - 17} {-reach - 3} {yy - 5} q-5 8 2 12', stroke=GREY, width=1)
        b += path(f'M1 {yy + 7} C{reach * .4} {yy - 14} {reach} {yy - 18} {reach + 3} {yy - 6} q6 10 -2 13', stroke=MUTED, width=.8)
    return group(x, y, b, scale)


def _fan(side=1, color=SAND, changing=False):
    b = path('M0 0 Q36 -67 94 -97 Q152 -123 206 -99 Q204 -31 144 18 Q80 75 15 36Z', color, INK, 2)
    for i in range(11):
        bx, by = 64 + i * 12, -40 - i * 4.5
        tx, ty = 62 + i * 13.3, 64 - i * 5.1
        short = changing and i in [2, 7]
        if short:
            tx, ty = bx + 5, by + 43
        shade = PALE if short else color
        b += path(f'M{bx - 8} {by} Q{bx + 10} {by + 20} {tx + 5} {ty - 9} Q{tx + 5} {ty + 6} {tx - 5} {ty + 3} Q{bx - 12} {by + 30} {bx - 8} {by}Z', shade, INK, 1.1)
        b += path(f'M{bx - 2} {by + 9} Q{bx + 4} {by + 35} {tx} {ty - 4}', stroke=MUTED, width=.9)
        for j in range(3):
            yy = by + 19 + j * 9
            xx = bx + (tx - bx) * (j + 1) / 5
            b += path(f'M{xx} {yy} l-7 -4 M{xx} {yy} l6 -6', stroke=MUTED, width=.55)
    b += path('M4 4 Q38 -44 92 -65 Q134 -88 184 -86', stroke=INK, width=1.8)
    for i in range(8):
        xx, yy = 18 + i * 19, -11 - i * 8
        b += path(f'M{xx} {yy} q7 -16 21 -12 q-1 12 -13 19', color, MUTED, .9)
        b += path(f'M{xx + 2} {yy + 9} q8 -10 17 -8', stroke=MUTED, width=.8)
    return f'<g transform="scale({side} 1)">{b}</g>'


def _fold(side=1, color=SAND):
    b = path('M0 0 Q30 -20 39 8 Q58 42 26 92 Q3 70 -4 26Z', color, INK, 1.7)
    for i in range(7):
        b += path(f'M{10 + i * 3} {8 + i * 2} Q{44 + i * 2} {46 + i * 2} {22 + i * 2} {80 - i * 2}', stroke=MUTED, width=.8)
    for i in range(5):
        b += path(f'M{3 + i * 4} {4 + i * 4} q12 -9 20 7', stroke=MUTED, width=.85)
    return f'<g transform="scale({side} 1)">{b}</g>'


def _figure(x, y, h=130, pose='stand', opened=False, back=False, shirt=GREEN, wing_scale=.62, elder=False):
    """着装完整，手臂、翼与腿彼此独立；y 为脚下稳定地面。"""
    b = ''
    for side in [-1, 1]:
        wings = _fan(side) if opened else _fold(side)
        b += group(side * 8, -77, wings, wing_scale)
    b += ellipse(0, -101, 12, 15, SKIN, INK, 1.5)
    hair = GREY if elder else MUTED
    b += path('M-12 -103 Q-12 -119 2 -118 Q14 -117 12 -101 Q3 -111 -12 -103Z', hair, INK, 1)
    if not back:
        b += ellipse(5, -103, 1, 1.2, INK)
        b += path('M5 -96 q4 2 6 -1', stroke=MUTED, width=.7)
    b += path('M-12 -81 Q0 -85 12 -81 L17 -43 Q0 -36 -17 -43Z', shirt, INK, 1.7)
    if back:
        b += path('M-8 -80 Q0 -76 8 -80 M-15 -78 Q-20 -69 -13 -56 M15 -78 Q20 -69 13 -56 M-11 -76 Q0 -71 11 -76', stroke=MUTED, width=.8)
    else:
        b += path('M-9 -79 Q0 -74 9 -79 M0 -72 V-44 M-10 -52 h7 M6 -52 h5', stroke=MUTED, width=.8)
        for yy in [-68, -60, -51]:
            b += ellipse(2, yy, .9, .9, INK)
    if pose in ['sit', 'care', 'work']:
        b += path('M-11 -42 L-12 -25 L14 -25 L19 -3 M9 -42 L18 -33 L31 -33 L34 -3', stroke=BLACK, width=8)
        if pose == 'work':
            b += path('M-12 -75 Q-19 -55 4 -42 L30 -38 M12 -75 Q34 -62 41 -43 L44 -38', stroke=shirt, width=7)
            hands = [(31, -38), (46, -38)]
        else:
            b += path('M-12 -75 Q-27 -61 -19 -44 L3 -38 M12 -75 Q31 -61 30 -49 L16 -39', stroke=shirt, width=7)
            hands = [(5, -38), (15, -39)]
        shoes = [(19, -2), (34, -2)]
    elif pose == 'push':
        b += path('M-9 -42 L-13 -24 L-21 -2 M9 -42 L18 -25 L26 -7', stroke=BLACK, width=8)
        b += path('M-13 -75 L-29 -78 L-43 -82 M13 -75 L-16 -87 L-48 -82', stroke=shirt, width=7)
        hands = [(-43, -82), (-48, -82)]
        shoes = [(-21, -1), (26, -6)]
    elif pose == 'reach':
        b += path('M-10 -42 L-13 -20 L-15 -2 M9 -42 L14 -21 L18 -2', stroke=BLACK, width=8)
        b += path('M-13 -75 L-26 -62 L-35 -41 M13 -75 L28 -72 L44 -83', stroke=shirt, width=7)
        hands = [(-36, -39), (46, -84)]
        shoes = [(-16, -1), (19, -1)]
    elif pose in ['fly', 'glide']:
        b += path('M-9 -42 L-19 -23 L-9 -10 M9 -42 L23 -26 L34 -20', stroke=BLACK, width=8)
        b += path('M-13 -74 L-30 -63 L-43 -56 M13 -74 L31 -64 L44 -68', stroke=shirt, width=7)
        hands = [(-45, -55), (46, -68)]
        shoes = [(-9, -9), (34, -19)]
    elif pose == 'walk':
        b += path('M-9 -42 L-16 -24 L-29 -2 M9 -42 L22 -27 L35 -12', stroke=BLACK, width=8)
        b += path('M-13 -75 L-27 -56 L-37 -62 M13 -75 L26 -57 L38 -46', stroke=shirt, width=7)
        hands = [(-39, -62), (40, -45)]
        shoes = [(-29, -1), (35, -11)]
    else:
        b += path('M-9 -42 L-10 -20 L-12 -2 M9 -42 L11 -20 L13 -2', stroke=BLACK, width=8)
        b += path('M-13 -75 Q-24 -61 -25 -38 M13 -75 Q26 -61 26 -38', stroke=shirt, width=7)
        hands = [(-25, -35), (26, -35)]
        shoes = [(-12, -1), (13, -1)]
    for j, (hx, hy) in enumerate(hands):
        b += _hand(hx, hy, -1 if j == 0 else 1)
    for sx, sy in shoes:
        b += path(f'M{sx - 4} {sy - 3} q7 -2 12 3 l-1 4 h-15Z', BROWN, INK, 1)
        b += line(sx - 4, sy + 4, sx + 7, sy + 4, INK, .8)
    return group(x, y, b, h / 120)


def _profile(x, y, h=270):
    b = group(8, -78, _fold(1, GREY), .95)
    b += path('M-6 -42 L-9 -19 L-14 -2 M6 -42 L9 -20 L8 -2', stroke=BLACK, width=8)
    b += path('M-14 -4 h-12 v6 h18 M8 -4 h-14 v6 h18', BROWN, INK, 1)
    b += path('M-11 -79 Q-18 -65 -10 -42 Q4 -38 15 -45 Q20 -62 11 -81Z', GREEN, INK, 1.6)
    b += path('M-12 -73 Q-28 -59 -24 -38', stroke=GREEN, width=7) + _hand(-25, -35)
    b += ellipse(-1, -101, 11, 15, SKIN, INK, 1.5)
    b += path('M-10 -104 Q-10 -118 4 -117 L10 -107 Q0 -111 -10 -104Z', MUTED, INK, 1)
    b += path('M-10 -104 l-5 5 l5 2 M-8 -93 q4 2 6 0', stroke=INK, width=.9)
    b += ellipse(-8, -103, .9, 1.1, INK)
    b += group(14, -77, _fold(1), 1.04)
    b += path('M-4 -74 Q-17 -60 -16 -40', stroke=GREEN, width=7) + _hand(-16, -37)
    b += path('M-6 -78 Q2 -72 7 -77 M-4 -66 v17 M-10 -48 h13', stroke=MUTED, width=.85)
    return group(x, y, b, h / 120)


def _baby(x, y, scale=1):
    b = ellipse(0, 46, 41, 8, PALE)
    for side in [-1, 1]:
        b += group(side * 23, 8, _fold(side, PALE), .32)
        b += group(side * 28, 14, _down(0, 0), .25)
    b += path('M-25 5 Q-32 20 -17 42 Q0 56 21 36 Q32 16 22 4Z', SAND, INK, 1.7)
    b += path('M-23 10 L20 28 M-26 19 L11 43 M-15 38 L23 16', stroke=GOLD, width=1.3)
    b += ellipse(0, 0, 13, 14, SKIN, INK, 1.5)
    b += path('M-12 -4 Q-8 -16 4 -14 Q10 -12 12 -5', stroke=BROWN, width=1.3)
    b += path('M-7 1 q3 2 5 0 M3 1 q3 2 5 0 M-3 7 q3 2 6 0', stroke=MUTED, width=.9)
    return group(x, y, b, scale)


def _crib(x, y, scale=1, infant=True):
    b = path('M-105 -15 L-67 -48 H81 L109 -13 L69 14 H-68Z', SAND, INK, 2)
    b += path('M-85 -17 Q-63 -41 -40 -34 Q-23 -23 -12 -31 Q4 -42 24 -29 Q43 -20 64 -33 L90 -13 L65 3 H-62Z', WHITE, INK, 1.2)
    b += path('M-77 -11 Q-54 -29 -34 -20 M39 -23 Q60 -29 78 -12', stroke=BLUE, width=1.8)
    if infant:
        b += _baby(0, -32, .72)
    b += path('M-106 -65 V29 M108 -66 V27 M-106 -65 L-77 -87 H77 L108 -66 M-106 -8 H108 M-106 29 H108', stroke=BROWN, width=3)
    for i in range(13):
        xx = -95 + i * 16
        b += line(xx, -5, xx, 28, GOLD, 2)
    for i in range(9):
        xx = -67 + i * 17
        b += line(xx, -83, xx, -48, GOLD, 1.3)
    b += path('M-106 29 L-110 50 M108 27 L113 50 M-72 14 L-75 49 M68 14 L73 49', stroke=INK, width=3)
    return group(x, y, b, scale)


def _pram(x, y, scale=1):
    b = path('M-79 -36 Q-89 -85 -53 -112 Q-8 -129 30 -89 L40 -35Z', PALE, INK, 2)
    b += path('M-73 -35 Q-60 -71 -34 -70 Q-9 -71 12 -44', stroke=GREEN, width=1.3)
    b += _baby(-9, -65, .62)
    b += path('M-73 -32 Q-45 -8 28 -18 L56 -44 Q-18 -60 -73 -32Z', SAND, INK, 1.7)
    b += path('M-52 -33 Q-37 -47 -20 -34 M2 -34 Q20 -46 39 -35', stroke=BLUE, width=1.5)
    b += path('M-60 -19 L29 24 M32 -24 L-43 25 M36 -30 L68 -93 L93 -93', stroke=INK, width=3)
    b += path('M-43 23 H43 M-55 -18 H30', stroke=MUTED, width=2)
    for xx in [-44, 42]:
        b += ellipse(xx, 25, 15, 15, BLACK, INK, 1.5) + ellipse(xx, 25, 7, 7, WHITE, INK, 1)
        for angle in range(0, 360, 60):
            rad = math.radians(angle)
            b += line(xx, 25, xx + 7 * math.cos(rad), 25 + 7 * math.sin(rad), MUTED, .8)
    return group(x, y, b, scale)


def _water(x, y, w, depth=90, rows=5):
    b = path(f'M{x} {y} Q{x + w * .3} {y - 11} {x + w * .6} {y + 2} T{x + w} {y} L{x + w} {y + depth} H{x}Z', '#E4ECEB', 'none')
    for j in range(rows):
        yy = y + 12 + j * depth / (rows + 1)
        for i in range(5):
            xx = x + 12 + i * (w - 28) / 5 + (j % 2) * 9
            b += path(f'M{xx} {yy} q11 -4 22 0 t22 0', stroke=BLUE, width=.9, opacity=.65)
    return b


def _rocks(x, y, scale=1):
    b = path('M-41 9 L-27 -13 L-1 -21 L17 -3 L40 6 L26 16 H-29Z', '#E3DED3', MUTED, 1.1)
    b += path('M-27 -13 L-15 4 L17 -3 M-1 -21 L-15 4 L-8 15 M17 -3 L26 16', stroke=GREY, width=1)
    return group(x, y, b, scale)


def _leaves(x, y, scale=1):
    b = path('M-61 8 Q-82 -14 -53 -26 Q-58 -51 -27 -44 Q-6 -66 14 -44 Q43 -61 53 -34 Q83 -27 63 -4 Q77 20 42 25 Q13 48 -10 27 Q-40 40 -61 8Z', PALE, GREEN, 1.5)
    for xx, yy in [(-48, -9), (-25, -30), (2, -33), (34, -20), (39, 9), (8, 19), (-27, 14)]:
        b += path(f'M{xx} {yy} q10 -13 20 -2 q-6 13 -20 2Z', '#DFE6D4', GREEN, .7)
        b += path(f'M{xx + 2} {yy} l13 -3', stroke=GREEN, width=.65)
    return group(x, y, b, scale)


def _forest_tree(x, y, h=300, lean=0):
    b = path('M-11 0 Q-5 -90 -14 -185 L-3 -255 L12 -248 Q8 -139 14 0Z', '#D8C5AC', MUTED, 1.8)
    b += path('M-3 0 Q7 -82 -5 -190 M6 -12 Q12 -92 1 -149', stroke=BROWN, width=.8)
    b += path('M-7 -128 Q-41 -146 -77 -196 M3 -192 Q30 -231 60 -254 M5 -158 Q44 -176 88 -198', stroke=BROWN, width=6)
    b += path('M-7 -128 Q-41 -146 -77 -196 M3 -192 Q30 -231 60 -254 M5 -158 Q44 -176 88 -198', stroke=GOLD, width=3)
    b += _leaves(-68, -213, .88) + _leaves(52, -261, .96) + _leaves(83, -186, .83) + _leaves(-8, -278, 1)
    b += path('M-11 0 L-35 9 M14 0 L37 7 M0 -6 L-15 12', stroke=BROWN, width=2)
    return group(x, y, b, h / 330, lean)


def _shelter(x, y, w=145, h=105, roof=GREEN):
    b = path(f'M{x} {y - h} H{x + w} V{y} H{x}Z', SAND, INK, 1.7)
    b += path(f'M{x - 9} {y - h} L{x + w * .38} {y - h - 28} L{x + w + 12} {y - h}Z', roof, INK, 1.7)
    b += path(f'M{x + w} {y - h} l25 -14 v{h} l-25 14Z', '#E0D0B9', INK, 1.5)
    b += rect(x + w * .36, y - h * .54, w * .23, h * .54, TERRA, INK, 1, 1.2)
    b += line(x + w * .47, y - h * .54, x + w * .47, y, MUTED, 1)
    for xx in [x + 12, x + w * .68]:
        b += rect(xx, y - h + 17, w * .19, h * .29, '#E7EFEB', INK, 1, 1)
        b += line(xx, y - h + 17 + h * .15, xx + w * .19, y - h + 17 + h * .15, MUTED, .8)
    for j in range(4):
        yy = y - 10 - j * 15
        b += path(f'M{x + 3} {yy} h15 M{x + w - 23} {yy - 4} h16', stroke=GOLD, width=.8)
    b += path(f'M{x + w * .29} {y} h{w * .36} l9 7 h{-w * .47}Z', '#E3DED3', MUTED, 1)
    return b


def _platform(x, y, w=160):
    b = path(f'M{x} {y} l{w * .16} -18 h{w * .79} l{w * .1} 18Z', PALE, INK, 1.7)
    b += path(f'M{x} {y} v10 h{w * 1.05} v-10 M{x + 15} {y + 10} v24 M{x + w - 4} {y + 10} v24', stroke=INK, width=2)
    b += path(f'M{x + 7} {y - 2} v-23 h{w * .23} M{x + 7} {y - 16} h{w * .23}', stroke=MUTED, width=1.5)
    for xx in [x + 17, x + 31, x + w - 7]:
        b += line(xx, y - 24, xx, y - 2, MUTED, 1.2)
    b += path(f'M{x + w * .39} {y - 4} h{w * .18} M{x + w * .69} {y - 8} h{w * .17}', stroke=GOLD, width=2)
    return b


def _elevator(x, top, bottom, w=75):
    b = rect(x, top, w, bottom - top, '#ECE8DD', INK, 1, 1.5)
    b += path(f'M{x + 13} {top + 8} V{bottom - 4} M{x + w - 13} {top + 8} V{bottom - 4}', stroke=MUTED, width=2)
    b += ellipse(x + w / 2, top + 15, 9, 9, GOLD, INK, 1)
    b += line(x + w / 2 - 7, top + 23, x + w / 2 - 7, bottom - 55, MUTED, 1)
    cabin_y = bottom - 99
    b += rect(x + 16, cabin_y, w - 32, 77, PALE, INK, 1, 1.3)
    b += path(f'M{x + 19} {cabin_y + 65} h{w - 38} M{x + w / 2} {cabin_y + 7} v50', stroke=MUTED, width=1)
    b += _figure(x + w / 2 - 1, cabin_y + 66, 57, shirt=TERRA, wing_scale=.3)
    for yy in range(int(top + 50), int(bottom - 110), 40):
        b += line(x, yy, x + w, yy, GOLD, 1)
    b += path(f'M{x - 8} {bottom} h{w + 16} M{x - 9} {top - 5} h{w + 18}', stroke=INK, width=2)
    return b


def _ferry(x, y, scale=1):
    b = path('M-103 -5 H114 L87 33 Q-2 45 -86 30Z', SAND, INK, 2)
    b += path('M-91 7 H101 M-76 22 H89', stroke=BROWN, width=1)
    b += rect(-65, -54, 130, 48, WHITE, INK, 2, 1.5)
    b += path('M-75 -56 H74 M-20 -54 V-80 H4 V-54 M-35 -81 H15', stroke=INK, width=2)
    for i in range(5):
        b += rect(-56 + i * 24, -44, 17, 22, '#E4ECEB', INK, 1, 1)
    for xx in [-82, 87]:
        b += ellipse(xx, -1, 5, 8, BLACK, INK, 1)
    b += path('M68 -8 V-36 H93 V-8 M75 -19 H90 M-93 -8 V-25 H-67', stroke=MUTED, width=1.6)
    b += path('M-116 45 q14 -5 29 0 t29 0 t29 0 t29 0 t29 0 t29 0 t29 0', stroke=BLUE, width=1.2)
    return group(x, y, b, scale)


def _train(x, y, scale=1):
    b = path('M0 -59 Q1 -78 22 -78 H98 L121 -54 V-7 H0Z', GREEN, INK, 1.8)
    b += rect(15, -66, 32, 29, PALE, INK, 2, 1.2) + path('M63 -67 H92 L108 -49 H63Z', PALE, INK, 1.2)
    b += path('M3 -20 H115 M55 -75 V-23 M8 -11 h102', stroke=MUTED, width=1.3)
    for i in range(2):
        xx = 135 + i * 123
        b += rect(xx, -62, 112, 52, SAND, INK, 1, 1.5)
        b += path(f'M{xx + 5} -56 h102 M{xx + 5} -21 h102', stroke=BROWN, width=1)
        for j in range(5):
            b += line(xx + 11 + j * 22, -55, xx + 11 + j * 22, -22, GOLD, 1.1)
        b += line(xx - 12, -16, xx, -16, INK, 3)
    for xx in [24, 97, 154, 226, 277, 348]:
        b += ellipse(xx, -6, 9, 9, BLACK, INK, 1) + ellipse(xx, -6, 3, 3, GREY)
    return group(x, y, b, scale)


def _rail(x, y, w):
    b = path(f'M{x} {y} h{w} M{x} {y + 10} h{w}', stroke=MUTED, width=2)
    for xx in range(int(x), int(x + w), 22):
        b += path(f'M{xx} {y - 4} l-3 19', stroke=BROWN, width=2)
    return b


def _silo(x, y, w=65, h=145):
    b = path(f'M{x} {y - h} Q{x + w / 2} {y - h - 32} {x + w} {y - h} V{y} Q{x + w / 2} {y + 13} {x} {y}Z', '#E2D8C5', INK, 1.6)
    b += ellipse(x + w / 2, y - h, w / 2, 9, SAND, INK, 1.2)
    for j in range(5):
        yy = y - h + 21 + j * (h - 25) / 5
        b += path(f'M{x} {yy} q{w / 2} 13 {w} 0', stroke=GOLD, width=.9)
    b += path(f'M{x + w - 17} {y - h + 9} V{y - 4} M{x + w - 9} {y - h + 9} V{y - 4}', stroke=MUTED, width=1)
    for yy in range(int(y - h + 15), int(y), 10):
        b += line(x + w - 17, yy, x + w - 9, yy, MUTED, .8)
    return b


def _gondola(x, y, scale=1):
    b = path('M-32 -5 Q-42 0 -34 35 H34 Q42 0 32 -5Z', TERRA, INK, 1.8)
    b += rect(-26, 2, 52, 19, PALE, INK, 2, 1.1)
    b += path('M0 -5 V-36 L-11 -45 H15 M-8 2 V21 M8 2 V21 M-28 28 H29', stroke=INK, width=1.2)
    b += ellipse(-9, -45, 4, 4, GREY, INK, 1) + ellipse(13, -45, 4, 4, GREY, INK, 1)
    return group(x, y, b, scale)


def _field(x, y, w=290, h=105):
    b = path(f'M{x} {y} l{w} -23 l-18 {h} l{-w + 4} 14Z', '#E8E5CE', GREEN, 1)
    for i in range(8):
        xx = x + 12 + i * (w - 25) / 8
        b += path(f'M{xx} {y + 1 - i * 2.8} l-18 {h - 10}', stroke=GOLD, width=1)
        for j in range(4):
            yy = y + 13 + j * 19 - i * 2.2
            b += path(f'M{xx - j * 3} {yy} l-3 -8 M{xx - j * 3} {yy - 3} l5 -5', stroke=GREEN, width=.85)
    return b


def _snow(x, y, scale=1):
    b = ''
    for a in range(0, 180, 60):
        rad = math.radians(a)
        dx, dy = 6 * math.cos(rad), 6 * math.sin(rad)
        b += line(-dx, -dy, dx, dy, BLUE, 1)
    return group(x, y, b, scale)


def _scene_wind():
    b = cloud(190, 86, 150) + cloud(695, 108, 110)
    b += path('M25 293 L138 177 L223 256 L318 153 L410 269 L514 197 L628 276 L780 171 L875 296', '#E7EBDD', LINE, 1.5)
    b += path('M25 344 Q117 305 198 311 L337 311 L401 367 H521 L588 292 H774 L868 368 V553 H25Z', '#E9DDC8', INK, 1.7)
    b += path('M51 367 l93 8 l38 50 M251 327 l-22 61 l41 27 M588 314 l-31 53 M790 339 l-23 53 l35 25', stroke=GOLD, width=1.2)
    b += _water(39, 503, 825, 55, 3)
    b += path('M329 313 L329 442 H430 V313Z', SAND, INK, 1.7)
    b += _shelter(581, 293, 124, 85) + _shelter(120, 312, 104, 72, TERRA)
    b += _platform(283, 311, 184) + _platform(560, 294, 177)
    b += _elevator(377, 303, 485, 63)
    b += path('M34 483 Q313 464 567 481 T867 482 M36 493 Q313 474 567 491 T867 492', stroke=MUTED, width=1.3)
    b += bus(112, 475, 153) + _figure(318, 480, 73, pose='walk', shirt=TERRA)
    b += _figure(328, 309, 80, shirt=GREEN, wing_scale=.45) + _figure(659, 289, 75, shirt=TERRA, wing_scale=.45)
    b += _figure(503, 230, 70, pose='glide', opened=True, wing_scale=.62)
    b += path('M742 286 V222 M734 222 H751 L778 232 L751 239Z', SAND, INK, 1.5)
    b += path('M751 222 V239 M763 226 V236', stroke=TERRA, width=2)
    b += curve_arrow('M273 156 Q424 103 560 150', (560, 150), .25, BLUE, 2, '7 6')
    b += _forest_tree(85, 460, 140) + _forest_tree(796, 480, 175)
    b += _rocks(63, 509, .6) + _rocks(758, 528, .5)
    for i in range(7):
        b += path(f'M{465 + i * 46} 447 q12 -5 20 1', stroke=GOLD, width=.8)
    return b


def _scene_tide():
    b = path('M31 255 L119 190 L183 255 L269 202 L334 294 L443 258 L577 297 L729 227 L869 298', PALE, LINE, 1.5)
    b += _water(31, 301, 838, 239, 9)
    b += path('M31 306 Q102 277 219 299 L285 347 Q202 388 136 464 L31 493Z', '#E7DDCA', INK, 1.7)
    b += path('M869 292 Q776 276 703 309 L639 343 Q706 404 778 444 L869 464Z', '#E7DDCA', INK, 1.7)
    b += _shelter(70, 310, 128, 98) + _shelter(739, 316, 97, 82, TERRA)
    b += _platform(178, 348, 119) + _platform(625, 345, 122)
    b += path('M186 370 L316 397 L311 412 L178 386Z', GOLD, INK, 1.7)
    for i in range(9):
        b += path(f'M{188 + i * 14} {372 + i * 2.9} l-4 14', stroke=BROWN, width=.9)
    b += path('M191 385 v38 M289 406 v35 M308 410 v31', stroke=BROWN, width=4)
    b += _ferry(460, 419, 1.1) + crate(221, 374, 38, 24) + crate(258, 387, 28, 20)
    b += _figure(174, 387, 66, pose='walk', shirt=TERRA, wing_scale=.42)
    b += _figure(250, 343, 63, shirt=GREEN, wing_scale=.4)
    b += _figure(705, 339, 66, shirt=TERRA, wing_scale=.4)
    b += _figure(262, 237, 59, pose='glide', opened=True, wing_scale=.52)
    b += curve_arrow('M167 189 Q244 151 313 195', (313, 195), .5, BLUE, 1.8, '5 6')
    b += _forest_tree(61, 371, 128) + _forest_tree(831, 409, 142)
    b += _rocks(117, 446, .8) + _rocks(763, 413, .65)
    b += path('M345 245 Q451 224 562 241 M374 269 Q490 249 645 267 M413 286 Q552 273 743 282', stroke=WHITE, width=18, opacity=.76)
    b += path('M340 239 Q463 219 586 240 M414 266 Q566 246 736 262', stroke=LINE, width=1, opacity=.75)
    b += bus(63, 481, 93)
    return b


def _scene_canopy():
    b = path('M29 342 Q148 287 269 326 T493 330 Q609 287 865 329 V544 H29Z', '#E9E5D5', LINE, 1.4)
    b += _water(33, 464, 313, 70, 4)
    b += _forest_tree(190, 442, 374, -4) + _forest_tree(680, 446, 372, 3)
    b += _forest_tree(277, 434, 265) + _forest_tree(773, 470, 275)
    b += _forest_tree(494, 357, 297)
    b += path('M142 222 Q214 205 287 212 M635 231 Q696 215 747 232', stroke=BROWN, width=11)
    b += path('M142 219 Q214 202 287 209 M635 228 Q696 212 747 229', stroke=GOLD, width=5)
    b += _platform(188, 221, 97) + _platform(606, 235, 110)
    b += _figure(244, 216, 65, wing_scale=.4) + _figure(662, 228, 65, shirt=TERRA, wing_scale=.4)
    b += _figure(400, 274, 62, pose='glide', opened=True, wing_scale=.5)
    b += curve_arrow('M294 277 Q378 306 467 264', (467, 264), -.4, BLUE, 1.6, '6 5')
    b += path('M166 285 l-8 32 M160 306 l-20 13 M733 269 l14 33 M744 292 l19 12', stroke=BROWN, width=3)
    b += _leaves(145, 318, .52) + _leaves(775, 307, .6)
    b += _shelter(551, 473, 140, 96, GOLD)
    b += _rail(356, 494, 441)
    b += rect(390, 465, 123, 10, PALE, INK, 1, 1.5)
    b += path('M394 475 H508 M395 466 V441 M507 465 V441', stroke=INK, width=2)
    for xx in [410, 494]:
        b += ellipse(xx, 484, 8, 8, BLACK, INK, 1) + ellipse(xx, 484, 3, 3, GREY)
    for i in range(5):
        yy = 416 + i * 10
        b += path(f'M396 {yy} H487 Q505 {yy + 4} 487 {yy + 9} H396Z', '#D8C5AC', BROWN, 1)
        b += ellipse(488, yy + 4.5, 6, 4, SAND, BROWN, 1)
        b += line(408, yy + 3, 477, yy + 3, GOLD, .8)
    b += path('M421 408 V461 M469 408 V461', stroke=BLACK, width=2)
    b += _figure(721, 491, 77, pose='walk', shirt=TERRA, wing_scale=.43)
    b += crate(600, 484, 45, 29) + _rocks(319, 513, .63)
    for x, y in [(80, 165), (327, 98), (557, 143), (797, 187), (603, 91)]:
        b += path(f'M{x} {y} q-6 13 -2 17 q9 -2 2 -17Z', '#CDDDE0', BLUE, .8)
    return b


def _scene_basin():
    b = cloud(224, 104, 163) + cloud(695, 110, 139)
    b += path('M31 289 Q99 214 183 269 Q297 211 373 277 Q540 241 659 276 Q776 231 868 279', PALE, LINE, 1.4)
    b += path('M31 301 Q455 264 868 293 V544 H31Z', '#ECE7D4', LINE, 1.2)
    b += _field(53, 333, 287, 99) + _field(340, 297, 277, 83)
    b += _water(43, 443, 313, 42, 3)
    b += path('M298 322 Q318 388 345 451 M305 321 Q325 384 351 449', stroke=BLUE, width=1.5)
    b += _silo(572, 423, 66, 140) + _silo(641, 423, 66, 153)
    b += _shelter(728, 428, 112, 107, GREY)
    b += path('M550 446 L573 425 H713 L735 447Z', PALE, INK, 1.2)
    b += _rail(31, 509, 837) + _train(338, 503, 1.06)
    b += _figure(281, 283, 68, pose='glide', opened=True, wing_scale=.6)
    b += curve_arrow('M175 243 Q225 227 274 233', (274, 233), .1, BLUE, 1.7, '5 5')
    b += _figure(324, 443, 78, pose='reach', shirt=TERRA, wing_scale=.38)
    b += path('M361 394 L378 390 L381 405 L366 407Z', PALE, INK, 1.3)
    b += line(365, 398, 376, 397, MUTED, .9)
    b += _figure(787, 479, 78, pose='walk', wing_scale=.4)
    b += crate(739, 446, 37, 26) + crate(777, 441, 40, 30)
    b += _forest_tree(97, 532, 154) + _forest_tree(836, 478, 121)
    b += _rocks(45, 533, .6)
    b += path('M451 195 q-8 -17 0 -32 M473 200 q-8 -19 0 -34', stroke=GOLD, width=1.5, dash='4 5')
    return b


def _scene_cliff():
    b = cloud(641, 112, 155)
    b += path('M31 271 L144 153 L233 260 L345 95 L461 249 L563 132 L685 259 L792 139 L868 242', '#E7E5DB', LINE, 1.5)
    b += path('M31 542 V345 L99 332 L161 259 H284 L325 338 L346 543Z', '#E3D7C5', INK, 1.8)
    b += path('M479 543 L514 389 L595 339 L626 282 H810 L868 367 V543Z', '#E3D7C5', INK, 1.8)
    b += path('M101 363 l23 40 l-21 32 M238 301 l-23 66 l41 54 M276 397 l-13 63 M595 371 l-16 49 l-33 25 M729 321 l-17 81 l32 44 M812 381 l-26 87', stroke=BROWN, width=1.1)
    b += _water(338, 500, 168, 44, 4)
    b += _shelter(177, 260, 100, 77, TERRA) + _shelter(665, 284, 124, 82, GREY)
    b += _platform(119, 261, 169) + _platform(602, 286, 191)
    b += path('M236 198 V252 M694 215 V280 M220 198 H253 M678 215 H711', stroke=INK, width=4)
    b += path('M227 195 Q438 216 703 213 M227 202 Q439 223 703 220', stroke=MUTED, width=2)
    b += _gondola(399, 252, .87) + _gondola(565, 258, .73)
    b += _figure(165, 258, 67, wing_scale=.4) + _figure(745, 279, 66, shirt=TERRA, wing_scale=.4)
    b += _figure(619, 284, 60, pose='walk', wing_scale=.38)
    b += crate(255, 240, 25, 18) + crate(767, 264, 29, 18)
    b += path('M47 498 Q160 478 245 496 L282 520 M735 498 Q804 482 859 499', stroke=MUTED, width=2)
    b += bus(64, 492, 108) + truck(728, 494, 102)
    b += _forest_tree(63, 391, 124, -8) + _forest_tree(808, 474, 131, 6)
    b += _rocks(303, 497, .64) + _rocks(548, 497, .62)
    b += curve_arrow('M417 141 C460 106 490 159 453 178 C423 192 415 173 433 160', (433, 160), -.9, BLUE, 1.8, '6 5')
    b += path('M322 363 Q377 327 441 342 M369 386 Q421 355 476 360', stroke=LINE, width=1.2, dash='5 7')
    return b


def _scene_frost():
    b = path('M31 290 L137 211 L246 279 L343 207 L443 282 L557 209 L647 285 L780 197 L868 292', '#E6E9E4', LINE, 1.5)
    b += path('M31 346 Q312 302 868 341 V544 H31Z', '#F0F0E9', LINE, 1.2)
    b += _water(47, 450, 177, 82, 3)
    b += path('M47 452 l28 -9 l29 12 l44 -7 l37 10 l39 -5 M88 470 l22 12 l-14 20 M181 474 l-24 15 l17 22', stroke=WHITE, width=3)
    b += _shelter(251, 390, 153, 129, GREY) + _shelter(653, 396, 163, 139, TERRA)
    b += _silo(177, 404, 59, 125)
    b += path('M240 258 Q312 250 365 260 L416 262 M641 251 Q739 240 829 255', stroke=WHITE, width=9)
    b += path('M399 327 H659 V396 H399Z', PALE, INK, 1.8)
    b += path('M399 327 L420 313 H644 L659 327 M409 389 H650', stroke=MUTED, width=1.4)
    for xx in [426, 477, 528, 579, 630]:
        b += path(f'M{xx} 332 V388 M{xx} 337 h31 v41 h-31Z', '#E2ECE9', MUTED, 1)
    b += _figure(447, 383, 61, pose='walk', shirt=TERRA, wing_scale=.35)
    b += _figure(606, 383, 61, shirt=GREEN, wing_scale=.35, elder=True)
    b += path('M31 472 Q457 453 868 472 M31 493 Q457 474 868 493', stroke=MUTED, width=1.5)
    b += bus(286, 476, 183) + truck(613, 478, 131)
    b += crate(563, 421, 37, 28) + crate(604, 428, 31, 22)
    b += _figure(523, 475, 79, pose='walk', shirt=TERRA, wing_scale=.36)
    b += _forest_tree(96, 421, 208) + _forest_tree(818, 424, 159)
    b += path('M54 292 Q87 280 125 290 M56 322 Q94 311 130 322 M799 324 Q839 310 868 325', stroke=WHITE, width=6)
    b += _rocks(205, 526, .63)
    for x, y in [(109, 106), (213, 154), (434, 136), (556, 97), (698, 174), (805, 117), (383, 219), (48, 201)]:
        b += _snow(x, y, 1)
    b += path('M107 519 Q180 507 253 518 M464 521 Q530 508 596 521 M746 520 Q802 509 857 519', stroke=LINE, width=1.1)
    return b


# 外形：大展翼背面与真正的收翼侧面，不以内部骨架替代已知功能。
_body = _figure(303, 530, 300, opened=True, back=True, wing_scale=.46)
_body += _profile(733, 525, 278)
_body += ground(47, 537, 535) + ground(636, 532, 208)
_body += path('M286 326 q-10 17 -4 31 M320 326 q10 17 4 31', stroke=BLUE, width=2, dash='4 4')
_body += pin(1, 56, 126, 239, 428) + pin(2, 529, 108, 463, 249)
_body += pin(3, 75, 562, 275, 509) + pin(4, 577, 370, 325, 343)
_body += pin(5, 841, 143, 815, 381)
DIAGRAMS['anatomy'] = make(
    'anatomy', '双手、独立羽翼与双腿', _body,
    '展翼背面与收翼侧面采用形制示例，不按比例。翼根只标功能联系，未知精细解剖不作定论。',
    [('独立双手', '前肢保留双手操作，手臂与羽翼分别可见。'),
     ('独立双翼', '中间肢对形成羽翼，展开羽面与手臂不是同一肢体。'),
     ('地面双腿', '后肢承担站立、步行与起降时的地面支撑。'),
     ('翼根功能', '翼带与手臂肩带邻接而独立，胸背共同支持承力。'),
     ('收翼余量', '羽片收拢后仍占背侧空间，衣物与设施需留活动余量。')],
    question='背面图中能分别找到两只手、两片羽翼和两条腿吗？')


# 羽被：外形、完整与断轴、绒羽和实际羽片色样分别留白。
_body = _quill(154, 140, 251, SAND, -9)
_body += _quill(351, 151, 241, SAND, 8, True)
_body += _down(570, 226, 1.8) + _down(679, 273, 1.1)
_body += _quill(734, 140, 113, GREY, 25)
_body += pin(1, 51, 86, 148, 269) + pin(2, 378, 87, 338, 254)
_body += pin(3, 552, 108, 570, 247)
for i, color in enumerate([GREY, WHITE, BROWN, BLACK, RUST]):
    xx = 175 + i * 135
    _body += _quill(xx, 439, 108, color, -12 + i * 6)
_body += pin(4, 70, 446, 175, 476)
_body += ground(91, 568, 720)
DIAGRAMS['plumage'] = make(
    'plumage', '羽片、绒羽与常见色样', _body,
    '羽片与色样是淡彩形制示例，不按比例。这里只观察外形和断轴，不规定未知微观结构或羽区名称。',
    [('完整羽片', '完整羽轴与左右羽面共同呈现羽片的可见外形。'),
     ('断轴对照', '断裂羽轴不能通过一次整理立即恢复原有完整状态。'),
     ('绒羽外观', '幼体小翼覆盖绒羽，但出生时不能承重飞行。'),
     ('既有翼色', '灰、白、褐、黑和赭色均是常见色系，颜色不表示人格或价值。')],
    question='完整与断裂两片羽毛的羽轴连续性有什么不同？')


_body = group(165, 231, _fan(1, SAND, True), 1.78)
_body += group(94, 312, _fold(-1), .75)
_body += _quill(625, 140, 170, SAND, 14, True)
_body += chair(696, 509, 1.08) + _figure(696, 509, 133, pose='sit', shirt=TERRA, wing_scale=.43)
_body += bus(482, 536, 133)
_body += _quill(119, 499, 53, SAND, -63) + _quill(200, 525, 46, PALE, 75)
_body += path('M296 454 L295 525 M276 527 Q296 512 324 525 L329 540 H273Z', SAND, INK, 1.7)
for i in range(8):
    _body += line(278 + i * 6, 529, 276 + i * 7, 542, BROWN, 1)
_body += ground(55, 553, 756)
_body += pin(1, 70, 80, 227, 253) + pin(2, 560, 80, 437, 180)
_body += pin(3, 785, 107, 603, 213) + pin(4, 840, 416, 714, 469)
_body += pin(5, 74, 442, 299, 528)
DIAGRAMS['molting'] = make(
    'molting', '错峰换羽与异常停飞', _body,
    '长短羽片交错是更新形制示例，不按比例，也不是换羽日程。正常更新保留羽面，右侧异常断轴另示收翼地面休息。',
    [('保留羽面', '正常换羽错峰进行，不会一次失去全部关键飞羽。'),
     ('不同更新状态', '长短与淡色羽片仅表示不同更新状态，不规定次序或时长。'),
     ('异常断轴', '羽轴断裂或意外大面积掉羽需要停飞与专业评估。'),
     ('地面接续', '收翼休息和使用公交不等于生活活动停止。'),
     ('落羽清扫', '自然落羽增加清扫与过滤需求，回收也受卫生和品质限制。')],
    question='左侧羽面保留了哪些羽片，右侧人物选择了什么地面活动？')


# 五个生活场景分两行，年龄只放在图外说明。
_body = _crib(153, 229, .97)
_body += _shelter(405, 249, 63, 49, GOLD)
_body += path('M464 257 L566 277 H804 V304 H461Z', '#E5EBD8', LINE, 1.2)
_body += path('M480 258 L572 280 M578 290 H803', stroke=GOLD, width=1.2)
_body += _figure(520, 258, 75, pose='glide', opened=True, wing_scale=.49)
_body += _figure(708, 279, 108, pose='reach', shirt=TERRA, wing_scale=.42)
_body += path('M501 275 Q520 283 541 278', stroke=LINE, width=1, dash='3 4')
_body += ground(424, 307, 401)
_body += _platform(40, 552, 226) + _figure(151, 475, 96, pose='glide', opened=True, wing_scale=.46)
_body += _figure(61, 544, 89, shirt=TERRA, wing_scale=.38)
_body += _figure(420, 544, 109, pose='walk', wing_scale=.44) + parcel(451, 477, 22)
_body += _platform(353, 550, 157) + _shelter(478, 550, 47, 82)
_body += bus(666, 543, 178) + _figure(610, 548, 98, pose='walk', shirt=TERRA, wing_scale=.37, elder=True)
_body += path('M611 476 L612 538 L622 538', stroke=BROWN, width=2)
_body += ground(566, 558, 288)
_body += pin(1, 62, 90, 142, 168) + pin(2, 797, 90, 534, 233)
_body += pin(3, 72, 350, 151, 430) + pin(4, 450, 344, 425, 489)
_body += pin(5, 789, 349, 759, 506)
DIAGRAMS['life'] = make(
    'life', '从幼翼照护到高龄接驳', _body,
    '五个生活场景采用形制示例，不按比例。两行观察带不表示人人同龄首飞，也不构成能力排名。',
    [('小翼襁褓', '出生至两岁已有小翼和绒羽，但不能承重飞行。'),
     ('低坡监督', '图中滑降人物对应六至九岁的监督近地练习；三至五岁只在低矮软地建立平衡。'),
     ('少年短飞', '十至十二岁仍需监督，多数人在十二至十五岁获得基本独立飞行能力。'),
     ('成年出行', '十七至二十岁骨骼、耐力与操控趋于成熟，成年仍可选择步行。'),
     ('高龄接驳', '高龄可出现耐力下降，公交与可靠地面设施持续支持社会参与。')],
    question='五个场景中，哪些活动依靠稳定地面和他人的监督或照护？')


_body = path('M44 352 H433 M48 355 V104 H431 M62 106 L190 82 H411', stroke=LINE, width=2)
_body += _crib(226, 319, 1.31)
_body += _figure(373, 366, 174, pose='care', shirt=TERRA, wing_scale=.39) + chair(373, 366, 1.43)
_body += desk(52, 401, 97) + cup(97, 351, .67)
_body += path('M174 373 h96 v15 h-96Z', PALE, LINE, 1)
_body += _pram(661, 415, .9)
_body += _figure(803, 445, 166, pose='push', shirt=GREEN, wing_scale=.39)
_body += ground(551, 452, 300)
_body += path('M48 474 Q337 468 450 477 M486 474 Q655 465 856 476', stroke=LINE, width=1.5)
_body += path('M512 532 Q665 501 844 534 L844 555 H511Z', '#E9EBD9', LINE, 1)
_body += _figure(578, 543, 62, shirt=GOLD, wing_scale=.35)
_body += _figure(700, 543, 104, shirt=TERRA, wing_scale=.38)
_body += pin(1, 70, 79, 168, 300) + pin(2, 438, 108, 371, 303)
_body += pin(3, 633, 114, 655, 394) + pin(4, 829, 513, 699, 527)
DIAGRAMS['reproduction'] = make(
    'reproduction', '留翼位的床与地面育幼', _body,
    '婴儿床、推车与低矮活动场均为形制示例，不按比例。画面只说明地面照护与留翼空间，不构成医疗或抱持教程。',
    [('床内留翼位', '婴幼儿的小翼不能承重，床内应避免挤压翼部。'),
     ('成人地面照护', '长期育幼依靠稳定地面活动，照护时不可提拽羽翼。'),
     ('推车留翼位', '推车为稳定地面移动提供空间，不能据此推定可抱幼儿飞行。'),
     ('低矮活动', '三至五岁活动使用低矮软地环境，不从开放高处试飞。')],
    question='床和推车的哪两处弧形留空围绕幼儿的小翼？')


_body = _figure(191, 382, 181, back=True, shirt=GREEN, wing_scale=.73)
_body += _figure(89, 387, 170, pose='reach', shirt=TERRA, wing_scale=.41)
_body += path('M139 267 Q158 260 168 275', stroke=SKIN, width=5)
_body += ground(46, 399, 257)
_body += _quill(430, 157, 180, SAND, -13)
_body += ellipse(430, 278, 37, 37, 'none', BLUE, 2)
_body += path('M454 306 l27 31', stroke=BROWN, width=5)
_body += _quill(494, 358, 106, SAND, 35)
_body += desk(351, 493, 205) + cup(383, 442, .64)
_body += path('M586 389 V166 H850 V391 M596 391 H849', stroke=LINE, width=2)
_body += rect(777, 185, 54, 57, PALE, INK, 3, 1.2)
for i in range(6):
    _body += line(785, 194 + i * 7, 824, 194 + i * 7, MUTED, 1)
_body += chair(695, 459, 1.45)
_body += _figure(695, 459, 181, pose='sit', opened=True, back=True, wing_scale=.29)
for j in range(3):
    _body += curve_arrow(f'M823 {275 + j * 34} Q790 {256 + j * 34} 756 {275 + j * 34}', (756, 275 + j * 34), 3, BLUE, 1.5, '5 5')
_body += ground(592, 475, 258)
_body += pin(1, 65, 112, 160, 273) + pin(2, 376, 91, 424, 274)
_body += pin(3, 829, 94, 805, 220) + pin(4, 776, 523, 712, 392)
DIAGRAMS['wing-care'] = make(
    'wing-care', '同意后的整羽与通风干羽', _body,
    '动作与设施是形制示例，不按比例，左侧表示已经征得同意后的协助。画面不提供医疗操作、干羽温度或卫生标准。',
    [('同意后协助', '帮助整理难以自行触及的背羽须先取得本人同意。'),
     ('观察羽面', '维护关注羽片排列与羽轴完整，不能仅凭颜色判断异常原因。'),
     ('通风干羽', '低温通风干羽设施需要电力与日常维护。'),
     ('维护边界', '舒适留翼空间支持维护，但整羽与干羽不等同于治愈损伤。')],
    question='协助整羽、羽面观察和通风干羽分别出现在画面的什么位置？')


# 六个功能复原草图：不用真实骨架、物种名称或必然进步箭头。
def _functional_body(x, y, scale=1, mode='water'):
    b = path('M-42 -13 Q-18 -32 18 -20 Q42 -7 22 14 Q-10 31 -42 10Z', PALE, MUTED, 1.5)
    b += ellipse(-44, -8, 15, 12, SAND, MUTED, 1.3)
    b += path('M-48 -11 q5 -2 8 0', stroke=MUTED, width=.8)
    if mode == 'water':
        limbs = ['M-28 -8 L-49 15 L-69 22', 'M-21 8 L-37 30 L-56 37',
                 'M-1 -10 L-9 22 L-25 36', 'M7 7 L13 31 L-2 40',
                 'M22 -7 L42 9 L44 30', 'M21 10 L32 29 L27 43']
    else:
        limbs = ['M-29 -9 L-53 -35 L-65 -52', 'M-23 9 L-43 -9 L-53 -28',
                 'M-2 -12 L6 -43 L29 -52', 'M6 8 L26 -6 L44 -27',
                 'M22 -4 L40 16 L56 18', 'M22 11 L28 37 L45 40']
    for d in limbs:
        b += path(d, stroke=MUTED, width=5) + path(d, stroke=GOLD, width=2)
    for hx, hy in ([(-69, 22), (-56, 37)] if mode == 'water' else [(-65, -52), (-53, -28)]):
        b += path(f'M{hx - 5} {hy} q5 -7 11 -1 M{hx - 3} {hy + 3} q5 -6 10 -1', stroke=MUTED, width=1)
    return group(x, y, b, scale)


_body = _water(37, 207, 255, 57, 4)
_body += _rocks(144, 266, .87) + _functional_body(164, 212, 1.13)
_body += ground(45, 271, 240)
_body += path('M386 275 Q406 198 395 107 M378 181 Q448 157 527 110 M400 229 Q448 205 538 213', stroke=BROWN, width=8)
_body += _leaves(392, 105, .53) + _leaves(544, 122, .56)
_body += group(453, 196, _functional_body(0, 0, .95, 'canopy'), 1, -28)
_body += path('M632 230 L684 183 L714 230 M759 277 Q813 251 861 268', stroke=GOLD, width=2)
_body += _figure(758, 217, 76, pose='glide', opened=True, wing_scale=.41)
_body += curve_arrow('M705 152 Q733 163 779 242', (779, 242), 1.1, BLUE, 1.5, '5 5')
_body += _rocks(681, 250, .85) + _leaves(837, 276, .4)
_body += _figure(161, 485, 105, pose='fly', opened=True, wing_scale=.43)
_body += path('M54 527 Q129 502 278 526', PALE, LINE, 1.2)
_body += curve_arrow('M62 412 Q60 433 78 449', (78, 449), .8, BLUE, 1.5)
_body += curve_arrow('M260 449 Q278 429 270 408', (270, 408), -1.9, BLUE, 1.5)
_body += _rocks(92, 544, .68)
_body += _figure(424, 547, 116, pose='work', shirt=GOLD, wing_scale=.38)
_body += path('M397 512 L493 501 L518 519 H400Z', '#E3DED3', INK, 1.5)
_body += path('M398 512 L399 539 M503 518 V540', stroke=BROWN, width=4)
_body += path('M458 491 L476 500 L470 510 L451 501Z', '#D8C5AC', MUTED, 1.2)
_body += path('M465 484 L475 510 M468 486 L487 491 L478 498Z', GREY, INK, 1.2)
_body += _quill(545, 517, 45, SAND, -63)
_body += _figure(727, 540, 114, pose='care', shirt=GREEN, wing_scale=.4)
_body += _baby(744, 480, .58)
_body += _rocks(782, 546, .85) + _leaves(688, 546, .53)
_body += ground(633, 562, 226)
for n, x, y, tx, ty in [(1, 53, 79, 149, 228), (2, 362, 76, 452, 180), (3, 644, 77, 757, 180),
                         (4, 57, 348, 166, 430), (5, 357, 347, 479, 501), (6, 653, 346, 744, 481)]:
    _body += pin(n, x, y, tx, ty)
DIAGRAMS['evolution'] = make(
    'evolution', '三对附肢的六种功能复原', _body,
    '六景仅为功能复原形制示例，不按比例，祖先轮廓没有化石外形依据。环境与动作不表示演化预先追求飞行，也不确定真实骨架。',
    [('浅水撑行', '约距今三点二亿年，三对附肢辅助浅水推进、撑行与转向。'),
     ('林冠抓握', '约距今一点四亿年，前肢抓握、后肢推进，中肢支撑与平衡。'),
     ('有羽滑降', '约距今八千万年，扩大覆盖结构帮助滑降时减速与转向。'),
     ('主动拍翼', '约距今四千五百万年，拍翼与承力、呼吸及肌肉协同变化。'),
     ('工具操作', '约距今八百万年的祖先继续保留双手，复杂觅食与工具使用持续重要。'),
     ('长期育幼', '距今二百万年以内的早期人类加强交流合作，育幼与知识传递不只依赖飞行。')],
    question='浅水、枝间、空中和稳定地面的动作分别利用了哪些附肢功能？')


_REGION_SCENES = {
    'region-wind': _scene_wind,
    'region-tide': _scene_tide,
    'region-canopy': _scene_canopy,
    'region-basin': _scene_basin,
    'region-cliff': _scene_cliff,
    'region-frost': _scene_frost,
}
_REGION_DETAILS = {
    'region-wind': (
        '台地平台与公共电梯',
        [('接地台地', '建筑和平台由台地或地面承重，云层不能供人站立。'),
         ('公共平台', '起降、候风与轻装通行需要可用平台及净空。'),
         ('公共电梯', '可见轿厢把上部平台与地面公交联系起来。'),
         ('风向变化', '山口和建筑附近的风场会改变实际通行条件。')],
        [(65, 125, 180, 346), (842, 164, 640, 291), (520, 398, 409, 423), (709, 63, 763, 233)],
        '能从电梯轿厢向上找到平台、向下找到地面公交吗？'),
    'region-tide': (
        '海湾船运、海雾与沿岸短飞',
        [('沿岸短飞', '合适天气下的沿岸短程连接仍需落点和返程安排。'),
         ('船运接续', '渡船、码头和地面集散承担人员与重货运输。'),
         ('海雾限制', '海雾与湿翼会改变个人通行，数字导航不能取消天气边界。'),
         ('水面无落点', '海面不能供人临时站立休息，跨海运输持续依赖机械载具。')],
        [(64, 87, 260, 206), (73, 551, 458, 419), (806, 78, 558, 249), (814, 548, 702, 487)],
        '短飞位于哪段沿岸空间，渡船与码头怎样衔接？'),
    'region-canopy': (
        '林冠净空与地面运材',
        [('枝叶边界', '多层林冠中的枝叶限制大翼展，不是处处可穿越。'),
         ('通行节点', '林冠节点之间需要可展开、转向与退出的净空。'),
         ('地面运材', '木材等重货由地面机械转运，不由轻装飞行者承担。'),
         ('高湿维护', '丰沛雨水和高湿增加羽面维护与干羽需求。')],
        [(69, 53, 162, 301), (603, 54, 412, 241), (820, 531, 475, 436), (856, 94, 798, 195)],
        '人物通行的开阔间隙与载材车辆所在的地面路线有何不同？'),
    'region-basin': (
        '平原巡视、铁路与粮仓',
        [('轻装巡视', '飞行补充田间观察和轻件联络，不代替翻土与运粮。'),
         ('地面生产', '耕地和灌溉仍依赖土壤、水源及地面劳动。'),
         ('粮仓储备', '粮仓与可靠运输在停飞期间继续维持生活供给。'),
         ('铁路重货', '铁路连接地面城市与批量粮食运输。')],
        [(80, 92, 280, 243), (60, 553, 328, 404), (807, 160, 651, 354), (845, 546, 573, 480)],
        '轻装巡视者、田间劳动者与货运列车各自承担什么任务？'),
    'region-cliff': (
        '稀疏坡台与索道接续',
        [('坡台落点', '山地台地稀疏，停留、补给与退出路线受到约束。'),
         ('索道运输', '索道承担可靠机械连接，不能用个人双翼替代所有运输。'),
         ('山口乱流', '高处空气变化和山口乱流使越高越适飞的推断不成立。'),
         ('谷底连接', '水源与地面应急、货运连接仍是坡台生活的基础。')],
        [(62, 85, 150, 262), (842, 87, 565, 256), (492, 65, 455, 158), (832, 542, 419, 515)],
        '两处坡台之间有哪些机械连接，谷底还保留了哪些地面设施？'),
    'region-frost': (
        '寒地廊道、储粮与机械通行',
        [('封闭廊道', '封闭公共廊道支持收翼步行及不同身体状态的日常参与。'),
         ('储粮供给', '长冬生活需要储粮与可靠运输，而非持续依赖个人飞行。'),
         ('机械接驳', '公交和货车承担不适飞季节的人员接驳与物资运输。'),
         ('冰雪边界', '冬季个人飞行稀少，羽翼仍需空间、保温和维护。')],
        [(462, 72, 489, 361), (237, 79, 207, 349), (824, 548, 667, 449), (62, 72, 125, 463)],
        '封闭廊道中的步行者与街面的公交、粮仓之间如何形成地面生活连接？'),
}

for _key, _draw in _REGION_SCENES.items():
    _title, _notes, _pins, _question = _REGION_DETAILS[_key]
    _body = _draw()
    for _n, (_x, _y, _tx, _ty) in enumerate(_pins, 1):
        _body += pin(_n, _x, _y, _tx, _ty)
    DIAGRAMS[_key] = make(
        _key, _title, _body,
        '景观、建筑和器物仅为形制示例，不按比例。不是地图，不确定地域方位、邻接、城名或动植物种类。',
        _notes, question=_question)


_body = ''
for i, (_key, _draw) in enumerate(_REGION_SCENES.items()):
    xx = 29 + (i % 3) * 293
    yy = 61 + (i // 3) * 264
    _body += group(xx, yy, _draw(), .296)
    _body += pin(i + 1, xx + 26, yy - 16, xx + 92, yy + 87)
DIAGRAMS['regions'] = make(
    'regions', '六类环境的生活缩览', _body,
    '六幅独立环境缩览均为形制示例，不按比例，不构成地域地图。每景同时观察山坡、水、树、接地建筑和交通，不规定位置或统一建筑传统。',
    [('温和台地', '台地公共平台与电梯、地面公交共同支持通行。'),
     ('湿润海湾', '沿岸短飞受到雾和湿翼约束，船运持续承担可靠连接。'),
     ('多层林冠', '枝叶限制展开净空，地面机械承担木材转运。'),
     ('广阔平原', '田间巡视补充地面生产，铁路和粮仓承担批量供给。'),
     ('山地坡台', '稀疏落点与山口乱流使索道和补给连接重要。'),
     ('寒冷长冬', '封闭廊道、储粮与机械接驳维持季节停飞时的生活。')],
    question='六景中各自能找到哪一种水体、接地建筑和交通对象？')


# 迁飞只使用无物种轮廓的抽象符号，避免填补未知动物名录。
_body = _forest_tree(127, 516, 291) + _forest_tree(264, 508, 203)
_body += path('M340 462 L345 277 Q445 253 551 277 L561 464Z', SAND, INK, 1.8)
_body += path('M345 277 Q445 263 551 277 M345 293 H551 M340 462 H561', stroke=MUTED, width=1.2)
for xx in [367, 408, 449, 490, 531]:
    _body += rect(xx, 310, 24, 86, '#E5EEEE', INK, 1, 1)
    _body += path(f'M{xx + 3} 324 l16 -9 M{xx + 4} 342 l16 -9 M{xx + 4} 375 l16 -9', stroke=WHITE, width=2)
    for yy in [352, 366, 380]:
        _body += line(xx + 4, yy, xx + 19, yy, GOLD, 1.5)
_body += rect(421, 414, 43, 48, TERRA, INK, 1, 1.2)
_body += _platform(334, 277, 207)
_body += _water(44, 526, 307, 47, 3)
_body += _shelter(663, 486, 137, 110, GREY)
_body += bus(618, 542, 159) + _figure(610, 499, 85, pose='walk', wing_scale=.4)
_body += _figure(741, 316, 78, pose='glide', opened=True, wing_scale=.54)
_body += curve_arrow('M634 245 Q744 233 824 276', (824, 276), .5, BLUE, 1.9, '6 6')
_body += path('M48 190 Q277 142 481 191 T849 189 M48 208 Q277 160 481 209 T849 207', stroke=GREEN, width=1.1, dash='6 7')
for i in range(10):
    xx = 86 + i * 75
    yy = 184 + 17 * math.sin(i * .8)
    _body += path(f'M{xx - 8} {yy + 4} L{xx} {yy - 4} L{xx + 8} {yy + 4}', stroke=GREEN, width=2)
_body += path('M577 488 V356 Q579 342 595 342 H624 M589 342 H631 L638 351 H586Z', BLACK, INK, 1.4)
_body += path('M591 353 L576 418 Q609 431 640 416 L628 353Z', '#F3E4BE', 'none', opacity=.55)
_body += ground(355, 554, 499)
_body += pin(1, 65, 78, 312, 181) + pin(2, 553, 74, 453, 357)
_body += pin(3, 840, 376, 617, 360) + pin(4, 807, 82, 755, 291)
DIAGRAMS['ecology'] = make(
    'ecology', '迁飞符号、玻璃与照明边界', _body,
    '建筑、玻璃可见处理和遮光灯具为形制示例，不按比例。迁飞只用抽象方向符号，不确定物种外形、真实路线或保育设计标准。',
    [('抽象迁飞', '方向符号表示需要保留的动物通道，不是人类优先使用的捷径。'),
     ('玻璃障碍', '玻璃外立面和透明障碍可能造成伤害，可见处理方式这里只作例示。'),
     ('照明干扰', '夜间照明需要限制不必要光照，图中灯具不代表统一标准。'),
     ('人类通行', '个人通行和地面设施应协调避开迁飞与栖地空间。')],
    question='抽象迁飞带与人类通行线是否分开，玻璃和灯光位于哪里？')


_body = _water(56, 352, 776, 93, 4)
_body += path('M48 302 Q153 281 278 308 L313 352 L56 360Z', '#E8DDC8', INK, 1.5)
_body += path('M523 354 Q566 308 699 298 L839 309 V361Z', '#E8DDC8', INK, 1.5)
_body += _platform(120, 307, 143) + _platform(578, 307, 165)
_body += _shelter(60, 303, 83, 67, GREEN) + _shelter(748, 308, 77, 62, TERRA)
_body += _figure(391, 268, 81, pose='glide', opened=True, wing_scale=.59)
_body += curve_arrow('M253 228 Q371 158 548 229', (548, 229), .45, BLUE, 1.8, '6 6')
_body += _forest_tree(92, 337, 112) + _forest_tree(799, 338, 122)
_body += _rocks(275, 346, .54) + _rocks(570, 348, .65)
_body += path('M48 539 Q117 497 226 511 L264 554 H48Z', '#E8DDC8', INK, 1.5)
_body += _water(264, 486, 575, 96, 5)
_body += _ferry(574, 513, .8) + crate(149, 516, 34, 24)
_body += _figure(219, 552, 67, shirt=TERRA, wing_scale=.4)
_body += path('M307 449 Q503 433 804 450 M338 467 Q559 451 832 467', stroke=LINE, width=1, dash='5 8')
_body += pin(1, 61, 100, 200, 306) + pin(2, 809, 100, 644, 306)
_body += pin(3, 95, 421, 740, 550) + pin(4, 805, 422, 567, 515)
DIAGRAMS['boundaries'] = make(
    'boundaries', '短河沟与远海无落点的对照', _body,
    '上下两景为通行条件对照与形制示例，不按比例，也不是地图。上方仅表示合适条件下的短障碍跨越，下方远海不据图宽推定距离。',
    [('短障碍起点', '短河沟的一侧有稳定出发场地，仍须确认身体与天气适宜。'),
     ('对岸落点', '可跨越短障碍需要可用落点及进近、制动空间。'),
     ('远海限制', '海面没有临时站立休息的落点，单段能力不能无限重复。'),
     ('机械跨海', '远海与跨洋运输依赖机械载具、补给及可靠接续。')],
    question='上景有哪些对岸落点，下景为什么不能照搬同一种个人跨越方式？')
