"""Front Porch Suppers logo kit. Text is converted to outlines so it looks the same everywhere.
Fonts: Lora (OFL), Inter (OFL)."""
import os, re
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)
TEAL, CHERRY, CREAM, INK, BUTTER = "#1f4e79", "#c98a1b", "#fffdf7", "#1f2933", "#ffd77a"

lora = instantiateVariableFont(TTFont("/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"), {"wght": 700})
inter = TTFont("/usr/share/fonts/opentype/inter/Inter-Bold.otf")


class Font:
    def __init__(self, tt):
        self.gs, self.cmap, self.hmtx, self.upm = tt.getGlyphSet(), tt.getBestCmap(), tt["hmtx"], tt["head"].unitsPerEm

    def text(self, s, x, y, size, tracking=0.0):
        sc, pen, cx = size / self.upm, SVGPathPen(self.gs), x
        for ch in s:
            name = self.cmap[ord(ch)]
            self.gs[name].draw(TransformPen(pen, (sc, 0, 0, -sc, cx, y)))
            cx += self.hmtx[name][0] * sc + tracking * size
        return pen.getCommands(), cx - x - tracking * size


LORA, INTER = Font(lora), Font(inter)


def mark(card=CREAM, edge=TEAL, line=CHERRY, faint=TEAL, heart=CHERRY):
    """A little house with a front porch: roof, porch posts, a warm door and steps."""
    return f'''
  <path d="M8 44 L48 12 L88 44" fill="none" stroke="{edge}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M18 38 V74 H78 V38" fill="{card}" stroke="{edge}" stroke-width="5" stroke-linejoin="round"/>
  <rect x="12" y="50" width="72" height="7" rx="2" fill="{edge}"/>
  <path d="M19 57 V74 M77 57 V74" stroke="{edge}" stroke-width="5" stroke-linecap="round"/>
  <rect x="40" y="58" width="16" height="16" rx="2" fill="{heart}"/>
  <circle cx="48" cy="40" r="5.5" fill="{heart}"/>
  <path d="M30 80 H66 M24 87 H72" stroke="{edge}" stroke-width="5" stroke-linecap="round"/>'''


def lockup(word=INK, small=CHERRY, card=CREAM, edge=TEAL):
    top_d, top_w = LORA.text("Front Porch", 106, 56, 42)
    main_d, main_w = INTER.text("SUPPERS", 109, 84, 17, tracking=0.42)
    W = int(106 + max(top_w, main_w) + 8)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 100" width="{W * 3}" height="300">'
            f'<g transform="translate(4 2)">{mark(card=card, edge=edge)}</g>'
            f'<path d="{top_d}" fill="{word}"/><path d="{main_d}" fill="{small}"/></svg>'), W


def icon(bg=CREAM, rx=22):
    back = f'<rect width="100" height="100" rx="{rx}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">{back}<g transform="translate(1 3) scale(.98)">{mark()}</g></svg>'


logo, W = lockup()
open(os.path.join(OUT, "front-porch-suppers-logo.svg"), "w").write(logo)
open(os.path.join(OUT, "front-porch-suppers-logo-white.svg"), "w").write(lockup(word="#ffffff", small=BUTTER, card="#1d242d", edge="#8fbbe6")[0])
open(os.path.join(OUT, "front-porch-suppers-icon.svg"), "w").write(icon())
open(os.path.join(OUT, "front-porch-suppers-icon-square.svg"), "w").write(icon(rx=0))
print("width", W)
