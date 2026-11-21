import os, contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    from make_logo import LORA, INTER, mark, lockup, INK, CHERRY, CREAM
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gdn")
n_d, n_w = LORA.text("Front Porch", 0, 0, 29)
k_d, k_w = INTER.text("SUPPERS", 0, 0, 11.5, tracking=0.42)
def square(bg):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200"><rect width="200" height="200" fill="{bg}"/>'
            f'<g transform="translate(66 26) scale(.72)">{mark()}</g>'
            f'<path transform="translate({(200-n_w)/2:.2f} 136)" d="{n_d}" fill="{INK}"/>'
            f'<path transform="translate({(200-k_w)/2:.2f} 160)" d="{k_d}" fill="{CHERRY}"/></svg>')
lg, W = lockup()
inner = lg[lg.index(">") + 1: lg.rindex("</svg>")]
def land(bg):
    s = 2.4; w = W * s
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300"><rect width="1200" height="300" fill="{bg}"/>'
            f'<g transform="translate({(1200-w)/2:.1f} {(300-100*s)/2:.1f}) scale({s})">{inner}</g></svg>')
for tag, bg in (("white", "#ffffff"), ("cream", CREAM)):
    open(f"{D}/square-{tag}.svg", "w").write(square(bg)); open(f"{D}/landscape-{tag}.svg", "w").write(land(bg))
