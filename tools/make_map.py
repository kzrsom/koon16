svg = '''<svg viewBox="0 0 820 540" role="group" aria-label="Schematic orientation diagram with selectable places">
  <defs>
    <linearGradient id="sea" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0c2a33"/><stop offset="1" stop-color="#04141a"/>
    </linearGradient>
    <linearGradient id="land" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#12333c"/><stop offset="1" stop-color="#0c242c"/>
    </linearGradient>
    <pattern id="gr" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0v40" fill="none" stroke="#c9a227" stroke-opacity=".13"/>
    </pattern>
  </defs>
  <rect width="820" height="540" fill="url(#sea)"/>
  <rect width="820" height="540" fill="url(#gr)"/>
  <path d="M0 0 L118 0 C 214 118, 296 222, 356 320 C 396 388, 436 470, 466 540 L0 540 Z" fill="url(#land)"/>
  <g fill="none" stroke="#c9a227" stroke-opacity=".22">
    <path d="M0 60 C 96 160, 178 250, 238 348 C 272 404, 306 476, 330 540"/>
    <path d="M0 130 C 70 214, 140 292, 196 380 C 228 430, 258 490, 276 540"/>
    <path d="M0 210 C 44 274, 100 340, 148 412 C 176 452, 200 500, 214 540"/>
    <path d="M0 300 C 30 344, 62 392, 96 448 C 114 478, 132 512, 146 540"/>
  </g>
  <path d="M118 0 C 214 118, 296 222, 356 320 C 396 388, 436 470, 466 540"
        fill="none" stroke="#ffb866" stroke-opacity=".85" stroke-width="2.2"/>
  <path d="M134 0 C 230 116, 312 220, 372 318 C 412 386, 452 468, 482 540"
        fill="none" stroke="#ffb866" stroke-opacity=".22" stroke-width="1"/>
  <path d="M246 138 C 274 206, 296 268, 316 318 C 332 352, 358 374, 390 384"
        fill="none" stroke="#8fd0d8" stroke-opacity=".6" stroke-width="2.2" stroke-linecap="round"/>
  <path d="M262 132 C 290 200, 312 262, 332 312 C 348 346, 374 368, 404 378"
        fill="none" stroke="#8fd0d8" stroke-opacity=".2" stroke-width="1"/>
  <g stroke="#c9a227" stroke-opacity=".5" stroke-dasharray="6 7" fill="none">
    <path d="M358 392 L 470 402"/>
    <path d="M358 392 L 300 300"/>
    <path d="M358 392 L 560 340"/>
    <path d="M300 300 L 190 358"/>
    <path d="M358 392 L 650 262"/>
  </g>
  <g class="map-node is-active" data-place="1" data-kind="Orientation" data-title="Benadir orientation"
     data-body="A starting point for locating a context, not a definition of the reach of community ties, movement, or historical relationship."
     data-note="Orientation, not enclosure.">
    <circle cx="358" cy="392" r="19" fill="#ff8000" fill-opacity=".16"/>
    <circle cx="358" cy="392" r="7" fill="#ff8000"/>
    <text x="358" y="366" text-anchor="middle" fill="#ffd7ae" font-family="IBM Plex Mono, monospace" font-size="11" letter-spacing="1.4">BENADIR</text>
  </g>
  <g class="map-node" data-place="2" data-kind="Coastal connection" data-title="Coastal connections"
     data-body="Ports, fishing, trade, and travel link coastal settlements in ways that registers rarely capture. These connections are research questions, not fixed routes."
     data-note="Illustrative diagram — not a navigational or legal map.">
    <circle cx="470" cy="402" r="6.5" fill="#0a2028" stroke="#ffb866" stroke-width="1.8"/>
    <text x="482" y="406" fill="#cfe0dc" font-family="IBM Plex Mono, monospace" font-size="10" letter-spacing="1.2">COASTAL</text>
  </g>
  <g class="map-node" data-place="3" data-kind="Inland relation" data-title="Inland relations"
     data-body="Kinship, grazing, and markets connect inland and riverine communities. Naming and boundaries may differ between administrative records and local usage."
     data-note="Relationship, not boundary.">
    <circle cx="190" cy="358" r="6.5" fill="#0a2028" stroke="#ffb866" stroke-width="1.8"/>
    <text x="202" y="362" fill="#cfe0dc" font-family="IBM Plex Mono, monospace" font-size="10" letter-spacing="1.2">INLAND</text>
  </g>
  <g class="map-node" data-place="4" data-kind="Diasporic pathway" data-title="Diasporic pathways"
     data-body="Remittance, correspondence, and return shape how histories are remembered and funded. Diaspora memory may preserve material absent from local collections."
     data-note="Movement across contexts, not a single route.">
    <circle cx="650" cy="262" r="6.5" fill="#0a2028" stroke="#ffb866" stroke-width="1.8"/>
    <text x="662" y="266" fill="#cfe0dc" font-family="IBM Plex Mono, monospace" font-size="10" letter-spacing="1.2">DIASPORA</text>
  </g>
  <g class="map-node" data-place="5" data-kind="River &amp; farmland" data-title="River corridor and farmland"
     data-body="Water access, irrigation, and tenure are entangled. Claims about land often depend on how water is described, and by whom."
     data-note="Context for land questions — no claim about tenure.">
    <circle cx="316" cy="318" r="6.5" fill="#0a2028" stroke="#8fd0d8" stroke-width="1.8"/>
    <text x="328" y="314" fill="#bfe3e6" font-family="IBM Plex Mono, monospace" font-size="10" letter-spacing="1.2">RIVER</text>
  </g>
  <text x="640" y="330" text-anchor="middle" fill="#6f8b87" font-family="IBM Plex Mono, monospace" font-size="9" letter-spacing="2.4">INDIAN OCEAN</text>
  <text x="560" y="500" text-anchor="middle" fill="#6f8b87" font-family="IBM Plex Mono, monospace" font-size="8.5" letter-spacing="1.8">SCHEMATIC · NOT TO SCALE</text>
</svg>'''
open('/site/assets/plates/orientation.svg','w').write(svg)
print('written', len(svg))
