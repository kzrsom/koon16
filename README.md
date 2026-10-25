# Koonfur Bari — Southern Somalia Research Program (redesign)

A redesigned, **multi-page static website** (20 standalone HTML pages, shared CSS/JS, no build step required to view) based on the original single-file hash-routed prototype.

Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8080
# → http://localhost:8080/index.html
```

## Pages

| Program | Research | Biimaal archive | Utility |
|---|---|---|---|
| `index.html` | `research.html` | `archive.html` (overview) | `404.html` |
| `about.html` | `timeline.html` | `archive/chronology.html` | |
| `mission.html` | `map.html` | `archive/places.html` | |
| `principles.html` | `questions.html` | `archive/oral-histories.html` | |
| `history.html` | `document.html` | `archive/history-resistance.html` | |
| `field-notes.html` | | `archive/sensitive-records.html` | |
| `get-involved.html` | | `archive/method.html` | |

## Design system

- **Palette:** deep teal/ink (`#04141a`, `#071b22`), warm paper (`#f5efe2`, `#fffdf7`), amber (`#ffbd74`), gold hairlines (`#c9a227`), orange accent (`#ff8000`).
- **Type:** Fraunces (display serif), Source Serif 4 (body), IBM Plex Mono (labels, metadata, navigation).
- **Components** (`assets/styles.css`): hero / page-hero, archive sub-navigation, cards, plates with corner brackets and status captions, chips, key–value lists, numbered lists, tables, accordions, tabs, filters, timeline rail, forms, notices, gate modal, annotated document frame, footer, search overlay, toast, back-to-top.
- **Imagery:** all visuals are locally generated SVG "archive plates" (`assets/plates/*.svg`) in the site's duotone palette — no external image dependencies, and every plate is captioned as illustrative context, never as evidence.

## Interaction (`assets/app.js`, vanilla JS)

- Sticky header with reading-progress bar; mobile menu
- Scroll-reveal (only for below-the-fold elements, with load/print safety nets)
- Category filters (research themes, catalogue, timeline, field notes, question register)
- Tabs (chronology evidence fields, testimony metadata)
- Annotated document: click a highlighted phrase ↔ note highlighting
- Interactive orientation diagram with a live readout panel
- Modal "safe-open" acknowledgement on sensitive-records
- Contribution / research-lead forms with custom validation, error states, and local-only success messaging
- Site search overlay (`Ctrl/⌘ + K`) over a generated index (`assets/search-index.js`)
- EN / SO toggle for navigation, labels, hero, and footer (long-form sections remain English pending translation review)
- Copy-to-clipboard citation templates

## Rebuilding

The HTML pages are generated from a small Python builder so the header, footer, and navigation stay in sync:

```bash
cd tools
python3 build.py     # writes the 20 pages + assets/search-index.js
```

- `tools/ui.py` — shell, header, footer, and UI primitives
- `tools/content_core.py` — home, about, mission, principles, history
- `tools/content_site.py` — research, archive, timeline, map, field notes, get involved, questions, document
- `tools/content_archive.py` — six archive dockets + 404
- `tools/make_plates.py`, `make_map.py`, `make_weave.py` — SVG artwork generators

## Editorial behaviour inherited from the original

The site keeps the source prototype's careful stance: no invented events, names, dates, figures, or citations; every record carries a visible status label (verified, documented, community memory, interpretation, allegation, unresolved, restricted); access conditions are described before content; and correction, right of reply, withdrawal, and takedown are presented as normal editorial outcomes.
