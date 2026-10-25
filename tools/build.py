"""Build the Koonfur Bari multi-page static site."""
import os
import json
import ui
import content_core
import content_site
import content_archive

OUT = "/site"
PAGES = content_core.PAGES + content_site.PAGES + content_archive.PAGES

# search index (written once, shared)
index = [
    {"t": p["nav_title"], "u": p["url"], "d": p["description"], "s": p["section"]}
    for p in PAGES if p["url"] != "404.html"
]
with open(os.path.join(OUT, "assets/search-index.js"), "w") as f:
    f.write("window.KB_INDEX = " + json.dumps(index, ensure_ascii=False) + ";\n")

# pages
for p in PAGES:
    path = os.path.join(OUT, p["url"])
    os.makedirs(os.path.dirname(path), exist_ok=True)
    depth = 0 if "/" not in p["url"] else p["url"].count("/")
    ui.set_prefix("../" * depth)
    body = p["body"]()
    html = ui.shell(p["title"], p["description"], p["active"], body, p.get("subnav"))
    with open(path, "w") as f:
        f.write(html)
    print("built", p["url"], f"{len(html)//1024}kb")

print("total pages:", len(PAGES))
