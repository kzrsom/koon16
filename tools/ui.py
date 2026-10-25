"""Shared UI primitives + page shell for the Koonfur Bari redesign build."""

import time

PREFIX = ""
ASSET_V = str(int(time.time()))


def set_prefix(p):
    global PREFIX
    PREFIX = p


def H(path):
    """Resolve a site-relative link against the current page depth."""
    return PREFIX + path


# ---------------------------------------------------------------- primitives

def label(text, dark=False, cls="", rule=False):
    c = "label"
    if dark:
        c += " label--dark"
    if rule:
        c += " label--rule"
    if cls:
        c += " " + cls
    return f'<span class="{c}">{text}</span>'


def btn(href, text, variant="primary", small=False, arrow=True, so=None):
    ic = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
          if arrow else '')
    cls = f"btn btn--{variant}" + (" btn--sm" if small else "")
    so_attr = f' data-so="{so}"' if so else ''
    return f'<a class="{cls}" href="{href}"{so_attr}>{text}{ic}</a>'


def plate(name, cap, tag=None, cls="plate--wide", alt=None, note=None):
    alt = alt or cap
    tag_html = f'<span class="plate__tag">{tag}</span>' if tag else ''
    note_html = f'<p class="img-note">{note}</p>' if note else ''
    return f'''<figure class="plate-stack" style="margin:0">
  <div class="plate {cls}">
    <img src="{H('assets/plates/' + name)}" alt="{alt}" loading="lazy" decoding="async">
    {tag_html}
    <figcaption class="plate__cap">{cap}</figcaption>
  </div>
  {note_html}
</figure>'''


def section_head(lbl, title, body, dark=False, cls=""):
    return f'''<div class="section-head {cls}">
  <div>{label(lbl, dark=dark)}<h2 class="display h2 mt-2">{title}</h2></div>
  <p class="body lede soft">{body}</p>
</div>'''


def card(title, body, num=None, dark=False, link=None, chips=None, cls="", tag=None):
    c = "card" + (" card--dark" if dark else "")
    if cls:
        c += " " + cls
    num_html = f'<span class="card__num">{num}</span>' if num else ''
    chips_html = f'<div class="chips mt-2">{chips}</div>' if chips else ''
    link_html = f'<a class="link-arrow mt-2" style="display:inline-flex" href="{link[1]}">{link[0]} →</a>' if link else ''
    tag_html = f'<span class="chip chip--amber" style="margin-bottom:.8rem;display:inline-flex">{tag}</span>' if tag else ''
    inner = f'''<article class="{c}">
  {num_html}{tag_html}
  <h3 class="h4">{title}</h3>
  <p class="mt-1">{body}</p>
  {chips_html}{link_html}
</article>'''
    return inner


def kv(pairs, dark=False, stack=False):
    rows = "".join(
        f'<div><span class="k">{k}</span><span class="v">{v}</span></div>' for k, v in pairs
    )
    cls = "kv kv--stack" if stack else "kv"
    return f'<div class="{cls}">{rows}</div>'


def accordion(items, cls=""):
    body = []
    for i, (q, a) in enumerate(items):
        body.append(f'''<details{" open" if i == 0 else ""}>
  <summary><span>{q}</span><span class="sign" aria-hidden="true"></span></summary>
  <div class="acc-body">{a}</div>
</details>''')
    return f'<div class="acc {cls}">' + "".join(body) + "</div>"


def numlist(items):
    return '<ol class="numlist">' + "".join(
        f'<li><strong>{t}</strong><p>{d}</p></li>' for t, d in items
    ) + "</ol>"


def statrow(items):
    return '<div class="statrow">' + "".join(
        f'<div class="stat-item"><span class="n">{n}</span><span class="l" style="display:block">{l}</span></div>'
        for n, l in items
    ) + "</div>"


def filters(fid, cats, active="all"):
    out = [f'<div class="filters" data-filters="{fid}" role="group" aria-label="Filter">']
    for slug, text, count in cats:
        cls = "filter is-active" if slug == active else "filter"
        cnt = f'<span class="count">{count}</span>' if count else ''
        out.append(f'<button class="{cls}" type="button" data-filter="{slug}">{text}{cnt}</button>')
    out.append('</div>')
    return "".join(out)


def tabs(uid, items):
    """items = [(label, html), ...]"""
    bar, panels = [], []
    for i, (name, html) in enumerate(items):
        sel = "true" if i == 0 else "false"
        active = " is-active" if i == 0 else ""
        bar.append(f'<button class="tab" role="tab" aria-selected="{sel}" data-tab="{uid}-{i}" id="tab-{uid}-{i}">{name}</button>')
        panels.append(f'<div class="tabpanel{active}" role="tabpanel" id="{uid}-{i}" aria-labelledby="tab-{uid}-{i}" data-tabpanel="{uid}">{html}</div>')
    return (f'<div class="tabs" role="tablist" data-tabs="{uid}">' + "".join(bar) + "</div>"
            + f'<div data-panels="{uid}">' + "".join(panels) + "</div>")


def notice(lbl, body, variant=""):
    return f'''<div class="notice {variant}">
  <span class="label">{lbl}</span>
  <p>{body}</p>
</div>'''


def quote(text, cite):
    return f'<blockquote class="quote"><p>{text}</p><cite>{cite}</cite></blockquote>'


def cta_band(lbl, title, body, links, dark=True):
    band = "band--ink2" if dark else "band--paper2"
    return f'''<section class="section band {band} band--edge">
  <div class="wrap">
    <div class="grid g-1-2 align-center">
      <div>{label(lbl, dark=dark)}<h2 class="display h2 mt-2">{title}</h2></div>
      <div>
        <p class="lede soft">{body}</p>
        <div class="btn-row mt-3">{links}</div>
      </div>
    </div>
  </div>
</section>'''


def crumbs(items):
    parts = []
    for i, (name, href) in enumerate(items):
        if i:
            parts.append('<span class="sep">/</span>')
        if href:
            parts.append(f'<a href="{href}">{name}</a>')
        else:
            parts.append(f'<span aria-current="page">{name}</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + "".join(parts) + "</nav>"


# ---------------------------------------------------------------- navigation

NAV = [
    ("About", "about.html", "Ku saabsan"),
    ("Mission", "mission.html", "Hadafka"),
    ("History", "history.html", "Taariikh"),
    ("Research", "research.html", "Cilmi-baaris"),
    ("Archive", "archive.html", "Kaydka"),
    ("Field notes", "field-notes.html", "Qoraallo goobeed"),
    ("Get involved", "get-involved.html", "Ka qaybgal"),
]

ARCHIVE_NAV = [
    ("Overview", "archive.html", "Guudmar"),
    ("Chronology", "archive/chronology.html", "Taxane taariikheed"),
    ("Places", "archive/places.html", "Goobaha"),
    ("Oral histories", "archive/oral-histories.html", "Taariikhaha afka"),
    ("History & resistance", "archive/history-resistance.html", "Taariikh iyo iska caabin"),
    ("Sensitive records", "archive/sensitive-records.html", "Diiwaanno xasaasi ah"),
    ("Method", "archive/method.html", "Habka"),
]

FOOTER_COLS = [
    ("Program", [
        ("About the platform", "about.html"),
        ("Our mission", "mission.html"),
        ("What guides us", "principles.html"),
        ("History", "history.html"),
        ("Field notes", "field-notes.html"),
    ]),
    ("Research", [
        ("Research & evidence", "research.html"),
        ("Timeline framework", "timeline.html"),
        ("Map & land", "map.html"),
        ("Question register", "questions.html"),
        ("Document guide", "document.html"),
    ]),
    ("Biimaal archive", [
        ("Archive overview", "archive.html"),
        ("Chronology", "archive/chronology.html"),
        ("Places in relation", "archive/places.html"),
        ("Oral histories", "archive/oral-histories.html"),
        ("History & resistance", "archive/history-resistance.html"),
        ("Sensitive records", "archive/sensitive-records.html"),
        ("Editorial method", "archive/method.html"),
    ]),
]

SEARCH_INDEX = [
]

SVG_MARK = '''<svg class="brand-mark" viewBox="0 0 48 48" aria-hidden="true">
  <rect x="1" y="1" width="46" height="46" fill="none" stroke="#ffb866" stroke-opacity=".55"/>
  <rect x="1" y="1" width="46" height="46" fill="#071b22"/>
  <path d="M11 34V14h3.4v8.6L24.4 14h4.2l-8.2 7.6L29 34h-4.1l-6.4-9.2L14.4 28v6z" fill="#fffdf7"/>
  <path d="M31 14h6.4c3 0 5 1.6 5 4 0 1.7-1 3-2.6 3.5 2 .5 3.2 1.9 3.2 3.9 0 2.7-2.2 4.6-5.6 4.6H31zm3.3 2.6v4h2.6c1.5 0 2.4-.8 2.4-2s-.9-2-2.4-2zm0 6.2v4.4h2.9c1.7 0 2.7-.9 2.7-2.2s-1-2.2-2.7-2.2z" fill="#ff8000"/>
</svg>'''


def header(active, subnav=None):
    utility = f'''<div class="utility">
  <div class="wrap utility-inner">
    <span data-so="Qaab cilmi-baaris · ma aha xaqiijin taariikheed">Research framework · not a verified historical account</span>
    <div class="utility-links">
      <a href="{H('archive/method.html')}" data-so="Habka tifaftirka">Editorial method</a>
      <a href="{H('questions.html')}" data-so="Su'aalo furan">Open questions</a>
      <button class="lang-toggle" type="button" data-lang-toggle aria-label="Switch language">EN / SO</button>
    </div>
  </div>
</div>'''

    active_attr = ' class="is-active" aria-current="page"'
    links = "".join(
        f'<a href="{H(href)}" data-so="{so}"{active_attr if active == href else ""}>{name}</a>'
        for name, href, so in NAV
    )
    mobile = "".join(
        f'<a href="{H(href)}" data-so="{so}"{active_attr if active == href else ""}><span>{i+1:02d}</span>{name}</a>'
        for i, (name, href, so) in enumerate(NAV)
    ) + f'''<a href="{H("principles.html")}" data-so="Mabaadi'da"><span>08</span>Principles</a>
    <a href="{H("timeline.html")}" data-so="Taxanaha waqtiga"><span>09</span>Timeline</a>
    <a href="{H("map.html")}" data-so="Khariidad iyo dhul"><span>10</span>Map &amp; land</a>
    <a href="{H("questions.html")}" data-so="Su'aalo"><span>11</span>Questions</a>
    <a href="{H("document.html")}" data-so="Hagaha dukumeentiga"><span>12</span>Document guide</a>'''

    sub = ""
    if subnav:
        items = "".join(
            f'<a href="{H(href)}" data-so="{so}"{active_attr if subnav == href else ""}>{name}</a>'
            for name, href, so in ARCHIVE_NAV
        )
        sub = f'''<div class="subnav"><div class="wrap subnav-inner">
      <span class="subnav-label" data-so="Kaydka Biimaal">Biimaal archive</span>{items}
    </div></div>'''

    return f'''<div class="progress" aria-hidden="true"><span data-progress></span></div>
<header class="site-header" id="site-header">
  {utility}
  <div class="wrap header-main">
    <a class="brand" href="{H('index.html')}" aria-label="Koonfur Bari — home">
      {SVG_MARK}
      <span class="brand-text">
        <span class="brand-name">Koonfur Bari</span>
        <span class="brand-sub">Southern Somalia Research Program</span>
      </span>
    </a>
    <nav class="nav" aria-label="Primary">{links}</nav>
    <div class="header-actions">
      <button class="icon-btn" type="button" data-search-open aria-label="Search the site">
        <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
      </button>
      <button class="icon-btn menu-btn" type="button" data-menu-toggle aria-expanded="false" aria-controls="nav-mobile" aria-label="Open menu">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
      </button>
    </div>
  </div>
  <nav class="nav-mobile" id="nav-mobile" aria-label="Mobile">
    <div class="nm-grid">{mobile}</div>
  </nav>
  {sub}
</header>'''


def footer():
    cols = ""
    for title, links in FOOTER_COLS:
        inner = "".join(f'<a href="{H(href)}">{name}</a>' for name, href in links)
        cols += f'<div class="footer-col"><h4>{title}</h4>{inner}</div>'

    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <a class="brand" href="{H('index.html')}" style="text-decoration:none">
          {SVG_MARK}
          <span class="brand-text">
            <span class="brand-name">Koonfur Bari</span>
            <span class="brand-sub">Southern Somalia Research Program</span>
          </span>
        </a>
        <p data-so="Koonfur Bari waa madal rayid iyo taariikh. Sawirrada macnaha leh waa lagu calaamadeeyay si gooni ah marka la barbardhigo caddaynta taariikhda la xaqiijiyay.">A civic and historical platform for peaceful advocacy, community consent, and responsible documentation. Contextual imagery is labelled separately from verified historical evidence.</p>
        <div class="chips mt-3">
          <span class="chip chip--ghost-light"><span class="dot dot--open"></span>Lawful</span>
          <span class="chip chip--ghost-light"><span class="dot dot--open"></span>Peaceful</span>
          <span class="chip chip--ghost-light"><span class="dot dot--open"></span>Inclusive</span>
        </div>
      </div>
      {cols}
      <div class="footer-col">
        <h4 data-so="Ka qaybgal">Contribute</h4>
        <a href="{H('get-involved.html')}">Share a source</a>
        <a href="{H('get-involved.html')}#corrections">Request a correction</a>
        <a href="{H('get-involved.html')}#right-of-reply">Right of reply</a>
        <a href="{H('research.html')}#lead">Propose a research lead</a>
        <a href="{H('404.html')}">Access &amp; takedown</a>
        <a href="{H('about.html')}#contact">Contact pathways</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> Koonfur Bari · Demonstration build · Local placeholder content</span>
      <span class="pill">No verified historical claims published</span>
      <span>Language: <b data-lang-label>English</b></span>
    </div>
  </div>
</footer>
<button class="backtop" type="button" data-backtop aria-label="Back to top">
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 19V5M6 11l6-6 6 6"/></svg>
</button>
<div class="searchbox" data-search-box role="dialog" aria-modal="true" aria-label="Search">
  <div class="search-inner">
    <input type="search" placeholder="Search pages, archive dockets, questions…" data-search-input aria-label="Search query">
    <div class="search-results" data-search-results></div>
    <p class="search-hint">Press <b>Esc</b> to close · searching page titles and descriptions</p>
  </div>
</div>'''


def shell(title, description, active, body, subnav=None, extra_head=""):
    depth = 0 if PREFIX == "" else PREFIX.count("/")
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#04141a">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<link rel="icon" href="{H('assets/favicon.svg')}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=IBM+Plex+Mono:wght@400;500;600&family=Source+Serif+4:ital,opsz,wght@0,8..60,300..700;1,8..60,300..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{H('assets/styles.css')}?v={ASSET_V}">
{extra_head}
</head>
<body data-page="{active}" data-depth="{depth}">
<a class="skip" href="#main">Skip to content</a>
{header(active, subnav)}
<main id="main">
{body}
</main>
{footer()}
<div class="toast" data-toast role="status" aria-live="polite"></div>
<script src="{H('assets/search-index.js')}?v={ASSET_V}" defer></script>
<script src="{H('assets/app.js')}?v={ASSET_V}" defer></script>
</body>
</html>'''


def build_index(pages):
    """Flat JSON-ish index for the search overlay, injected into app.js."""
    rows = []
    for p in pages:
        rows.append('{"t":%s,"u":%s,"d":%s,"s":%s}' % (
            jstr(p["nav_title"]), jstr(p["url"]), jstr(p["description"][:110]), jstr(p["section"])))
    return "[" + ",".join(rows) + "]"


def jstr(s):
    import json
    return json.dumps(s)
