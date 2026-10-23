# Auto tasks – dizaino darbai

Du bendri artefaktai (taisomi failai šiame aplanke, nuorodos nesikeičia):

- **Auto tasks prototipai** – https://claude.ai/artifact/U6JvYPom14xE6unYd6fjZ6
  - `index.html` – navigacija (ekranas · variantas)
  - `puslapiai/prototipas.html` – vienas prototipas su bendrais duomenimis: Dashboard (`#dashboard`) ir Picker accounts (`#picker-accounts`), tarp jų pereinama per kairįjį meniu
- **Auto tasks dokumentai** – https://claude.ai/artifact/5PZcnCghqBsyTqL7sei8hb
  - `dokumentai/index.html` – navigacija
  - `dokumentai/dizaino-sprendimai.html` – `#dizaino-sprendimai`
  - `dokumentai/variklio-logika.html` – `#variklio-logika`

Naujas ekrano variantas: atskiras failas `puslapiai/` + eilutė `PAGES` sąraše `index.html`.

`archyvas/` – 2026-10-22 review failas, GitHub Pages bandymas ir atmesti variantai (`atmesti-variantai/`); tik šiame kompiuteryje, ne git.
Versijų istorija – vietinis git.

## GitHub Pages

`docs/` – svetainės kopija GitHub Pages'ui (sugeneruota, ranka netaisyti).
Atnaujinti: `python3 scripts/build-pages.py`, tada GitHub Desktop → Commit → Push.
