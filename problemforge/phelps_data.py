"""Phelps elite training sistem — statički podaci.

Sve iz MD dokumenta o top 0.1% pristupu, strukturirano za UI prikaz.
"""

# ────────────────────────────────────────────────────────────────────
# DNEVNI MINIMUM — 3 stavke, svaki dan, 365 dana
# ────────────────────────────────────────────────────────────────────
DAILY_MINIMUM = [
    {
        "id": "problems_md",
        "icon": "📍",
        "label": "problems.md unos",
        "duration": "15 min",
        "desc": "Zapiši jedan loše rešen problem (posao, alati, procesi).",
    },
    {
        "id": "anki",
        "icon": "🃏",
        "label": "Anki pregled",
        "duration": "15 min",
        "desc": "Pregledaj Anki kartice (spaced repetition).",
    },
    {
        "id": "active_recall",
        "icon": "🧠",
        "label": "Aktivno prisjećanje",
        "duration": "15 min",
        "desc": "Iz glave rekonstruiši jučerašnje učenje (blank page test).",
    },
]

# ────────────────────────────────────────────────────────────────────
# NEDELJNI RASPORED — Phelps režim (~12-15h nedeljno)
# ────────────────────────────────────────────────────────────────────
WEEKLY_SCHEDULE = [
    {
        "days": "Pon – Pet",
        "blocks": [
            ("🏗️ Izgradi od nule", "45 min/dan", "Auth domen dubina — npr. OAuth provider od nule, source reading Keycloak/Auth0"),
            ("✍️ Content / Leverage", "45 min/dan", "500-reči analiza, open source PR, ili solo proizvod prototip"),
        ],
        "total": "~1.5h dnevno produkcije",
    },
    {
        "days": "Subota",
        "blocks": [
            ("🌍 Kompeticija / Izlaganje", "1h", "Submit nešto javno: PR, blog post, konferencijski talk prijava"),
            ("📚 Studija top inženjera", "1h", "Čitaj RFC autora, analitziraj Big Tech dizajn dokove, gledaj top talk-ove"),
        ],
        "total": "~2h kompeticije",
    },
    {
        "days": "Nedelja",
        "blocks": [
            ("📊 Review metrika", "30 min", "Šta sam proizveo? Šta izmjerio? Gde sam najslabiji?"),
            ("📅 Planiranje", "30 min", "Koja je najslabija karika? Šta napadam ove nedelje?"),
        ],
        "total": "~1h review + plan",
    },
]

# ────────────────────────────────────────────────────────────────────
# MESEČNE KONTROLE — 5 stvari koje moraš uraditi svakog meseca
# ────────────────────────────────────────────────────────────────────
MONTHLY_CHECKS = [
    ("mentor_session", "🎓 Mentor sesija", "1h sa paid mentor-om — code review + arhitekturalni feedback"),
    ("mastermind", "👥 Mastermind sync", "3-5 ambicioznih inženjera, nedeljni/meisečni sync"),
    ("publish", "📤 Objavi artefakt", "Blog post, open source PR, konferencijski talk"),
    ("metrics_review", "📊 Metrika review", "Skoraci na sve 4 metrike (output, dubina, leverage, pipeline)"),
    ("contact_better", "🥇 Kontaktiraj nekoga boljeg", "Pitaj jednu konkretnu stvar osobu koju poštuješ"),
]

# ────────────────────────────────────────────────────────────────────
# KVARTALNI MILESTONES
# ────────────────────────────────────────────────────────────────────
QUARTERLY_MILESTONES = [
    ("launch", "🚀 Lansiraj nešto na 'tržište'", "Proizvod, open source, ili talk — javno izlaganje"),
    ("retrospective", "🔍 Retrospektiva nivoa", "Top 5% ili top 1% u domeni? Ko bi potvrdio?"),
    ("checklist_update", "✅ Ažuriraj 'Mogu li ovo?' checklistu", "Šta novo možeš iz glave?"),
]

# ────────────────────────────────────────────────────────────────────
# 4 METRIKE — šta meriti
# ────────────────────────────────────────────────────────────────────
METRICS = [
    {
        "id": "output",
        "icon": "🏗️",
        "label": "Output",
        "unit": "min/dan",
        "desc": "Vreme u 'izgradi od nule' projektima + pisanje (ADR, blog, analize)",
        "target": "90 min/dan",
    },
    {
        "id": "depth",
        "icon": "🧠",
        "label": "Dubina",
        "unit": "skala 1-10",
        "desc": "Blank Page Test — koliko koncepta možeš iz glave?",
        "target": "8+/10",
    },
    {
        "id": "leverage",
        "icon": "⚡",
        "label": "Leverage",
        "unit": "ljudi",
        "desc": "Broj ljudi koji koristi tvoj kod/proizvod/content",
        "target": "rast nedeljno",
    },
    {
        "id": "pipeline",
        "icon": "📍",
        "label": "Pipeline",
        "unit": "problema",
        "desc": "Broj unosa u problems.md (nedeljno)",
        "target": "7+/nedelja",
    },
]

# ────────────────────────────────────────────────────────────────────
# MENTALITET: top 5% vs top 0.1%
# ────────────────────────────────────────────────────────────────────
MENTALITY_SHIFTS = [
    ("Trebalo bi da naučim X", "Ko je najbolji u X i šta on radi drugačije?"),
    ("Ovo je dovoljno dobro", "Da li je ovo najbolje što sam sposoban?"),
    ("Nemam vremena", "Ovo je prioritet, ostalo se prilagođava"),
    ("Godine iskustva", "Godine namernog razvoja"),
    ("Komotno sam", "Komotno znači da ne rastem"),
    ("Znam ovo", "Mogu li da generišem ovo iz glave?"),
    ("Radi moj posao", "Koji problem rešavam i za koga?"),
]

# ────────────────────────────────────────────────────────────────────
# REALAN VREMENSKI OKVIR
# ────────────────────────────────────────────────────────────────────
TIMELINE = [
    ("6 meseci", "Top 10%", "Top 10% u auth/authz dubini u regiji. problems.md pun. Prvi artefakti objavljeni."),
    ("12 meseci", "Top 5%", "Top 5% u auth + osiguranje presek. Prvi plaćeni solo projekat. Prepoznat u community."),
    ("24 meseca", "Top 1%", "Top 1% u domeni. Lisirani proizvod. Tražen kao konsultant/speaker."),
]
