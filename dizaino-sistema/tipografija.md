# Tipografija – naudojimo auditas

Atnaujinta 2026-11-04. Auditas tik skaito failus, Figmoje niekas nekeista.

## Šaltiniai

- **Design system:** [🏸 Typography and colours](https://www.figma.com/design/R5mokxY6vEUFn1DxtqsUE3/) – 92 text styles, importuota Tailwind sistema (pavadinimai `text-{dydis}/leading-{eilutė}/font-{storis}[/modifikatoriai]`). Šriftas – Inter.
- **Tikrinti dizainai:** [Picking](https://www.figma.com/design/J1biVaroqChpfig1xouSb7/) → puslapis „📄 Picker accounts“ → „Section 1“ (`31608:23501`): lentelė, batch actions, create / edit / view, inspector, toasts, empty state, skeleton.

Kiti Picking failo puslapiai netikrinti – juose gali būti naudojami kiti stiliai.

## Santrauka

| Rodiklis | Reikšmė |
|---|---|
| Stilių design system'e | 92 |
| Naudojama Picker accounts sekcijoje | **11** (9 sąsajai, 2 tik anotacijoms) |
| Nenaudojama | 81 |
| Teksto sluoksnių | 918, iš jų 753 (82 %) – komponentų viduje |
| Tekstų be stiliaus | 1 („Create picker accounts to…“, empty-state komponente: Inter Regular 14/20) |
| Šriftai | Inter Regular, Medium, Semi Bold, Bold |

Išvada: sąsaja realiai remiasi 9 stiliais. Jie padengia visus Picker accounts langų poreikius, įskaitant sutartą 18 px sekcijų antraštę ir 14 px tekstą (PK2, PK6).

## Naudojami stiliai (sąsaja)

| Stilius | Dydis / eilutė | Vaidmuo | Kur naudojama | Kartai |
|---|---|---|---|---|
| `text-2xl/leading-8/font-bold` | 24/32 Bold | Puslapio antraštė | „Picker accounts“, „Create picker account“, „Edit account“ | 13 |
| `text-lg/leading-6/font-medium` | 18/24 Medium | Sekcijos ir modalo antraštė | „Personal information“, „Employee information“, „Delete account?“ | 22 |
| `text-sm/leading-5/font-medium` | 14/20 Medium | Pagrindinis sąsajos tekstas: veiksmai, navigacija, pavadinimai | Button, sidebar-nav, topbar-nav, breadcrumbs, Filter Dropdown, Pagination, text-link, toast, Checkboxes, input label, lentelės vardo stulpelis (Cell), laukų pavadinimai peržiūroje | 523 |
| `text-sm/leading-5/font-normal` | 14/20 Regular | Reikšmės ir aprašai | Cell (skaičiai, kiti stulpeliai), input reikšmė ir placeholder, Select Menu, Dropdown meniu punktai, toast aprašas, modalo tekstas, peržiūros reikšmės | 286 |
| `text-sm/leading-5/font-semibold` | 14/20 Semi Bold | Aktyvaus filtro reikšmė | filter-status („Name: **Silvija**“) | 5 |
| `text-xs/leading-4/font-medium/tracking-wider/uppercase` | 12/16 Medium, +5 %, UPPER | Lentelės stulpelio antraštė | Header | 28 |
| `text-xs/leading-4/font-medium` | 12/16 Medium | Skaitiklio ženklelis | Filter Dropdown (aktyvių filtrų skaičius) | 5 |
| `text-xs/leading-4/font-normal` | 12/16 Regular | Pagalbinis tekstas po lauku | „Picker login name will…“ | 2 |
| `text-sm/leading-none/font-normal` | 14/14 Regular | Avataro inicialai | topbar-nav („VP“) | 13 |

## Naudojami tik anotacijoms (ne sąsaja)

| Stilius | Kur |
|---|---|
| `text-7xl/leading-none/font-normal` | Drafting skyrių pavadinimai („Batch actions“, „Toasts“, „Empty state“) |
| `text-lg/leading-6/font-normal` | Anotacijų paantraštės („Activation/deactivation“, „Create“) |
| `text-sm/leading-5/font-normal` | Anotacijų tekstas („default“, „hover“) – tas pats stilius kaip sąsajoje |

Anotacijos naudoja DS stilius. Dėl to drafting užrašai susimaišo su sąsajos naudojimu ir 7xl atrodo naudojamas.

## Nenaudojami stiliai (81)

Nė viename Picker accounts dizaine:

- **Display dydžiai 3xl–9xl** (30–128 px), visi `extrabold` ir `tracking-tight` – marketingo puslapiams, admin sąsajai nereikalingi.
- **2xl, xl** be `2xl/leading-8/font-bold` – kitos eilutės ir storio kombinacijos.
- **lg** be `lg/leading-6/font-medium` – `leading-none`, `leading-7`, `leading-8` variantai, `semibold`, `bold`, `underline`, `italic`, `uppercase`.
- **base (16 px)** – nė vienas iš 13 variantų. Sąsaja 16 px nenaudoja.
- **sm** – `leading-4`, `leading-8`, `bold`, `underline`, `italic`, `uppercase` variantai.
- **xs** – `leading-none`, `leading-5`, `semibold` ir kiti `uppercase` variantai.

## Pastebėtos design system problemos (nekeista)

1. **Dublikatas:** `text-4xl/leading-10/font-extrabold/tracking-tight` yra du kartus (raktai `0980b90f…` ir `f4684ffd…`).
2. **Pavadinimas neatitinka reikšmės:** `text-base/leading-8/font-medium/italic` eilutės aukštis 28 (tai `leading-7`, ne `leading-8` = 32).
3. **Per daug to paties dydžio variantų:** pvz., 14 px turi 4 eilutės aukščius (`none`, `4`, `5`, `8`) ir 13 stilių. Sąsaja naudoja 3 iš jų.
4. **Pavadinimai techniniai, ne pagal vaidmenį:** iš `text-sm/leading-5/font-medium` nesimato, kad tai mygtukų, navigacijos ir laukų pavadinimų tekstas. Vaidmenų stulpelis lentelėje viršuje yra pirmas žingsnis link semantinių pavadinimų.
5. **Anotacijų ir sąsajos stiliai bendri** – žr. skiltį „Naudojami tik anotacijoms“.
6. **Spalvų faile tarp fill styles yra Tailwind UI pavyzdžių paveikslėliai** (`Avatar/…`, `Banner/…`, apie 90). Tai ne spalvos, o šablono likučiai. Detaliau – spalvų audite.
7. **`italic` stilių šriftas nepatikrintas:** per API nepavyko perskaityti šrifto stiliaus (pvz., ar tai tikrai Inter Italic).

## Taisyklės kuriant naujus dizainus (kol DS netvarkytas)

- Naudoti tik 9 sąsajos stilius iš lentelės „Naudojami stiliai“. Naujo stiliaus prireikus – pirmiausia aptarti.
- 18 px sekcijų antraštės = `text-lg/leading-6/font-medium`. 14 px tekstas = `text-sm/leading-5/font-normal` (reikšmės) arba `font-medium` (pavadinimai, veiksmai).
- Tekstą be stiliaus naudoti tik anotacijose.

## Kiti žingsniai

- [ ] Spalvų naudojimo auditas tuo pačiu principu.
- [ ] Jei reikia pilno vaizdo – tas pats auditas visam Picking failui (visi puslapiai).
- [ ] Nuspręsti dėl nenaudojamų stilių: palikti, paslėpti nuo publikavimo ar trinti (tik po aptarimo).
