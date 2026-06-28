# ProblemForge

> **Native GTK4 desktop aplikacija za Pop!_OS / GNOME** — podržava sistem karijernog razvoja zasnovan na 5 vanvremenskih inženjerskih tema, sa fokusom na **problem-sensing** (`problems.md` dnevnik) kao glavnoj funkciji.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org)
[![GTK4](https://img.shields.io/badge/GTK-4.0-7E5497.svg)](https://gtk.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Šta je ProblemForge?

ProblemForge je desktop alat koji pretvara teoriju karijernog razvoja u **dnevnu praksu**. Ako si inženjer koji prelazi iz outsourcinga (izvršilac tuđih odluka) ka solo/indie radu (vlasnik celog ciklusa), glavna prepreka je **problem-sensing** — sposobnost da primetiš loše rešene probleme koje drugi previde.

**Problemi koje drugi previde su tvoje najvrednije indie ideje.** ProblemForge ti daje sistem da ih hvataš.

## Glavna funkcija: 📍 Dnevnik problema

Svaki dan, zapiši jednu stvar koja je "loše rešena" — na poslu, u alatima, u procesima klijenata. Posle 90 dana imaćeš ~90 unosa; 5–10 će biti prave indie prilike.

```
Problem: [Šta je neefikasno/bolno/glupo?]
Ko trpi: [Korisnik? Dev tim? Biznis?]
Trenutno rešenje: [Excel? Manual? Workaround?]
Zašto je loše: [Koliko vremena/novca/stresa košta?]
Moja ideja: [Ako bih rešavao — kakav pristup?]
Potencijal kao proizvod: [1-5]
```

## 5 tabova

| Tab | Šta radi |
|-----|----------|
| 📖 **Dnevnik** | CRUD dnevnik problema — glavna funkcija, pretraga, sortiranje, export u Markdown |
| 🎯 **Teme** | 5 vanvremenskih tema sa ključnim principima i vežbama |
| 💪 **Vežbe** | 6 Force Multiplier vežbi (najveći ROI) + dnevni ritam + prioriteti |
| 📚 **Resursi** | Kurirana biblioteka knjiga, članka i eseja po temama |
| 📋 **Šabloni** | Gotovi formati: ADR, Design Doc, Post-Mortem, Pet zašto — copy/paste |

## 5 tema koje aplikacija pokriva

| # | Tema | Zašto |
|---|------|------|
| 🧱 | **Osnove > Alati** | Alati se menjaju; inženjerska disciplina ostaje konstanta od 1980-ih |
| 🌐 | **Sistemsko razmišljanje** | Arhitektura ostaje iako se detalji menjaju — vidi "veliku sliku" |
| 🎯 | **Accountability** | Ko snosi posledice kada stvari puknu — to odvaja seniore od ostalih |
| 🔍 | **Duboko razumevanje problema** | ⭐ Tvoj najveći leverage — šta uopšte treba da se napravi |
| ✍️ | **Komunikacija** | Inženjering je timski sport — tvoj rad mora biti jasan drugima |

## Instalacija

### Zahtevi (Pop!_OS / Ubuntu 24.04+)

```bash
# GTK4 + libadwaita + PyGObject (već instalirano na Pop!_OS 24.04)
sudo apt install python3-gi gir1.2-gtk-4.0 gir1.2-adwaita-1 python3-gi-cairo
```

### Pokretanje iz izvornog koda

```bash
git clone https://github.com/acailic/problemforge.git
cd problemforge
pip install --user .
problemforge
```

Ili direktno bez instalacije:

```bash
python3 -m problemforge
```

### Integracija sa desktopom (opcionalno)

```bash
# instaliraj .desktop fajl da se pojavi u aplikacijama
cp data/com.problemforge.ProblemForge.desktop ~/.local/share/applications/
```

## Gde se čuvaju podaci?

Podaci se čuvaju u `~/.local/share/problemforge/problems.json` (XDG standard). Tvoji podaci nikada ne napuštaju tvoj uređaj.

## Zašto native GTK4?

- **Lagana** — Python + PyGObject, bez Electron bloat-a
- **Integrisana** — izgleda kao deo Pop!_OS / GNOME-a (libadwaita)
- **Brza** — native rendering, ne web view
- **Desktop-native** — .desktop fajl, sistemski clipboard, XDG putevi

## Razvoj

```bash
# instaliraj u editabilnom režimu
pip install --user -e ".[dev]"

# testovi
pytest tests/

# pokreni iz izvornog koda
python3 -m problemforge
```

## Struktura projekta

```
problemforge/
├── problemforge/
│   ├── __init__.py        # paket
│   ├── __main__.py        # python -m problemforge
│   ├── main.py            # CLI entry point
│   ├── app.py             # GTK4 UI (svi view-ovi)
│   ├── data.py            # statički sadržaj (5 tema, vežbe, resursi)
│   └── storage.py         # JSON backend za dnevnik problema
├── data/
│   └── com.problemforge.ProblemForge.desktop
├── tests/
│   └── test_storage.py
├── pyproject.toml
├── LICENSE
└── README.md
```

## Licenca

MIT — vidi [LICENSE](LICENSE).
