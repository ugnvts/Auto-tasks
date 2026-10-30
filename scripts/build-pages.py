#!/usr/bin/env python3
"""Paruošia docs/ aplanką GitHub Pages svetainei iš to paties turinio, kuris publikuojamas kaip artefaktai.

Naudojimas (iš Auto-tasks aplanko):
  python3 scripts/build-pages.py                         – atnaujina naujausią versiją
  python3 scripts/build-pages.py --release "Aprašas"     – dar ir užšaldo prototipus kaip datuotą versiją

- index.html ir dokumentai/index.html artefakte gauna HTML pradžią automatiškai, čia ji pridedama;
- visiems puslapiams pridedama noindex žyma, kad nepatektų į paieškos sistemas;
- naujausia versija (docs/index.html, puslapiai/, dokumentai/) perrašoma kiekvieną kartą, jos ranka netaisyk;
- docs/versijos/ niekada neperrašomas: ten užšaldytos prototipų versijos (docs/versijos/YYYY-MM-DD[-N]/, be dokumentų)
  ir registras versijos.json, iš kurio sugeneruojamas versijų sąrašas docs/versijos/index.html.
"""
import argparse, datetime, html, json, os, re, shutil, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs")
VER = os.path.join(OUT, "versijos")
REG = os.path.join(VER, "versijos.json")
NOINDEX = '<meta name="robots" content="noindex, nofollow">'
SKELETON = ('<!doctype html>\n<html lang="lt"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n' + NOINDEX +
            '\n<style>body{margin:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif}'
            '[hidden]:not([hidden=until-found i]){display:none!important}</style></head><body>\n')

FILES = ["index.html", "dokumentai/index.html"]
FILES += [os.path.join(d, f) for d in ("puslapiai", "dokumentai")
          for f in sorted(os.listdir(os.path.join(ROOT, d))) if f.endswith(".html") and f != "index.html"]
LATEST = ["index.html", "puslapiai", "dokumentai"]
FROZEN = ["index.html", "puslapiai"]  # versijose saugomi tik prototipai


def prepare(src):
    if not re.match(r"\s*<!doctype", src, re.I):
        return SKELETON + src
    # tik tikslus <head>, ne <header>
    m = re.search(r"<head(\s[^>]*)?>", src, re.I)
    return src[:m.end()] + "\n" + NOINDEX + src[m.end():] if m else NOINDEX + "\n" + src


def build_latest():
    for rel in LATEST:
        p = os.path.join(OUT, rel)
        if os.path.isdir(p):
            shutil.rmtree(p)
        elif os.path.exists(p):
            os.remove(p)
    for rel in FILES:
        with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
            out = prepare(f.read())
        dst = os.path.join(OUT, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, "w", encoding="utf-8") as f:
            f.write(out)
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write("User-agent: *\nDisallow: /\n")


def load_reg():
    if os.path.exists(REG):
        with open(REG, encoding="utf-8") as f:
            return json.load(f)
    return []


def release(note):
    """Užšaldo dabartinius prototipus į docs/versijos/<data>[-N]/ – esamų versijų neliečia."""
    reg = load_reg()
    day = datetime.date.today().isoformat()
    vid, n = day, 2
    while os.path.exists(os.path.join(VER, vid)) or any(v["id"] == vid for v in reg):
        vid, n = f"{day}-{n}", n + 1
    dst = os.path.join(VER, vid)
    os.makedirs(dst)
    for rel in FROZEN:
        src = os.path.join(OUT, rel)
        (shutil.copytree if os.path.isdir(src) else shutil.copy2)(src, os.path.join(dst, rel))
    # Užšaldytame kataloge: data prie pavadinimo, nuoroda į versijų sąrašą vietoje „Versijos“
    idx = os.path.join(dst, "index.html")
    with open(idx, encoding="utf-8") as f:
        s = f.read()
    s = s.replace("<span>Prototypes</span>", f"<span>Prototypes · {vid}</span>", 1)
    s = s.replace('href="versijos/">Versions</a>', 'href="../">Frozen version · all versions</a>', 1)
    with open(idx, "w", encoding="utf-8") as f:
        f.write(s)
    try:
        commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    except OSError:
        commit = ""
    reg.append({"id": vid, "date": day, "note": note, "commit": commit})
    with open(REG, "w", encoding="utf-8") as f:
        json.dump(reg, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return vid


LIST_CSS = """:root{--bg:#eef0f3;--card:#fff;--fg:#17202a;--muted:#5f6b78;--line:#d8dde3;--accent:#4f46e5;
--f:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--m:"IBM Plex Mono",ui-monospace,Menlo,monospace}
@media (prefers-color-scheme:dark){:root{--bg:#11161c;--card:#181f27;--fg:#e3e8ee;--muted:#97a3b0;--line:#2b3540;--accent:#9d97ff;color-scheme:dark}}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 var(--f)}
main{max-width:760px;margin:0 auto;padding:32px max(16px,env(safe-area-inset-left,0px))}
h1{font-size:22px;font-weight:600;margin:0}.sub{color:var(--muted);margin:4px 0 24px}
ul{list-style:none;margin:0;padding:0;background:var(--card);border:1px solid var(--line);border-radius:10px}
li{display:flex;flex-wrap:wrap;gap:4px 16px;align-items:baseline;padding:14px 18px;border-top:1px solid var(--line)}li:first-child{border-top:0}
.d{font-family:var(--m);font-size:13px;min-width:110px}.n{flex:1 1 240px}.c{font-family:var(--m);font-size:12px;color:var(--muted)}
.l{display:flex;gap:14px}a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
.latest .d{color:var(--muted)}"""


def write_list():
    reg = load_reg()
    e = html.escape
    rows = ['<li class="latest"><span class="d">latest</span><span class="n">Current version – changes</span>'
            '<span class="l"><a href="../">Prototypes</a></span></li>']
    for v in sorted(reg, key=lambda v: v["id"], reverse=True):
        c = f'<span class="c">{e(v["commit"])}</span>' if v.get("commit") else ""
        rows.append(f'<li><span class="d">{e(v["id"])}</span><span class="n">{e(v["note"])}</span>{c}'
                    f'<span class="l"><a href="{e(v["id"])}/">Prototypes</a></span></li>')
    page = (SKELETON
            + '<title>Auto tasks versions</title>\n'
            + '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Mono:wght@500&display=swap">\n'
            + f"<style>{LIST_CSS}</style>\n<main><h1>Auto tasks · versions</h1>"
            + '<p class="sub">Frozen prototype versions never change, so they can be referenced in reviews. The latest version keeps changing.</p>'
            + "<ul>" + "".join(rows) + "</ul></main>\n</body></html>\n")
    os.makedirs(VER, exist_ok=True)
    with open(os.path.join(VER, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)


ap = argparse.ArgumentParser()
ap.add_argument("--release", metavar="APRAŠAS", help="užšaldyti naujausią versiją su šiuo aprašu")
a = ap.parse_args()
build_latest()
msg = f"docs/ paruoštas: {len(FILES)} puslapiai"
if a.release:
    msg += f"; užšaldyta versija {release(a.release)}"
write_list()
print(msg)
