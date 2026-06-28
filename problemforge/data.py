"""Sadržaj karijernog razvojnog sistema iz MD dokumenta.

5 tema, 6 force multiplier vežbi, resursi, i template formati.
Sve ovde je izvor istine — UI ga čita i prikazuje.
"""

# ────────────────────────────────────────────────────────────────────
# 5 TEMATSKE OBLASTI
# ────────────────────────────────────────────────────────────────────
THEMES = [
    {
        "id": "fundamentals",
        "title": "Osnove > Alati",
        "icon": "🧱",
        "subtitle": "Suština pre forme — inženjerske osnove ostaju konstanta",
        "summary": (
            "Industrija voli da izmišlja nova imena (AI Orchestrator, RAG Engineer) "
            "kako bi stvorila iluziju da se sve promenilo. Alati (uključujući AI) "
            "samo su sredstvo za rad, dok inženjerska disciplina ostaje konstanta "
            "još od 1980-ih."
        ),
        "key_principles": [
            "Svaki 'novi' alat je rekombinacija starih ideja (baze = fs + indeks)",
            "Simple ≠ Easy — simple je objektivno (raspleteno), easy je relativno",
            "Sve netrivijalne apstrakcije 'curu' — moraš znati šta je ispod",
            "Essence vs Accident: alati ne smanjuju suštinsku složenost",
            "Immutability: vrednosti su nepromenljivi snapshoti — čuva istoriju",
        ],
        "exercises": [
            {
                "name": "Bez žargona",
                "frequency": "Dnevno",
                "desc": (
                    "Kad god ti se pojavi nov alat/trend, napiši tri rečenice koje "
                    "objašnjavaju koji KLASIČNI problem rešava. Ako ne možeš — "
                    "ne razumeješ osnove, već si opčinjen ambalažom."
                ),
            },
            {
                "name": "Šta je ispod?",
                "frequency": "Nedeljno",
                "desc": (
                    "Izaberi alat koji koristiš. Objasni fundamentalni problem koji "
                    "rešava i koje klasične tehnike koristi ispod haube."
                ),
            },
            {
                "name": "Kvartalni fokus",
                "frequency": "Kvartalno",
                "desc": (
                    "Izaberi jednu temeljnu temu kvartalno i idi duboko: "
                    "konkurentnost, modelovanje podataka, distribuirani sistemi."
                ),
            },
            {
                "name": "Mapa apstrakcija",
                "frequency": "Nedeljno",
                "desc": (
                    "Za komponentu koju koristiš, nacrtaj slojeve apstrakcije "
                    "i gde svaki 'curi'. Identifikuj šta moraš znati ispod."
                ),
            },
        ],
        "resources": [
            ("Designing Data-Intensive Applications", "Martin Kleppmann", "Knjiga", "Fundament za baze, replikaciju, transakcije, konsenzus"),
            ("The Pragmatic Programmer (20th Anniversary)", "Hunt and Thomas", "Knjiga", "DRY, orthogonality, tracer bullets, broken windows"),
            ("No Silver Bullet", "Fred Brooks", "Članak (besplatno)", "Essence vs Accident — imunizuje od hype-a"),
            ("The Law of Leaky Abstractions", "Joel Spolsky", "Članak (besplatno)", "Sve apstrakcije curu — moraš znati ispod"),
            ("Simple Made Easy", "Rich Hickey", "Video (~1h)", "Simple ≠ Easy, complect = koren složenosti"),
            ("The Value of Values", "Rich Hickey", "Video (~40min)", "Immutable podaci, place-oriented programming"),
        ],
    },
    {
        "id": "systems",
        "title": "Sistemsko razmišljanje",
        "icon": "🌐",
        "subtitle": "Razumevanje 'velike slike' — arhitektura ostaje iako se detalji menjaju",
        "summary": (
            "Detalji implementacije se menjaju, ali arhitektura ostaje. Povezivanje "
            "AI agenata zahteva istu logiku kao povezivanje mikroservisa ili cron "
            "poslova. Tvoja vrednost je da vidiš kako se izolovani delovi uklapaju "
            "u širu infrastrukturu i korisničko iskustvo."
        ),
        "key_principles": [
            "Sistem > suma delova — struktura određuje ponašanje",
            "Stocks (akumulacije) i flows (protoci) + feedback petlje",
            "Balancing (stabilizujuće) vs reinforcing (pojačavajuće) petlje",
            "Kašnjenja u petljama izazivaju oscilaciju i nestabilnost",
            "Sistemi rade u degradiranom režimu — to je normalno, ne izuzetak",
            "Katastrofa zahteva VIŠESTRUKIE greške — single points su uklonjeni",
        ],
        "exercises": [
            {
                "name": "Crtaj pre nego što kuckaš",
                "frequency": "Dnevno",
                "desc": (
                    "Pre svakog taska, nacrtaj gde se tvoj deo uklapa u širi sistem — "
                    "i šta gore (kome služi), i šta dole (na šta se oslanja). "
                    "5 minuta, ne 50."
                ),
            },
            {
                "name": "Blast radius",
                "frequency": "Dnevno",
                "desc": (
                    "Pri svakoj promeni, nabroj sva mesta gde bi puklo ako pogrešiš. "
                    "Trenira istu veštinu koja ti treba za solo arhitekturu."
                ),
            },
            {
                "name": "Pre-mortem pre promene",
                "frequency": "Nedeljno",
                "desc": (
                    "Pre značajne promene: 'Šta će poći po zlu?'. Nabroj rizike i "
                    "mitigacije pre nego što kuckaš."
                ),
            },
            {
                "name": "Stock-flow mapa",
                "frequency": "Mesečno",
                "desc": (
                    "Nacrtaj stocks i flows tvog sistema. Identifikuj feedback petlje "
                    "i gde su kašnjenja koja izazivaju oscilaciju."
                ),
            },
            {
                "name": "Leverage point analiza",
                "frequency": "Mesečno",
                "desc": (
                    "Identifikuj gde je najveći leverage u sistemu. Najdublje tačke: "
                    "ciljevi sistema, paradigma, moć da se transcenduje paradigma."
                ),
            },
            {
                "name": "Retroaktivna Cook analiza",
                "frequency": "Mesečno",
                "desc": (
                    "Uzmi prošli incident. Analiziraj kroz Cook-ovih 18 teza: "
                    "kako je sistem bio 'degradiran' pre nego što je pukao?"
                ),
            },
        ],
        "resources": [
            ("Thinking in Systems: A Primer", "Donella Meadows", "Knjiga (~200 str)", "Stocks, flows, feedback, leverage points"),
            ("How Complex Systems Fail", "Dr. Richard Cook", "Članak (besplatno, 18 teza)", "Sistemi su uvek degradirani; katastrofa = višestruke greške"),
            ("Systemantics / The Systems Bible", "John Gall", "Knjiga", "Sistemi se protive svojoj svrsi"),
            ("Accelerate", "Forsgren, Humble, Kim", "Knjiga", "Empirijski podaci o devops performansama"),
        ],
    },
    {
        "id": "accountability",
        "title": "Accountability",
        "icon": "🎯",
        "subtitle": "Neprikosnovena odgovornost — ko snosi posledice kada stvari puknu",
        "summary": (
            "Rad sa novim alatima donosi nove nivoe apstrakcije i brzine, ali ne i "
            "promenu u tome ko snosi posledice kada stvari puknu. Biti osoba od "
            "poverenja koja rešava probleme kada sistem padne u produkciji je ono "
            "što odvaja prave seniore od ostalih."
        ),
        "key_principles": [
            "Error budget: SLO 99.9% → 0.1% budžet za greške — potrošiš = staje features",
            "SLI (mera) → SLO (cilj) → SLA (ugovor sa posledicama)",
            "Blameless post-mortem: svi su delovali logično; fokus na sistemu",
            "'Hope is not a strategy'",
            "Toil: rad koji je ponovljiv, automativ, taktički, bez trajne vrednosti",
            "Monitoring mora biti actionable — ako ne možeš reagovati, ne postavljaj",
            "Ownership: pratiš ishod (da li je rešeno), ne deliverable (da li si isporučio)",
        ],
        "exercises": [
            {
                "name": "Post-mortem bez obzira da li neko traži",
                "frequency": "Nedeljno",
                "desc": (
                    "Posle produkcijkog problema koji dodirneš, napiši: šta se desilo, "
                    "zašto, šta bi promenio. Makar za sebe. Izdvaja te kao nekoga ko "
                    "misli o sistemu, ne samo o tasku."
                ),
            },
            {
                "name": "Prati ishod, ne deliverable",
                "frequency": "Nedeljno",
                "desc": (
                    "Posle feature-a, saznaj: da li je problem zaista rešen? Da li "
                    "klijent koristi to što si napravio? Veza accountability + "
                    "problem-sensing."
                ),
            },
            {
                "name": "Dobrovoljni on-call",
                "frequency": "Prilika",
                "desc": (
                    "Ako imaš priliku da budeš u on-call rotaciji kod klijenta — uzmi. "
                    "Nema boljeg treninga za ownership od panka u 3 ujutru."
                ),
            },
            {
                "name": "Nedeljni review: 'Šta sam own-ovao?'",
                "frequency": "Nedeljno",
                "desc": (
                    "Prati ishode, ne aktivnosti. Šta si preuzeo vlasništvo nad "
                    "sistemske stvari, ne samo taskove."
                ),
            },
        ],
        "resources": [
            ("Site Reliability Engineering", "Google SRE Team", "Knjiga (besplatno online)", "Error budgets, post-mortems, incident response"),
            ("The Software Engineer's Guidebook", "Gergely Orosz", "Knjiga", "Senior→Staff: od rešavanja problema ka odabiru problema"),
            ("The DevOps Handbook", "Kim, Humble, et al.", "Knjiga", "Kultura accountability i učenja"),
        ],
    },
    {
        "id": "problem_understanding",
        "title": "Duboko razumevanje problema",
        "icon": "🔍",
        "subtitle": "Tvoj najveći leverage — šta uopšte treba da se napravi",
        "priority": True,
        "summary": (
            "Pravi inženjering nije puko pisanje koda, već shvatanje ŠTA treba da "
            "se napravi kada zahtevi nisu jasni. Ovo je tema gde imaš najviše "
            "prostora za rast i koja je PRESUDNA za prelaz na solo/indie."
        ),
        "key_principles": [
            "Mom Test: pričaj o NJIHOVOM životu, ne o tvojoj ideji",
            "Pitaj o specifikama u prošlosti, ne o mišljenjima o budućnosti",
            "Commitment (novac/kontakt) ≠ compliment ('zvuči super')",
            "Fall in love with the problem, not the solution",
            "MVP = najmanja stvar da testiraš hipotezu, ne lošija verzija",
            "Build-Measure-Learn petlja; validated learning kao mera napretka",
            "Najbolje ideje dolaze iz 'living in the future and noticing what's missing'",
        ],
        "exercises": [
            {
                "name": "Dnevnik loše rešenih problema (problems.md)",
                "frequency": "Dnevno",
                "priority": 1,
                "desc": (
                    "#1 PRIORITET. Svaki dan zapiši jednu stvar koja je 'loše rešena'. "
                    "Posle 90 dana: ~90 problema, 5-10 pravih indie prilika. "
                    "Ovo je glavna funkcija ove aplikacije — idi na 'Dnevnik' tab."
                ),
            },
            {
                "name": "Pet zašto na biznisu",
                "frequency": "Nedeljno",
                "desc": (
                    "Za svaki feature pitaj ZAŠTO dok ne dođeš do novca ili troška. "
                    "Sada znaš da li vredi X dinara ili nije bitan."
                ),
            },
            {
                "name": "Pričaj sa krajnjim korisnicima",
                "frequency": "Prilika",
                "desc": (
                    "U outsourcingu retkost — što je tačno competitive advantage. "
                    "Ako ikad imaš priliku da sedneš sa osobom koja koristi sistem — uzmi."
                ),
            },
            {
                "name": "Mom Test intervjui kolega",
                "frequency": "Mesečno",
                "desc": (
                    "Pitaj kolege o pain point-ima koristeći Mom Test pravila. "
                    "'Kada si poslednji put imao problem sa X?' ne 'Da li ti se sviđa X?'"
                ),
            },
        ],
        "resources": [
            ("The Mom Test", "Rob Fitzpatrick", "Knjiga (~150 str)", "Kako pitati o problemima da dobiješ istinu, ne komplimente"),
            ("Inspired: How to Create Tech Products Customers Love", "Marty Cagan", "Knjiga", "Product discovery, double diamond, fall in love with problem"),
            ("The Lean Startup", "Eric Ries", "Knjiga", "Build-Measure-Learn, MVP kao test hipoteze"),
            ("How to Get Startup Ideas", "Paul Graham", "Esej (besplatno)", "Living in the future, noticing what's missing"),
            ("Do Things That Don't Scale", "Paul Graham", "Esej (besplatno)", "Ručni rad u ranim danima je metoda učenja"),
            ("Don't Call Yourself A Programmer", "Patrick McKenzie", "Esej (besplatno)", "Rešavaš biznis probleme, ne pišeš kod"),
        ],
    },
    {
        "id": "communication",
        "title": "Komunikacija",
        "icon": "✍️",
        "subtitle": "Inženjering je timski sport — tvoj rad mora biti jasan drugima",
        "summary": (
            "Koliko god alati postajali napredni, inženjering ostaje timski sport. "
            "Razvijaj sposobnost da jasno komuniciraš tehničke kompromise. Ako drugi "
            "inženjeri mogu da ti veruju, lako nastave tvoj rad ili ga koriguju — "
            "tvoja vrednost u bilo kom timu biće ogromna."
        ),
        "key_principles": [
            "Writing scales; meetings don't — Tanya Reilly",
            "Tri stuba Staff rada: technical leadership, execution, alignment",
            "Influence without authority: ekspertiza + poverenje + odnosi",
            "Design doc: problem, goals/non-goals, pozadina, rešenje, alternative",
            "Pisanje forsira jasnoću mišljenja",
            "Code review koji uči, ne samo hvata bugove",
        ],
        "exercises": [
            {
                "name": "Piši design dokove i kad ne moraš",
                "frequency": "Nedeljno",
                "desc": (
                    "Pre složenijeg rada, napiši pola stranice: problem, opcije, "
                    "trade-off, preporuka. Podeli sa timom. Uči strukturano razmišljanje."
                ),
            },
            {
                "name": "ADR pre svake arhitektonske odluke",
                "frequency": "Prilika",
                "desc": (
                    "Architecture Decision Record: kontekst, odluka, zašto, posledice. "
                    "Vidi Templates tab za gotov format."
                ),
            },
            {
                "name": "Baka objašnjenje",
                "frequency": "Nedeljno",
                "desc": (
                    "Vežbaj tehničke trade-off-e objasniti netehničkom čoveku. "
                    "Ako ne možeš — sam ne razumeješ dovoljno duboko."
                ),
            },
            {
                "name": "Code review koji uči",
                "frequency": "Dnevno",
                "desc": (
                    "Piši review komentare kao da obučavaš: 'ovo može ovako, jer...' "
                    "ne 'ovo je bedno'. Ljudi pamte ko im je pomogao da porastu."
                ),
            },
        ],
        "resources": [
            ("The Staff Engineer's Path", "Tanya Reilly", "Knjiga (~300 str)", "Writing, influence without authority, big picture"),
            ("Staff Engineer: Leadership beyond the management track", "Will Larson", "Knjiga", "Sponsorship, leverage, 4 arhetipa"),
            ("Design Docs at Google", "Malte Kosian", "Članak", "Struktura dobrog design doc-a"),
            ("Cate Huston blog", "catehuston.com", "Blog", "Praktična inženjerska komunikacija"),
        ],
    },
]


# ────────────────────────────────────────────────────────────────────
# FORCE MULTIPLIERS — vežbe sa najvećim ROI (pogađaju 3+ teme)
# ────────────────────────────────────────────────────────────────────
FORCE_MULTIPLIERS = [
    {
        "name": "problems.md dnevnik",
        "icon": "📍",
        "themes": ["Duboko razumevanje problema", "Sistemsko razmišljanje", "Accountability"],
        "priority": 1,
        "why": (
            "Najvažnija vežba za prelazak u solo/indie. Svaki indie proizvod počinje "
            "sa primećivanjem problema koje drugi previde. Posle 90 dana imaćeš ~90 "
            "problema; 5-10 će biti prave prilike."
        ),
    },
    {
        "name": "Pisanje Design Dokova / ADR-a",
        "icon": "📝",
        "themes": ["Komunikacija", "Sistemsko razmišljanje", "Osnove > Alati", "Accountability"],
        "priority": 2,
        "why": (
            "Pisanje forsira jasnoću mišljenja. Ne možeš napisati 'Problem Statement' "
            "a da ne razumeš problem. Prelaz iz 'izvršilac' u 'osoba čije ideje usvajaju'."
        ),
    },
    {
        "name": "Blameless Post-Mortem (na sopstvenim greškama)",
        "icon": "🔬",
        "themes": ["Accountability", "Sistemsko razmišljanje", "Komunikacija"],
        "priority": 3,
        "why": (
            "Čak i retroaktivno. Sistemski uzroci, ne krivica. Najbrži put do "
            "reputacije 'osobe koja misli o sistemu'."
        ),
    },
    {
        "name": "Obrazloži osnove (500 reči)",
        "icon": "📚",
        "themes": ["Osnove > Alati", "Komunikacija"],
        "priority": 4,
        "why": (
            "Izaberi koncept nedeljno, napiši 500 reči iz prvih principa. Ako ne možeš "
            "jednostavno — ne razumeješ dovoljno duboko."
        ),
    },
    {
        "name": "Izgradi mali end-to-end proizvod",
        "icon": "🚀",
        "themes": ["Sve 5 tema"],
        "priority": 5,
        "why": (
            "Čak i CLI alat ili web app, solo. Razvija sve teme jer si TI ceo sistem — "
            "od problema do isporuke."
        ),
    },
]


# ────────────────────────────────────────────────────────────────────
# TEMPLATES — gotovi formati za copy/paste
# ────────────────────────────────────────────────────────────────────
TEMPLATES = {
    "problem_entry": {
        "title": "Dnevnik problema — unos",
        "desc": "Format za problems.md dnevnik (FORCE MULTIPLIER #1)",
        "body": (
            "## [Datum]\n"
            "**Problem:** [Šta je neefikasno/bolno/glupo?]\n"
            "**Ko trpi:** [Ko ima ovaj problem? Korisnik? Dev? Klijent?]\n"
            "**Trenutno rešenje:** [Kako se sada radi? Excel? Manual? Workaround?]\n"
            "**Zašto je loše:** [Koliko vremena/novca/stresa košta?]\n"
            "**Moja ideja:** [Ako bih rešavao — kakav pristup?]\n"
            "**Potencijal kao proizvod:** [1-5] (popuniti nakon nedelju dana)"
        ),
    },
    "adr": {
        "title": "ADR (Architecture Decision Record)",
        "desc": "Minimalni format za arhitektonske odluke",
        "body": (
            "# ADR-XXX: [Naslov odluke]\n"
            "**Datum:** \n"
            "**Status:** Proposed / Accepted / Superseded\n\n"
            "## Kontekst\n"
            "Zašto ova odluka postoji? Šta je problem? Šta su constraintovi?\n\n"
            "## Odluka\n"
            "Šta smo odlučili? (Konkretno, bez opravdanja — to dolazi ispod)\n\n"
            "## Zašto\n"
            "Razlozi. Tradeoff-ovi. Šta smo odbacili i zašto.\n\n"
            "## Posledice\n"
            "Šta ovo znači za sistem? Šta sada moramo da uradimo?"
        ),
    },
    "design_doc": {
        "title": "Design Doc",
        "desc": "Format za veće promene i sistemske odluke",
        "body": (
            "## Problem Statement (šta rešavamo i zašto)\n\n"
            "## Goals / Non-goals (šta jeste i šta nije u scope)\n\n"
            "## Background (kontekst koji čitalac treba)\n\n"
            "## Predloženo rešenje (arhitektura, dijagram)\n\n"
            "## Alternative razmotrene (šta smo odbacili i zašto)\n\n"
            "## Rizici i mitigacije"
        ),
    },
    "post_mortem": {
        "title": "Blameless Post-Mortem",
        "desc": "Format za analizu incidenata (bez krivice)",
        "body": (
            "# Post-Mortem: [Naslov incidenta]\n"
            "**Datum:** \n"
            "**Severity:** SEV-X\n"
            "**Duration:** \n\n"
            "## Impact (šta je pogođeno, koliko korisnika/biznis)\n\n"
            "## Timeline (hronološki — detekcija, akcije, rešenje)\n\n"
            "## Root Cause (sistemski, ne 'human error')\n\n"
            "## What Went Well (šta je spaslo situaciju)\n\n"
            "## What Went Wrong (gde je sistem zakazao)\n\n"
            "## Action Items (sa owner-ima i deadline-ima)\n"
            "- [ ] [Akcijs] — @owner — [datum]"
        ),
    },
    "five_whys": {
        "title": "Pet zašto (na biznisu)",
        "desc": "Kopaj do novca ili troška",
        "body": (
            "# Pet zašto na biznis logici\n\n"
            "**Feature:** [šta praviš]\n\n"
            "1. Zašto? → [odgovor]\n"
            "2. Zašto je to važno? → [odgovor]\n"
            "3. Zašto? → [odgovor]\n"
            "4. Zašto? → [odgovor]\n"
            "5. Koliko košta/treba? → [novac ili trošak]\n\n"
            "**Zaključak:** Da li ovaj feature vredi [iznos]?"
        ),
    },
}


# ────────────────────────────────────────────────────────────────────
# METAPODACI — prioriteti i dnevni ritam
# ────────────────────────────────────────────────────────────────────
PRIORITY_ORDER = [
    ("Dnevnik loše rešenih problema", "Najveći gap + direktno vodi ka indie idejama"),
    ("Praćenje ishoda feature-a", "Spaja accountability sa problem-sensingom"),
    ("Pet zašto na biznisu", "Najbrži način da naučiš domen dublje"),
    ("Sistemsko crtanje (5 min pre kodiranja)", "Jeftino, trenira viziju"),
    ("Ostalo", "Kumulira vremenom, ali nije blokirajuće"),
]

DAILY_RHYTHM = [
    ("10-15 min", "problems.md — zapiši jedan problem"),
    ("5 min", "Blast radius pre svake promene"),
    ("5 min", "Crtaj kontekst pre taska"),
    ("Na priliku", "Code review koji uči"),
]


def get_theme(theme_id: str) -> dict:
    """Vrati temu po ID-u."""
    for t in THEMES:
        if t["id"] == theme_id:
            return t
    raise KeyError(f"Nepoznata tema: {theme_id}")
