#!/usr/bin/env python3
"""CAFETO 21 og.png painter (1200x630, PIL, system fonts only — same toolchain as rind/
honey-bistro). Espresso band + cream type, crepe-stack + berries + matcha flat-vector
motif right, 21 disc in the wordmark. Tracked mono lines measured and asserted before
save (jeyas lesson: silent 4px clip on the share card is invisible without the guard)."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))

INK = (34, 26, 20)
CREAM = (243, 234, 214)
SOFT = (230, 214, 184)
CARAMEL = (201, 139, 74)
NUTELLA = (74, 44, 26)
BERRY = (163, 36, 63)
BERRY_DK = (113, 24, 46)
MATCHA = (111, 143, 79)
MATCHA_DK = (81, 107, 56)
CREPE = (227, 202, 147)
CREPE_DK = (211, 168, 107)

W, H = 1200, 630
MARGIN = 64
TEXT_W = W - MARGIN * 2

def serif(size, bold=True, italic=False):
    cands = []
    if bold:
        cands += ["/System/Library/Fonts/Supplemental/Iowan Old Style Bold.ttf",
                  "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf"]
    if italic:
        cands += ["/System/Library/Fonts/Supplemental/Iowan Old Style Italic.ttf",
                  "/System/Library/Fonts/Supplemental/Times New Roman Italic.ttf"]
    cands += ["/System/Library/Fonts/Supplemental/Iowan Old Style Roman.ttf",
              "/System/Library/Fonts/Supplemental/Times New Roman.ttf"]
    for c in cands:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except OSError:
                continue
    return ImageFont.load_default()

def mono(size):
    for c in ["/System/Library/Fonts/Menlo.ttc", "/System/Library/Fonts/Monaco.ttf"]:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except OSError:
                continue
    return ImageFont.load_default()

def tracked_width(draw, text, font, tracking):
    return sum(draw.textlength(ch, font=font) for ch in text) + tracking * max(0, len(text) - 1)

def draw_tracked(draw, x, y, text, font, tracking, fill):
    cur = x
    for ch in text:
        draw.text((cur, y), ch, font=font, fill=fill)
        cur += draw.textlength(ch, font=font) + tracking

img = Image.new("RGB", (W, H), INK)
d = ImageDraw.Draw(img)

# gradient band across the top (berry -> caramel -> matcha), same 8px signature as the site
seg = [(MARGIN + (TEXT_W * i / 100.0), BERRY_DK if i < 30 else (CARAMEL if i < 65 else MATCHA)) for i in range(0, 101)]
for i in range(100):
    d.line([(seg[i][0], 46), (seg[i + 1][0], 46)], fill=seg[i][1], width=10)

# crepe-stack motif (right side), flat vector
cx, cy = 960, 330
d.ellipse([cx - 150, cy - 128, cx + 150, cy + 172], fill=CREAM)  # plate
d.ellipse([cx - 116, cy + 26, cx + 116, cy + 70], fill=CREPE_DK, outline=NUTELLA, width=4)
d.ellipse([cx - 110, cy - 2, cx + 122, cy + 42], fill=CREPE, outline=NUTELLA, width=4)
d.ellipse([cx - 104, cy - 30, cx + 116, cy + 14], fill=(234, 217, 176), outline=NUTELLA, width=4)
d.polygon([(cx - 74, cy - 22), (cx - 4, cy - 78), (cx + 26, cy - 18)], fill=(240, 220, 171), outline=NUTELLA)
berries = [(-24, -120, BERRY, 26), (18, -104, BERRY_DK, 26), (58, -118, (194, 65, 107), 26), (-52, -96, (74, 93, 138), 22), (30, -74, (93, 74, 134), 22)]
for bx, by, col, r in berries:
    d.ellipse([cx + bx - r, cy + by - r, cx + bx + r, cy + by + r], fill=col)
# matcha cup
mx, my = cx + 96, cy + 108
d.ellipse([mx - 42, my - 42, mx + 42, my + 42], fill=MATCHA, outline=MATCHA_DK, width=5)
d.ellipse([mx - 27, my - 27, mx + 27, my + 27], fill=(147, 176, 109))

# text column (left)
f_kick = mono(24)
kick = "CREPERIA  ·  COFFEE  ·  DOWNTOWN TACOMA"
kw = tracked_width(d, kick, f_kick, 6)
assert kw <= TEXT_W - 260, "og guard: kicker too wide (%d)" % kw
draw_tracked(d, MARGIN, 92, kick, f_kick, 6, CARAMEL)

f_big = serif(168)
big = "Cafeto"
tw = d.textlength(big, font=f_big)
assert tw <= TEXT_W - 210, "og guard: Cafeto too wide (%d)" % tw
d.text((MARGIN, 140), big, font=f_big, fill=CREAM)
# the 21 disc, inline after the word
dr = 96
disc_x = MARGIN + tw + 34
d.ellipse([disc_x, 168, disc_x + dr * 2, 168 + dr * 2], fill=CARAMEL, outline=NUTELLA, width=6)
f_disc = mono(84)
dw = d.textlength("21", font=f_disc)
d.text((disc_x + dr - dw / 2, 168 + dr - 42), "21", font=f_disc, fill=INK)

f_sub = mono(26)
sub = "said “caf-ay-to.”"
assert d.textlength(sub, font=f_sub) <= TEXT_W - 260, "og guard: sub line"
d.text((MARGIN, 356), sub, font=f_sub, fill=SOFT)

f_addr = serif(42, bold=False, italic=True)
line1 = "Sweet & savory crepes, matcha and"
line2 = "horchata lattes — every day, 8 to 4."
y = 414
for text in (line1, line2):
    wpx = d.textlength(text, font=f_addr)
    assert wpx <= TEXT_W - 250, "og guard: line too wide (%d): %r" % (wpx, text)
    d.text((MARGIN, y), text, font=f_addr, fill=CREAM)
    y += 60

f_foot = mono(22)
foot1 = "1127 BROADWAY, SUITE 101  ·  TACOMA, WA 98402"
foot2 = "OPEN 8 A.M.–4 P.M. EVERY DAY"
w1 = tracked_width(d, foot1, f_foot, 4)
w2 = tracked_width(d, foot2, f_foot, 4)
assert w1 <= TEXT_W - 250 and w2 <= TEXT_W - 250, "og guard: foot lines (%d, %d)" % (w1, w2)
draw_tracked(d, MARGIN, 560, foot1, f_foot, 4, SOFT)
draw_tracked(d, MARGIN, 592, foot2, f_foot, 4, CARAMEL)

out = os.path.join(HERE, "public", "og.png")
os.makedirs(os.path.dirname(out), exist_ok=True)
img.save(out, "PNG", optimize=True)
sz = os.path.getsize(out)
print("og.png", sz, "bytes")
assert sz < 500_000, "og.png too heavy"
