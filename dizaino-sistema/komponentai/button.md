# Button

Atnaujinta 2026-11-04. Juodraštis: taisyklės – vartotojo (2026-11-04), struktūra – iš Figmos (tik skaityta, nieko nekeista).

## Kur yra

| Komponentas | Failas → puslapis | Paskirtis |
|---|---|---|
| [`Button`](https://www.figma.com/design/qAh6Pggy8XiKnR33fM5Vck/?node-id=1-1172) | 🏸 Components → Buttons | Visi įprasti veiksmai |
| [`Action Panel/Button/Red`](https://www.figma.com/design/qAh6Pggy8XiKnR33fM5Vck/?node-id=41-1075) | 🏸 Components → Buttons | Pavojingi veiksmai (trynimas) |
| `Button groups/Button` | 🏸 Components → Buttons | Mygtukų grupė – dar neperžiūrėta |

## Kurį tipą rinktis

| Tipas | Kada | Pavyzdžiai | Kiek |
|---|---|---|---|
| **Primary** (indigo, baltas tekstas) | Pagrindinis puslapio ar sekcijos veiksmas | Save, Create | Vienas puslapiui ar sekcijai |
| **White** (baltas, pilkas rėmelis) | Antrinis veiksmas šalia Primary; taip pat numatytasis mygtukas visiems kitiems veiksmams | Cancel šalia Save; Select all, Export | Kiek reikia |
| **Secondary** (šviesiai indigo fonas) | Retai: antras pagrindinis veiksmas, kuris turi išsiskirti, bet nekonkuruoti su Primary | Kalendoriuje „Today“, kai šiandiena nematoma | Retai, tik pagrįstai |
| **Icon only / White Icon only** | Retai, specifinėse situacijose: veiksmas lentelės ląstelėje, ryškesnis veiksmo pabrėžimas, sekcijų išskleidimas | ⋮ lentelės eilutėje, išskleisti sekciją | Tik kai tekstinis mygtukas netelpa ar netinka |
| **Danger** → atskiras komponentas `Action Panel/Button/Red` | Pavojingas, negrįžtamas veiksmas | Delete account | Vienas veiksmui |

Pagrindiniai veiksmai visada daromi Primary ir White mygtukais. Secondary ir Icon only – išimtys.

### Poros

- **Save + Cancel:** Save = Primary, Cancel = White.
- **Kelių veiksmų eilė:** vienas Primary, kiti White.

## Būsenos

| State | Kada naudoti dizaine |
|---|---|
| Default | Visada statiniuose ekranuose |
| Hover, Focus | Tik būsenų demonstracijai ar prototipui |
| Disabled | Retai, kai to reikia konkrečiai situacijai. Mygtukas neslepiamas, tik išblunka (komponente – permatomumas 50 %). Tooltip – tik jei situacija to reikalauja |

`Action Panel/Button/Red` neturi Disabled būsenos.

## Ikonos

`Icon`: False (be ikonos), Leading (prieš tekstą), Trailing (po teksto), Both, Only (tik ikona – naudoti kartu su `Type=Icon only` arba `White Icon only`).

Komponente ikona įrašyta kaip „Mail“ – ją reikia pakeisti instance'e rankiniu būdu.

## Struktūra (kaip yra dabar)

- `Button` savybės: `Type` (Primary, Secondary, White, Icon only, White Icon only), `Size` (tik base), `Icon` (False, Leading, Trailing, Both, Only), `State` (Default, Hover, Focus, Disabled) – 56 variantai.
- Matmenys: aukštis 38, paddingas 17/9 (su ikona prieš tekstą 15/9), kampai 6, tarpas iki ikonos 8.
- Tekstas: `text-sm/leading-5/font-medium`. Spalvos: Primary `indigo/600` (hover `indigo/700`), tekstas `white`; White – `white`, rėmelis `gray/300`, tekstas `gray/700`, hover `gray/50`; Secondary – `indigo/100`, tekstas `indigo/700`, hover `indigo/200`. Šešėlis `shadow/sm`, fokusas – ring efekto stilius.
- `Action Panel/Button/Red` savybės: `Breakpoint` (Desktop 38 px, Mobile 42 px), `State` (Default, Hover, Focus). Fonas `red/100` (hover `red/200`), tekstas `red/700`.
- Aprašymai: `Button` ir `Action Panel/Button/Red` rinkiniuose – nuo 2026-11-04 (žr. žemiau).

## Aprašymų juodraštis Figmai

Kalba – anglų, kaip ir visa DS. **Įrašyta į Figmą 2026-11-04** (abiejų rinkinių `description`; variantai nekeisti). Kituose failuose matysis po bibliotekos publikavimo.

**`Button` (komponentų rinkinio aprašymas):**

> Standard button for all non-destructive actions.
>
> Type:
> • Primary – the main action of a page or section (Save, Create). One per page or section.
> • White – secondary action next to Primary (Cancel next to Save) and the default for all other actions.
> • Secondary – rare. A second key action that should stand out without competing with Primary (e.g. "Today" in a calendar).
> • Icon only / White Icon only – rare, for specific cases: actions in table cells, emphasised actions, expanding sections below. Use with Icon=Only.
>
> Main actions always use Primary and White.
>
> State: use Default in static screens. Disabled is rare – the button stays visible and is faded; add a tooltip only if the case requires it. Hover and Focus are for state demos.
>
> Destructive actions: use "Action Panel/Button/Red".

**`Action Panel/Button/Red`:**

> Button for destructive, irreversible actions (Delete account). Use instead of Button for any delete action. Breakpoint: Desktop in admin screens. No Disabled state.

## Vėliau (struktūros pakeitimai, aptarti su komanda)

- B. Teksto savybė „Label“ ir ikonos „Instance swap“.
- C. Ikonos kaip jungikliai („Leading icon“, „Trailing icon“) vietoj `Icon` varianto.
- D. Išimti `Size` (viena reikšmė), sujungti `Type=Icon only` su `Icon=Only`, susieti Danger su `Button`.

## Rastos problemos (2026-11-04, nekeista)

Svarbiausios pirmiau.

1. **Perrašymai, kurie blokuoja DS atnaujinimus.** Picker accounts dizainuose beveik visi `Button` instance'ai turi perrašytus fono, teksto stiliaus, šešėlio ir aukščio laukus – su **tomis pačiomis** reikšmėmis kaip komponente (pvz., Primary: fill `indigo/600`, `shadow/sm`, h38; tekstas `white`, `text-sm/leading-5/font-medium`). Dabar jie atrodo teisingai, bet pakeitus mygtuką DS šie instance'ai pakeitimo negaus. Taisymas – dizainuose „Reset all overrides“, DS liesti nereikia.
2. **Disabled daromas trimis būdais:** be ikonos – permatomumas 40 %, su ikona – 50 %, Icon only – be permatomumo, fonas `gray/200` ir ikona `gray/400`.
3. **Du skirtingi pavojingo veiksmo mygtukai:** `Action Panel/Button/Red` (paskyroje „Delete account“, švelnus `red/100` fonas) ir `Modals/Button/Red` (modalo „Delete“). Nėra taisyklės, kada kurį. Be to, Red mygtukai neturi Disabled, neturi šešėlio, o dydį vadina `Breakpoint`, ne `Size`.
4. **Secondary Focus nevienodas:** su ikona fonas `indigo/50`, be ikonos – `indigo/100`.
5. **Ikonos įrašytos komponente:** tekstiniuose mygtukuose „Mail“, Icon only – „Plus sm“; nėra „Instance swap“ savybės, nėra teksto savybės (žr. B).

Kiti mygtukų komponentai Picker accounts dizainuose: `Navbars/Icon button`, `toast/dismiss button`, `Modals/Dismiss button` – specializuoti, atskirai neperžiūrėti.
