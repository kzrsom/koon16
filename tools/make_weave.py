import math
W,H=1200,780
s=[f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" preserveAspectRatio="xMidYMid slice" role="img">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d2a33"/><stop offset="1" stop-color="#04141a"/></linearGradient>
  <radialGradient id="glow" cx=".5" cy=".45" r=".65"><stop offset="0" stop-color="#ff8000" stop-opacity=".22"/><stop offset="1" stop-color="#ff8000" stop-opacity="0"/></radialGradient>
  <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2"/><feColorMatrix type="saturate" values="0"/></filter>
</defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<rect width="{W}" height="{H}" fill="url(#glow)"/>
''']
# subtle diagonal weave
for i in range(-H, W, 26):
    s.append(f'<line x1="{i}" y1="0" x2="{i+H}" y2="{H}" stroke="#c9a227" stroke-opacity=".07" stroke-width="2"/>')
    s.append(f'<line x1="{i}" y1="{H}" x2="{i+H}" y2="0" stroke="#ffb866" stroke-opacity=".05" stroke-width="1.5"/>')

cy=H/2
# repeated diamond band
for k in range(-6, 7):
    cx=W/2 + k*96
    r=30
    pts=f"{cx},{cy-r} {cx+r},{cy} {cx},{cy+r} {cx-r},{cy}"
    s.append(f'<polygon points="{pts}" fill="none" stroke="#ffb866" stroke-opacity=".55" stroke-width="1.6"/>')
    if k%2==0:
        s.append(f'<polygon points="{cx},{cy-r*0.5} {cx+r*0.5},{cy} {cx},{cy+r*0.5} {cx-r*0.5},{cy}" fill="#ff8000" fill-opacity=".55"/>')
# large centre diamond
R=190
s.append(f'<polygon points="{W/2},{cy-R} {W/2+R},{cy} {W/2},{cy+R} {W/2-R},{cy}" fill="none" stroke="#ffb866" stroke-opacity=".85" stroke-width="2"/>')
R2=150
s.append(f'<polygon points="{W/2},{cy-R2} {W/2+R2},{cy} {W/2},{cy+R2} {W/2-R2},{cy}" fill="none" stroke="#c9a227" stroke-opacity=".5" stroke-width="1"/>')
# top / bottom border bands
for y0 in (60, H-60):
    s.append(f'<line x1="0" y1="{y0}" x2="{W}" y2="{y0}" stroke="#c9a227" stroke-opacity=".35"/>')
    for x in range(30, W, 48):
        s.append(f'<circle cx="{x}" cy="{y0}" r="3" fill="#ffb866" fill-opacity=".5"/>')
s.append(f'<rect width="{W}" height="{H}" filter="url(#grain)" opacity=".12"/>\n</svg>')
open('/site/assets/plates/weave.svg','w').write("\n".join(s))
print('weave rebuilt')
