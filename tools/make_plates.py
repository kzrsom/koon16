import math, os, random

OUT = "/site/assets/plates"
os.makedirs(OUT, exist_ok=True)

GOLD = "#c9a227"
AMBER = "#ffb866"
ORANGE = "#ff8000"

def head(w=1200, h=900, bg1="#0a2028", bg2="#04141a", seed=3):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice" role="img">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{bg1}"/><stop offset="1" stop-color="{bg2}"/>
  </linearGradient>
  <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{AMBER}" stop-opacity=".85"/>
    <stop offset="1" stop-color="{AMBER}" stop-opacity=".05"/>
  </linearGradient>
  <radialGradient id="glow" cx=".72" cy=".18" r=".7">
    <stop offset="0" stop-color="{ORANGE}" stop-opacity=".42"/>
    <stop offset="1" stop-color="{ORANGE}" stop-opacity="0"/>
  </radialGradient>
  <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2"/><feColorMatrix type="saturate" values="0"/></filter>
</defs>
<rect width="{w}" height="{h}" fill="url(#bg)"/>
<rect width="{w}" height="{h}" fill="url(#glow)"/>
'''

def grid(w, h, step=48, op=".10"):
    out = [f'<g stroke="{GOLD}" stroke-opacity="{op}" stroke-width="1">']
    x = step
    while x < w:
        out.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}"/>'); x += step
    y = step
    while y < h:
        out.append(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}"/>'); y += step
    out.append('</g>')
    return "\n".join(out)

def tail(w, h):
    return f'<rect width="{w}" height="{h}" filter="url(#grain)" opacity=".12"/>\n</svg>'


def coast():
    w, h = 1200, 900
    s = [head(w, h, "#0c2a33", "#04141a")]
    s.append(grid(w, h, 60, ".07"))
    s.append(f'<circle cx="880" cy="230" r="120" fill="none" stroke="{AMBER}" stroke-opacity=".55" stroke-width="1.5"/>')
    s.append(f'<circle cx="880" cy="230" r="76" fill="{ORANGE}" fill-opacity=".22"/>')
    s.append(f'<circle cx="880" cy="230" r="76" fill="none" stroke="{AMBER}" stroke-opacity=".8"/>')
    random.seed(11)
    for i in range(26):
        y0 = 430 + i * 20
        amp = 10 + i * 1.6
        pts = []
        for x in range(0, w + 1, 20):
            yy = y0 + math.sin(x / (150 + i * 3) + i * .6) * amp + math.sin(x / 47 + i) * 2.2
            pts.append(f"{x},{yy:.1f}")
        op = .5 - i * .014
        col = ORANGE if i in (6, 7) else GOLD
        s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-opacity="{max(op,0.08):.2f}" stroke-width="{1.6 if i<9 else 1}"/>')
    s.append(tail(w, h))
    return "\n".join(s)


def delta():
    w, h = 1200, 900
    s = [head(w, h, "#0b2530", "#03121a")]
    s.append(grid(w, h, 75, ".06"))
    random.seed(5)
    # river mouth branching upward
    def branch(x, y, ang, length, depth, width):
        if depth == 0 or length < 14:
            return
        x2 = x + math.cos(ang) * length
        y2 = y + math.sin(ang) * length
        s.append(f'<path d="M{x:.1f},{y:.1f} Q{(x+x2)/2 + math.sin(ang*3)*8:.1f},{(y+y2)/2:.1f} {x2:.1f},{y2:.1f}" fill="none" stroke="{AMBER}" stroke-opacity="{.16 + depth*.09:.2f}" stroke-width="{width:.1f}" stroke-linecap="round"/>')
        branch(x2, y2, ang - .42 - random.random() * .16, length * .76, depth - 1, width * .72)
        branch(x2, y2, ang + .38 + random.random() * .16, length * .74, depth - 1, width * .7)
    branch(560, 900, -math.pi / 2 + .05, 150, 6, 6)
    branch(360, 900, -math.pi / 2 - .35, 110, 5, 3.4)
    branch(820, 900, -math.pi / 2 + .42, 120, 5, 3.6)
    for i in range(9):
        y = 900 - i * 26
        s.append(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="{GOLD}" stroke-opacity=".12" stroke-width="1"/>')
    s.append(f'<rect x="0" y="0" width="{w}" height="{h}" fill="url(#glow)"/>')
    s.append(tail(w, h))
    return "\n".join(s)


def columns():
    w, h = 1200, 900
    s = [head(w, h, "#0a1f2b", "#04141a")]
    s.append(grid(w, h, 60, ".08"))
    n = 7
    for i in range(n):
        x = 120 + i * 140
        s.append(f'<rect x="{x}" y="240" width="72" height="440" fill="{GOLD}" fill-opacity=".10" stroke="{GOLD}" stroke-opacity=".5"/>')
        s.append(f'<rect x="{x-14}" y="216" width="100" height="22" fill="none" stroke="{AMBER}" stroke-opacity=".55"/>')
        s.append(f'<rect x="{x-18}" y="680" width="108" height="26" fill="none" stroke="{AMBER}" stroke-opacity=".4"/>')
        for k in range(6):
            s.append(f'<line x1="{x+10+k*10}" y1="240" x2="{x+10+k*10}" y2="680" stroke="{GOLD}" stroke-opacity=".16"/>')
    s.append(f'<path d="M40 770 Q600 700 1160 770" fill="none" stroke="{ORANGE}" stroke-opacity=".5" stroke-width="1.4"/>')
    s.append(f'<path d="M40 806 Q600 736 1160 806" fill="none" stroke="{ORANGE}" stroke-opacity=".25" stroke-width="1"/>')
    s.append(tail(w, h))
    return "\n".join(s)


def ledger():
    w, h = 1200, 900
    s = [head(w, h, "#0d2730", "#05161c")]
    s.append(f'<rect x="90" y="70" width="1020" height="760" fill="#0a2129" stroke="{GOLD}" stroke-opacity=".35"/>')
    random.seed(9)
    row = 0
    for y in range(140, 800, 46):
        s.append(f'<line x1="120" y1="{y}" x2="1080" y2="{y}" stroke="{GOLD}" stroke-opacity=".16"/>')
        if row % 3 == 0:
            s.append(f'<rect x="130" y="{y-24}" width="{random.randint(120,220)}" height="8" fill="{AMBER}" fill-opacity=".35"/>')
        else:
            s.append(f'<rect x="130" y="{y-24}" width="{random.randint(160,300)}" height="8" fill="{GOLD}" fill-opacity=".2"/>')
        for c in range(3):
            s.append(f'<line x1="{420+c*220}" y1="{y-40}" x2="{420+c*220}" y2="{y}" stroke="{GOLD}" stroke-opacity=".22"/>')
        if row in (2, 5, 9):
            s.append(f'<rect x="640" y="{y-28}" width="{random.randint(140,300)}" height="14" fill="{ORANGE}" fill-opacity=".5"/>')
        row += 1
    s.append(f'<rect x="90" y="70" width="1020" height="48" fill="{GOLD}" fill-opacity=".10"/>')
    s.append(tail(w, h))
    return "\n".join(s)


def portrait():
    w, h = 1200, 900
    s = [head(w, h, "#0b222c", "#03121a")]
    s.append(grid(w, h, 44, ".06"))
    cx, cy = 600, 520
    # head + shoulders silhouette
    s.append(f'<path d="M{cx-150} 900 q10 -210 150 -250 q140 40 150 250 z" fill="{GOLD}" fill-opacity=".10" stroke="{GOLD}" stroke-opacity=".4"/>')
    s.append(f'<path d="M{cx-104} 430 q0 -150 104 -150 q104 0 104 150 q0 120 -104 160 q-104 -40 -104 -160 z" fill="{GOLD}" fill-opacity=".14" stroke="{AMBER}" stroke-opacity=".45"/>')
    # halftone arc
    for r in range(190, 470, 26):
        s.append(f'<circle cx="{cx}" cy="{cy-40}" r="{r}" fill="none" stroke="{AMBER}" stroke-opacity="{max(.42 - r/1400, .07):.2f}"/>')
    for i in range(14):
        y = 160 + i * 44
        s.append(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="{ORANGE}" stroke-opacity=".06"/>')
    s.append(f'<rect x="60" y="60" width="200" height="3" fill="{ORANGE}" fill-opacity=".8"/>')
    s.append(tail(w, h))
    return "\n".join(s)


def contour():
    w, h = 1200, 900
    s = [head(w, h, "#0c2a33", "#04141a")]
    cx, cy = 520, 470
    random.seed(4)
    for i in range(18):
        base = 40 + i * 26
        pts = []
        for a in range(0, 361, 12):
            rad = math.radians(a)
            rr = base * (1 + 0.16 * math.sin(a / 43 + i * .5) + 0.09 * math.sin(a / 21 + i))
            pts.append(f"{cx + math.cos(rad)*rr*1.18:.1f},{cy + math.sin(rad)*rr*.86:.1f}")
        s.append(f'<polygon points="{" ".join(pts)}" fill="none" stroke="{GOLD}" stroke-opacity="{max(.5-i*.022,.08):.2f}" stroke-width="{1.4 if i%4==0 else .9}"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="8" fill="{ORANGE}"/>')
    s.append(f'<line x1="{cx}" y1="0" x2="{cx}" y2="{h}" stroke="{AMBER}" stroke-opacity=".14" stroke-dasharray="6 8"/>')
    s.append(f'<line x1="0" y1="{cy}" x2="{w}" y2="{cy}" stroke="{AMBER}" stroke-opacity=".14" stroke-dasharray="6 8"/>')
    s.append(tail(w, h))
    return "\n".join(s)


def mapgrid():
    w, h = 1200, 900
    s = [head(w, h, "#0a2028", "#03121a")]
    s.append(grid(w, h, 60, ".13"))
    nodes = [(300, 300), (520, 250), (760, 340), (860, 560), (600, 610), (380, 520), (250, 700), (980, 720)]
    routes = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(4,6),(3,7),(6,1)]
    for a,b in routes:
        s.append(f'<line x1="{nodes[a][0]}" y1="{nodes[a][1]}" x2="{nodes[b][0]}" y2="{nodes[b][1]}" stroke="{AMBER}" stroke-opacity=".35" stroke-dasharray="7 6"/>')
    for i,(x,y) in enumerate(nodes):
        s.append(f'<circle cx="{x}" cy="{y}" r="{11 if i%3 else 16}" fill="{ORANGE if i%3==0 else "#0a2028"}" fill-opacity=".9" stroke="{AMBER}" stroke-opacity=".85"/>')
    s.append(f'<rect x="0" y="640" width="{w}" height="260" fill="#03121a" fill-opacity=".55"/>')
    for i in range(6):
        s.append(f'<path d="M{i*70} 900 q60 -90 40 -150" fill="none" stroke="{GOLD}" stroke-opacity=".18"/>')
    s.append(tail(w, h))
    return "\n".join(s)


def weave():
    w, h = 1200, 900
    s = [head(w, h, "#0d2730", "#04141a")]
    step = 34
    for i in range(-h, w, step):
        s.append(f'<line x1="{i}" y1="0" x2="{i+h}" y2="{h}" stroke="{GOLD}" stroke-opacity=".22" stroke-width="3"/>')
        s.append(f'<line x1="{i}" y1="{h}" x2="{i+h}" y2="0" stroke="{AMBER}" stroke-opacity=".13" stroke-width="2"/>')
    s.append(f'<rect x="140" y="200" width="920" height="500" fill="#04141a" fill-opacity=".72" stroke="{AMBER}" stroke-opacity=".5"/>')
    for i in range(5):
        s.append(f'<rect x="{190+i*180}" y="300" width="120" height="120" fill="{ORANGE}" fill-opacity=".18" stroke="{GOLD}" stroke-opacity=".5"/>')
    s.append(f'<line x1="190" y1="500" x2="1010" y2="500" stroke="{AMBER}" stroke-opacity=".4"/>')
    s.append(f'<line x1="190" y1="560" x2="890" y2="560" stroke="{AMBER}" stroke-opacity=".25"/>')
    s.append(f'<line x1="190" y1="610" x2="720" y2="610" stroke="{AMBER}" stroke-opacity=".18"/>')
    s.append(tail(w, h))
    return "\n".join(s)


plates = {
    "coast.svg": coast, "delta.svg": delta, "columns.svg": columns, "ledger.svg": ledger,
    "portrait.svg": portrait, "contour.svg": contour, "mapgrid.svg": mapgrid, "weave.svg": weave,
}
for name, fn in plates.items():
    with open(os.path.join(OUT, name), "w") as f:
        f.write(fn())
print("plates:", sorted(os.listdir(OUT)))
