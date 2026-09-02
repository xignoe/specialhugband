#!/usr/bin/env python3
"""draws every graphic on the site, pixel by pixel. run from the site folder: python3 make-gfx.py
outputs go to img/. rerun after changing a color or a word. safe to delete once you are happy."""
from PIL import Image, ImageDraw
import random

# ---------- a tiny 5x7 pixel font (lowercase only, on purpose) ----------
# rows 0-1 ascenders, rows 2-6 x-height, rows 7-8 descenders. '#' = pixel.
X = {  # x-height letters, 5 rows (2-6)
 'a': [".###.","....#",".####","#...#",".####"],
 'c': [".####","#....","#....","#....",".####"],
 'e': [".###.","#...#","#####","#....",".####"],
 'm': ["####.","#.#.#","#.#.#","#.#.#","#.#.#"],
 'n': ["#.##.","##..#","#...#","#...#","#...#"],
 'o': [".###.","#...#","#...#","#...#",".###."],
 'r': ["#.##.","##..#","#....","#....","#...."],
 's': [".####","#....",".###.","....#","####."],
 'u': ["#...#","#...#","#...#","#..##",".##.#"],
 'v': ["#...#","#...#","#...#",".#.#.","..#.."],
 'w': ["#...#","#...#","#.#.#","#.#.#",".#.#."],
 'x': ["#...#",".#.#.","..#..",".#.#.","#...#"],
 'z': ["#####","...#.","..#..",".#...","#####"],
 '-': [".....",".....","#####",".....","....."],
 '*': ["..#..",".###.","#####",".###.","..#.."],   # solid star
 '+': ["..#..",".#.#.","#...#",".#.#.","..#.."],   # hollow star
 '<': [".#.#.","#####","#####",".###.","..#.."],   # heart
 '=': [".....","#####",".....","#####","....."],
}
A = {  # ascender letters, 7 rows (0-6)
 'b': ["#....","#....","####.","#...#","#...#","#...#","####."],
 'd': ["....#","....#",".####","#...#","#...#","#...#",".####"],
 'f': ["..###",".#...","####.",".#...",".#...",".#...",".#..."],
 'h': ["#....","#....","#.##.","##..#","#...#","#...#","#...#"],
 'i': [".#...",".....","##...",".#...",".#...",".#...","###.."],
 'k': ["#....","#....","#..#.","#.#..","##...","#.#..","#..#."],
 'l': ["##...",".#...",".#...",".#...",".#...",".#...","..##."],
 't': [".#...",".#...","####.",".#...",".#...",".#..#","..##."],
 '0': [".###.","#...#","#..##","#.#.#","##..#","#...#",".###."],
 '1': ["..#..",".##..","..#..","..#..","..#..","..#..",".###."],
 '2': [".###.","#...#","....#","...#.","..#..",".#...","#####"],
 '3': ["####.","....#","....#",".###.","....#","....#","####."],
 '4': ["...#.","..##..",".#.#.","#..#.","#####","...#.","...#."],
 '5': ["#####","#....","####.","....#","....#","#...#",".###."],
 '6': [".###.","#....","#....","####.","#...#","#...#",".###."],
 '7': ["#####","....#","...#.","..#..",".#...",".#...",".#..."],
 '8': [".###.","#...#","#...#",".###.","#...#","#...#",".###."],
 '9': [".###.","#...#","#...#",".####","....#","....#",".###."],
 '!': ["#....","#....","#....","#....","#....",".....","#...."],
 "'": ["#....","#....",".....",".....",".....",".....","....."],
 '?': [".###.","#...#","....#","..##.","..#..",".....","..#.."],
 '/': ["....#","....#","...#.","..#..",".#...","#....","#...."],
 '$': ["..#..",".####","#.#..",".###.","..#.#","####.","..#.."],
 '&': [".##..","#..#.",".##..","##.#.","#..#.","#..##",".##.#"],
 '(': ["..#..",".#...","#....","#....","#....",".#...","..#.."],
 ')': ["#....",".#...","..#..","..#..","..#..",".#...","#...."],
 '@': [".###.","#...#","#.###","#.#.#","#.###","#....",".###."],
 '"': ["#.#..","#.#..",".....",".....",".....",".....","....."],
}
B = {  # marks that sit low
 '.': (6, ["#"]),
 ',': (6, ["#", "#"]),
 ':': (3, ["#", ".", ".", "#"]),
 ';': (3, ["#", ".", ".", "#", "#"]),
}
D = {  # descender letters, 7 rows (2-8)
 'g': [".####","#...#","#...#",".####","....#","#...#",".###."],
 'j': ["...#.",".....","..##.","...#.","...#.","...#.","#..#.",".##.."],  # rows 0-7, handled below
 'p': ["####.","#...#","#...#","####.","#....","#....","#...."],
 'q': [".####","#...#","#...#",".####","....#","....#","....#"],
 'y': ["#...#","#...#","#...#",".####","....#","#...#",".###."],
}

def glyph(ch):
    """returns a list of 9 rows (strings) for one character, trimmed to its width."""
    rows = ["....."] * 9
    if ch in X:
        rows[2:7] = [r.ljust(5, '.') for r in X[ch]]
    elif ch in A:
        rows[0:7] = [r.ljust(5, '.')[:5] for r in A[ch]]
    elif ch in D:
        g = D[ch]
        if ch == 'j':
            rows[0:8] = [r.ljust(5, '.') for r in g]
        else:
            rows[2:9] = [r.ljust(5, '.') for r in g]
    elif ch in B:
        top, g = B[ch]
        for i, r in enumerate(g):
            rows[top + i] = r.ljust(5, '.')
    elif ch == ' ':
        return ["..."] * 9
    else:
        return glyph('?')
    # trim empty columns left/right
    cols = [i for i in range(5) if any(r[i] == '#' for r in rows)]
    if not cols:
        return ["..."] * 9
    lo, hi = min(cols), max(cols)
    return [r[lo:hi + 1] for r in rows]

def text_size(s):
    w = sum(len(glyph(c)[0]) + 1 for c in s) - 1
    return w, 9

def draw_text(img, xy, s, fill, scale=1):
    """draw pixel text onto img (RGBA) at xy, scaled."""
    x0, y0 = xy
    px = img.load()
    x = x0
    for c in s:
        g = glyph(c)
        for ry, row in enumerate(g):
            for rx, v in enumerate(row):
                if v == '#':
                    for dy in range(scale):
                        for dx in range(scale):
                            X_, Y_ = x + rx * scale + dx, y0 + ry * scale + dy
                            if 0 <= X_ < img.width and 0 <= Y_ < img.height:
                                px[X_, Y_] = fill
        x += (len(g[0]) + 1) * scale

def text_image(s, fill, scale, shadow=None, pad=1):
    w, h = text_size(s)
    W, H = (w + pad * 2 + (1 if shadow else 0)) * scale, (h + pad * 2 + (1 if shadow else 0)) * scale
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if shadow:
        draw_text(im, ((pad + 1) * scale, (pad + 1) * scale), s, shadow, scale)
    draw_text(im, (pad * scale, pad * scale), s, fill, scale)
    return im

# ---------- palette ----------
NIGHT   = (18, 10, 31, 255)     # page background
STAR    = (255, 255, 255, 255)
LAV     = (200, 170, 255, 255)
INK     = (42, 23, 71, 255)     # dark purple text
PINK    = (214, 32, 150, 255)
GREEN   = (60, 140, 70, 255)
LIME    = (150, 230, 120, 255)
CREAM   = (246, 238, 255, 255)
YELLOW  = (255, 220, 60, 255)
BLACK   = (0, 0, 0, 255)
GREY    = (192, 192, 192, 255)

random.seed(9)

# ---------- background tile: night sky with pixel stars ----------
T = 128
bg = Image.new("RGBA", (T, T), NIGHT)
p = bg.load()
for _ in range(38):
    x, y = random.randrange(T), random.randrange(T)
    p[x, y] = random.choice([STAR, LAV, LAV, (120, 100, 170, 255)])
for _ in range(5):  # a few little crosses
    x, y = random.randrange(2, T - 2), random.randrange(2, T - 2)
    for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
        p[x + dx, y + dy] = LAV
    p[x, y] = STAR
bg.save("img/bg-stars.png", optimize=True)

# ---------- wordmark and headings ----------
text_image("special hug", INK, 6, shadow=PINK).save("img/wordmark.png", optimize=True)
for word in ["shows", "music", "merch", "about", "contact"]:
    text_image(f"* {word} *", INK, 3, shadow=LAV).save(f"img/h-{word}.png", optimize=True)

# ---------- the hero: latest release. change the title here when a new song drops. ----------
text_image("severance", INK, 4, shadow=PINK).save("img/h-severance.png", optimize=True)
a = text_image("new single out now!", (255, 255, 255, 255), 2, pad=1)
bgd = Image.new("RGBA", a.size, PINK); bgd.alpha_composite(a)
b = Image.new("RGBA", a.size, (236, 224, 255, 255))  # matches the hero box color in style.css
fr = [bgd.convert("RGB").quantize(8), b.convert("RGB").quantize(8)]
fr[0].save("img/outnow.gif", save_all=True, append_images=fr[1:], duration=[900, 300], loop=0)

# ---------- 88x31 buttons ----------
def button(label, fg, bg_, edge, fname, sub=None):
    im = Image.new("RGBA", (88, 31), bg_)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 87, 30], outline=edge)
    d.rectangle([1, 1, 86, 29], outline=(255, 255, 255, 90))
    if sub:
        w1, _ = text_size(label); w2, _ = text_size(sub)
        draw_text(im, ((88 - w1) // 2, 6), label, fg)
        draw_text(im, ((88 - w2) // 2, 16), sub, fg)
    else:
        w, _ = text_size(label)
        draw_text(im, ((88 - w) // 2, 11), label, fg)
    im.save(f"img/{fname}", optimize=True)

button("spotify",     (255,255,255,255), (25,110,60,255),   (10,60,30,255),  "btn-spotify.png")
button("apple music", (255,255,255,255), (170,40,120,255),  (90,20,60,255),  "btn-apple.png")
button("bandcamp",    (255,255,255,255), (30,120,150,255),  (15,60,80,255),  "btn-bandcamp.png")
button("youtube",     (255,255,255,255), (170,30,30,255),   (90,15,15,255),  "btn-youtube.png")
button("instagram",   (255,255,255,255), (120,50,160,255),  (60,25,80,255),  "btn-instagram.png")
button("tiktok",      (255,255,255,255), (20,20,30,255),    (0,0,0,255),     "btn-tiktok.png")
button("facebook",    (255,255,255,255), (50,80,170,255),   (25,40,90,255),  "btn-facebook.png")
button("best viewed", INK, GREY, (90,90,90,255), "btn-anybrowser.png", sub="in any browser")
button("special hug", INK, CREAM, INK, "btn-specialhug.png", sub="fairy grunge")

# ---------- the merch button, bevelled like a real 1999 button ----------
def big_button(label, fname, scale=2):
    t = text_image(label, INK, scale, pad=0)
    W, H = t.width + 28, t.height + 18
    im = Image.new("RGBA", (W, H), (221, 221, 221, 255))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W - 1, H - 1], outline=BLACK)
    d.line([1, 1, W - 2, 1], fill=(255, 255, 255, 255)); d.line([1, 1, 1, H - 2], fill=(255, 255, 255, 255))
    d.line([2, 2, W - 3, 2], fill=(255, 255, 255, 255)); d.line([2, 2, 2, H - 3], fill=(255, 255, 255, 255))
    d.line([1, H - 2, W - 2, H - 2], fill=(128, 128, 128, 255)); d.line([W - 2, 1, W - 2, H - 2], fill=(128, 128, 128, 255))
    d.line([2, H - 3, W - 3, H - 3], fill=(128, 128, 128, 255)); d.line([W - 3, 2, W - 3, H - 3], fill=(128, 128, 128, 255))
    im.alpha_composite(t, (14, 9))
    im.save(f"img/{fname}", optimize=True)
big_button("click here for merch", "btn-merch.png")

# ---------- animated sparkle (16x16, 4 frames) ----------
def sparkle_frame(size, phase):
    im = Image.new("RGBA", (16, 16), CREAM)
    px = im.load()
    c = 8
    col = [STAR, LAV, PINK, LAV][phase % 4]
    for i in range(-size, size + 1):
        px[c + i, c] = col; px[c, c + i] = col
    if size >= 3:
        for i in (-1, 1):
            px[c + i, c + i] = LAV; px[c + i, c - i] = LAV
    return im
frames = [sparkle_frame(s, i) for i, s in enumerate([1, 3, 5, 3])]
frames=[f.convert("RGB").quantize(16) for f in frames]
frames[0].save("img/sparkle.gif", save_all=True, append_images=frames[1:], duration=220, loop=0)

# ---------- divider bar (animated stars, 440x10, 3 frames) ----------
def divider_frame(k):
    im = Image.new("RGBA", (440, 10), CREAM)
    d = ImageDraw.Draw(im)
    d.line([0, 5, 439, 5], fill=LAV)
    for i in range(22):
        x = 10 + i * 20 + ((i + k) % 3 - 1) * 2
        col = [STAR, PINK, LAV][(i + k) % 3]
        d.point((x, 5), fill=col); d.point((x - 1, 5), fill=col); d.point((x + 1, 5), fill=col)
        d.point((x, 4), fill=col); d.point((x, 6), fill=col)
        if (i + k) % 3 == 0:
            d.point((x, 3), fill=col); d.point((x, 7), fill=col); d.point((x - 2, 5), fill=col); d.point((x + 2, 5), fill=col)
    return im
frames = [divider_frame(k) for k in range(3)]
frames=[f.convert("RGB").quantize(16) for f in frames]
frames[0].save("img/divider.gif", save_all=True, append_images=frames[1:], duration=350, loop=0)

# ---------- "new!" blinking badge (2 frames, scaled x2) ----------
a = text_image("new!", (255, 255, 255, 255), 2, pad=1)
bgd = Image.new("RGBA", a.size, PINK); bgd.alpha_composite(a)
b = Image.new("RGBA", a.size, CREAM)
fr=[bgd.convert("RGB").quantize(8), b.convert("RGB").quantize(8)]
fr[0].save("img/new.gif", save_all=True, append_images=fr[1:], duration=[700, 350], loop=0)

# ---------- under construction (striped, 2 frames) ----------
def construction_frame(shift):
    W, H = 180, 26
    im = Image.new("RGBA", (W, H), YELLOW)
    d = ImageDraw.Draw(im)
    for x in range(-H, W + H, 12):
        d.polygon([(x + shift, 0), (x + 6 + shift, 0), (x + 6 - H + shift, H), (x - H + shift, H)], fill=BLACK)
    inner = Image.new("RGBA", (W - 8, H - 8), YELLOW)
    im.alpha_composite(inner, (4, 4))
    t = text_image("under construction", BLACK, 1, pad=0)
    im.alpha_composite(t, ((W - t.width) // 2, (H - t.height) // 2))
    return im
frames = [construction_frame(0).convert("RGB").quantize(8), construction_frame(6).convert("RGB").quantize(8)]
frames[0].save("img/construction.gif", save_all=True, append_images=frames[1:], duration=500, loop=0)

# ---------- hit counter (odometer digits) ----------
def counter(s):
    cell_w, cell_h = 11, 15
    im = Image.new("RGBA", (cell_w * len(s) + 2, cell_h + 2), (60, 60, 60, 255))
    d = ImageDraw.Draw(im)
    for i, ch in enumerate(s):
        x = 1 + i * cell_w
        d.rectangle([x, 1, x + cell_w - 2, cell_h], fill=BLACK)
        draw_text(im, (x + 3, 4), ch, LIME)
    return im
counter("00000001").save("img/counter.png", optimize=True)

# ---------- small bits ----------
bullet = Image.new("RGBA", (5, 5), (0, 0, 0, 0)); px = bullet.load()
for y, row in enumerate(X['*']):
    for x, v in enumerate(row):
        if v == '#': px[x, y] = PINK
bullet.save("img/bullet.png", optimize=True)

env = Image.new("RGBA", (16, 11), (0, 0, 0, 0)); d = ImageDraw.Draw(env)
d.rectangle([0, 0, 15, 10], fill=CREAM, outline=INK)
d.line([0, 0, 7, 6], fill=INK); d.line([15, 0, 8, 6], fill=INK)
d.line([0, 10, 5, 5], fill=INK); d.line([15, 10, 10, 5], fill=INK)
env.save("img/email.png", optimize=True)

print("drew everything into img/")
