#!/usr/bin/env python3
"""Paruošia docs/ aplanką GitHub Pages svetainei iš to paties turinio, kuris publikuojamas kaip artefaktai.

Naudojimas (iš Auto-tasks aplanko):  python3 scripts/build-pages.py

- index.html ir dokumentai/index.html artefakte gauna HTML pradžią automatiškai, čia ji pridedama;
- visiems puslapiams pridedama noindex žyma, kad nepatektų į paieškos sistemas;
- docs/ perrašomas kiekvieną kartą, jo ranka netaisyk.
"""
import os, re, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs")
NOINDEX = '<meta name="robots" content="noindex, nofollow">'
SKELETON = ('<!doctype html>\n<html lang="lt"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n' + NOINDEX +
            '\n<style>body{margin:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif}'
            '[hidden]:not([hidden=until-found i]){display:none!important}</style></head><body>\n')

FILES = ["index.html", "dokumentai/index.html"]
FILES += [os.path.join(d, f) for d in ("puslapiai/picker-accounts", "puslapiai/dashboard", "dokumentai")
          for f in sorted(os.listdir(os.path.join(ROOT, d))) if f.endswith(".html") and f != "index.html"]


def prepare(src):
    if not re.match(r"\s*<!doctype", src, re.I):
        return SKELETON + src
    # tik tikslus <head>, ne <header>
    m = re.search(r"<head(\s[^>]*)?>", src, re.I)
    return src[:m.end()] + "\n" + NOINDEX + src[m.end():] if m else NOINDEX + "\n" + src


shutil.rmtree(OUT, ignore_errors=True)
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
print("docs/ paruoštas:", len(FILES), "puslapiai")
