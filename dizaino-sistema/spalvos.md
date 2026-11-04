# Spalvos – naudojimo auditas

Atnaujinta 2026-11-04. Auditas tik skaito failus, Figmoje niekas nekeista. Tie patys šaltiniai kaip [tipografija.md](tipografija.md).

## Šaltiniai

- **Design system:** [🏸 Typography and colours](https://www.figma.com/design/R5mokxY6vEUFn1DxtqsUE3/) – 241 paint style, kintamųjų (variables) nėra.
- **Tikrinti dizainai:** [Picking](https://www.figma.com/design/J1biVaroqChpfig1xouSb7/) → „📄 Picker accounts“ → „Section 1“ (`31608:23501`), 4653 sluoksniai.

## Santrauka

| Rodiklis | Reikšmė |
|---|---|
| Paint styles design system'e | 241: **143 spalvos** + **98 paveikslėliai** (`Avatar/…`, `Banner/…` iš Tailwind UI šablono) |
| Kintamieji | 0 – nėra semantinių tokenų, nėra režimų |
| Naudojama DS spalvų | **30** (28 sąsajai, 2 tik anotacijoms) |
| Nenaudojama DS spalvų | 113 + visi 98 paveikslėliai |
| Spalva iš kitos bibliotekos | 1: `neutral/neutral 800` („default colour for body text“) |
| Spalvos be stiliaus | 4 hex: logotipo `#cc0000`, `#66cc00`; `#c4c4c4` (placeholder); `#6b7280` (= gray/500, 1 kartas) |

Paletės naudojamos: **gray** (visi 10 atspalvių), **white**, **indigo**, **green**, **red**, vienas **rose**. Visai nenaudojamos: orange, yellow, Emerald, teal, cyan, light-blue, blue, pink, purple (tik anotacijose).

## Naudojamos spalvos pagal vaidmenį

### Tekstas

| Stilius | Hex | Vaidmuo | Kur |
|---|---|---|---|
| `gray/900` | #111827 | Pagrindinis tekstas | Cell (vardai), ekrano reikšmės, Select Menu, topbar |
| `gray/700` | #374151 | Laukų ir valdiklių pavadinimai | Checkboxes, Filter Dropdown, input label, antrinis Button |
| `gray/500` | #6b7280 | Antrinis tekstas | Cell (skaičiai), lentelės Header, topbar, placeholder |
| `gray/400` | #9ca3af | Ikonos, neaktyvus | sidebar-nav, Pagination, breadcrumbs |
| `gray/600` | #4b5563 | Filtro skaitiklis | Filter Dropdown |
| `white` | #ffffff | Tekstas ant pagrindinio mygtuko | Button |
| `indigo/600` | #4f46e5 | Nuorodos | text-link, Pagination |
| `indigo/700` | #4338ca | Antrinio (indigo) mygtuko tekstas | Button |
| `indigo/500` | #6366f1 | Breadcrumbs nuoroda | Simple with chevrons |
| `green/800` | #065f46 | Sėkmės pranešimo tekstas | toast |
| `red/800`, `red/700` | #991b1b, #b91c1c | Klaidos tekstas | toast, Dropdown („Delete“), Action Panel |
| `red/300` | #fca5a5 | Pavojingo veiksmo nuoroda | text-link |

### Paviršiai ir linijos

| Stilius | Hex | Vaidmuo | Kur |
|---|---|---|---|
| `white` | #ffffff | Kortelės, laukai, lentelės ląstelės | Cell, input, Select, Filter Dropdown |
| `gray/50` | #f9fafb | Lentelės antraštė, puslapio turinio fonas | Header (perrašyta instance'e), Content |
| `gray/100` | #f3f4f6 | Ląstelės fonas (hover / skeleton), dropdown | Cell, Dropdown |
| `indigo/50` | #eef2ff | Pažymėta lentelės eilutė | Cell (perrašyta instance'e, batch ekranas) |
| `indigo/100` | #e0e7ff | Aktyvaus filtro fonas | Filter Dropdown |
| `gray/800` | #1f2937 | Tamsūs paviršiai | sidebar-nav, batch-action-bar |
| `gray/200` | #e5e7eb | Skirtukai | `Divider` stačiakampiai (559 lentelėse) |
| `gray/300` | #d1d5db | Rėmeliai, skeleton | Cell, Checkboxes, input stroke, `placeholder` |

### Pagrindinė ir būsenų spalvos

| Stilius | Hex | Vaidmuo | Kur |
|---|---|---|---|
| `indigo/600` | #4f46e5 | Pagrindinis mygtukas, fokusas | Button fill, stroke |
| `green/600` | #059669 | Aktyvu / sėkmė (ikona) | Cell (varnelė), Checkboxes/display, toast |
| `green/50`, `green/400` | #ecfdf5, #34d399 | Sėkmės pranešimo fonas ir rėmelis | toast |
| `red/600` | #dc2626 | Klaida (ikona), pavojus | toast, Cell, Modal |
| `red/50`, `red/400` | #fef2f2, #f87171 | Klaidos pranešimo fonas ir rėmelis | toast |
| `red/100` | #fee2e2 | Pavojaus ikonos fonas | Modal |
| `rose/600` | #e11d48 | Žyma topbar'e | topbar-nav |

### Tik anotacijos

`purple/600` (drafting užrašai), `black` (skyrių pavadinimai 7xl).

## Pastebėtos design system problemos (nekeista)

1. **Sukeisti `green` ir `Emerald`:** DS `green/*` turi Tailwind **emerald** reikšmes (green/500 = #10b981), o `Emerald/*` – Tailwind **green** reikšmes (Emerald/500 = #22c55e). Be to, `Emerald` rašomas didžiąja raide, kitos paletės – mažąja.
2. **`yellow` yra Tailwind `amber`:** yellow/500 = #f59e0b (Tailwind amber-500), ne yellow.
3. **Kintamųjų nėra:** spalvos tik kaip paint styles, be semantinių pavadinimų (`text/primary`, `surface/selected`, `status/success`). Vaidmenis tenka atspėti iš atspalvio – lentelės viršuje yra pirmas žingsnis link jų.
4. **Antra spalvų sistema:** `neutral/neutral 800` atkeliauja iš kitos bibliotekos (Cell, Delivery ikonos, Filter menu-item).
5. **Viena reikšmė – keli atspalviai:** klaidos tekstas naudoja ir `red/700`, ir `red/800`. Indigo nuorodos – `indigo/500`, `/600` ir `/700`.
6. **Būsenos per instance perrašymus, ne variantus:** lentelės Header fonas (`gray/50`) ir pažymėta eilutė (`indigo/50`) perrašyti instance'uose.
7. **Skirtukai – atskiri stačiakampiai:** 559 `Divider` sluoksniai lentelėse, ne Cell rėmelis.
8. **98 paveikslėlių stiliai** (`Avatar/…`, `Banner/…`) spalvų sąraše – šablono likučiai.
9. **Spalvos be stiliaus:** `#c4c4c4` placeholder, `#6b7280` vienoje vietoje vietoj `gray/500`. Logotipo spalvos (`#cc0000`, `#66cc00`) – priimtina, tai prekės ženklas.

## Ką tai reiškia Auto tasks langams

HTML prototipas naudoja standartinį Tailwind (v3). Su DS jis sutampa ne visur:

| Prototipe | Tailwind hex | DS atitikmuo |
|---|---|---|
| Picking tag'as `green-100` / `green-800` | #dcfce7 / #166534 | `Emerald/100` / `Emerald/800` (ne `green/*`!) |
| Waiting `blue-100` / `blue-800` | #dbeafe / #1e40af | `blue/100` / `blue/800` – sutampa, bet DS sąsajoje blue dar nenaudojamas |
| Not synced `amber-100` / `amber-800` | #fef3c7 / #92400e | `yellow/100` / `yellow/800` |
| Naujoko žyma `violet-50` / `violet-700` | #f5f3ff / #6d28d9 | `purple/50` / `purple/700` – DS purple yra Tailwind violet; sąsajoje dar nenaudojamas |
| Temporary changes (indigo) | indigo | `indigo/*` – sutampa |

Būsenų tag'ams reikės paletės, kurios Picker accounts dizainuose dar nebuvo (blue, yellow/amber, purple).

**Sprendimas (2026-11-04): design system yra tiesos šaltinis.** Figmoje naudojamos DS spalvos jų DS pavadinimais, net jei hex skiriasi nuo prototipo. Žalia – `green/*`, kaip esamuose toast'uose ir Cell (ne `Emerald`). Prototipas laikomas eskizu: jo Tailwind spalvos Figmoje pakeičiamos artimiausiu DS stiliumi tuo pačiu pavadinimu (`green-100` → DS `green/100`, `amber-*` → DS `yellow/*`, `violet-*` → DS `purple/*`).

## Taisyklės kuriant naujus dizainus (kol DS netvarkytas)

- Design system yra tiesos šaltinis: jokių hex reikšmių ar spalvų iš prototipo, tik DS stiliai.
- Naudoti tik spalvas iš lentelių „Naudojamos spalvos pagal vaidmenį“; naujas paletes (blue, yellow, purple) – tik būsenų tag'ams, sutarus.
- Tekstas: `gray/900` pagrindinis, `gray/700` pavadinimai, `gray/500` antrinis. Nuorodos – `indigo/600`.
- Neperrašyti spalvų instance'uose, jei komponentas turi variantą.

## Kiti žingsniai

- [x] Žalia būsenų tag'ams – DS `green/*` (2026-11-04: DS yra tiesos šaltinis).
- [ ] Nuspręsti dėl semantinių kintamųjų (tekstas, paviršiai, būsenos) – pagal vaidmenų lenteles.
- [ ] Nuspręsti dėl paveikslėlių stilių ir nenaudojamų palečių (tik po aptarimo).
