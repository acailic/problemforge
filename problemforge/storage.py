"""JSON-backed storage za ProblemForge.

Sve podatke čuvamo u ~/.local/share/problemforge/ (XDG standard).
Glavna datoteka: problems.json — niz unosa u dnevniku problema.
"""

from __future__ import annotations

import json
import os
import uuid
from datetime import datetime
from pathlib import Path

# XDG: ~/.local/share/problemforge — standard za Linux desktop aplikacije
_APP_DIR = Path(os.environ.get("XGL_DATA_HOME", Path.home() / ".local" / "share")) / "problemforge"
_DB_FILE = _APP_DIR / "problems.json"


def get_data_dir() -> Path:
    """Vrati (i kreiraj ako treba) direktorijum za podatke aplikacije."""
    _APP_DIR.mkdir(parents=True, exist_ok=True)
    return _APP_DIR


def get_db_path() -> Path:
    """Vrati putanju do problems.json."""
    return _DB_FILE


def _now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def _load() -> list[dict]:
    """Učitaj sve probleme. Vrati praznu listu ako ne postoji/je neispravan."""
    if not _DB_FILE.exists():
        return []
    try:
        with _DB_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
    except (json.JSONDecodeError, OSError):
        pass
    return []


def _save(entries: list[dict]) -> None:
    """Snimi listu problema na disk."""
    get_data_dir()
    tmp = _DB_FILE.with_suffix(".json.tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)
    tmp.replace(_DB_FILE)  # atomično


def add_problem(
    problem: str,
    who_suffers: str = "",
    current_solution: str = "",
    why_bad: str = "",
    my_idea: str = "",
    product_potential: int = 0,
    tags: list[str] | None = None,
) -> dict:
    """Dodaj novi unos i vrati ga."""
    entry = {
        "id": uuid.uuid4().hex[:12],
        "created_at": _now_iso(),
        "updated_at": _now_iso(),
        "problem": problem.strip(),
        "who_suffers": who_suffers.strip(),
        "current_solution": current_solution.strip(),
        "why_bad": why_bad.strip(),
        "my_idea": my_idea.strip(),
        "product_potential": int(product_potential),
        "tags": tags or [],
    }
    entries = _load()
    entries.append(entry)
    _save(entries)
    return entry


def update_problem(entry_id: str, **fields) -> dict | None:
    """Ažuriraj postojeći unos. Vrati ažurirani unos ili None."""
    entries = _load()
    for e in entries:
        if e["id"] == entry_id:
            for k, v in fields.items():
                if k in e and v is not None:
                    e[k] = v.strip() if isinstance(v, str) else v
            e["updated_at"] = _now_iso()
            _save(entries)
            return e
    return None


def delete_problem(entry_id: str) -> bool:
    """Obriši unos po ID-u. Vrati True ako je obrisan."""
    entries = _load()
    before = len(entries)
    entries = [e for e in entries if e["id"] != entry_id]
    if len(entries) < before:
        _save(entries)
        return True
    return False


def list_problems(sort_by: str = "newest") -> list[dict]:
    """Vrati sve probleme, sortirane."""
    entries = _load()
    if sort_by == "newest":
        entries.sort(key=lambda e: e.get("created_at", ""), reverse=True)
    elif sort_by == "oldest":
        entries.sort(key=lambda e: e.get("created_at", ""))
    elif sort_by == "potential":
        entries.sort(key=lambda e: e.get("product_potential", 0), reverse=True)
    return entries


def search_problems(query: str) -> list[dict]:
    """Pretraži probleme po svim tekst poljima (case-insensitive)."""
    q = query.lower().strip()
    if not q:
        return list_problems()
    results = []
    for e in _load():
        haystack = " ".join(
            str(e.get(k, ""))
            for k in ("problem", "who_suffers", "current_solution", "why_bad", "my_idea", "tags")
        ).lower()
        if q in haystack:
            results.append(e)
    results.sort(key=lambda e: e.get("created_at", ""), reverse=True)
    return results


def get_stats() -> dict:
    """Vrati osnovne statistike za dashboard."""
    entries = _load()
    total = len(entries)
    high_potential = sum(1 for e in entries if e.get("product_potential", 0) >= 4)
    this_week = 0
    now = datetime.now()
    for e in entries:
        try:
            created = datetime.fromisoformat(e["created_at"])
            if (now - created).days <= 7:
                this_week += 1
        except (KeyError, ValueError):
            pass
    # broj po tagu
    tag_counts: dict[str, int] = {}
    for e in entries:
        for t in e.get("tags", []):
            tag_counts[t] = tag_counts.get(t, 0) + 1
    return {
        "total": total,
        "high_potential": high_potential,
        "this_week": this_week,
        "top_tags": sorted(tag_counts.items(), key=lambda x: -x[1])[:5],
    }


def export_markdown() -> str:
    """Izvezi sve probleme kao markdown (za backup ili deljenje)."""
    entries = list_problems(sort_by="oldest")
    lines = ["# ProblemForge — Dnevnik problema", ""]
    if not entries:
        lines.append("_Još uvek nema unosa. Počni danas!_")
        return "\n".join(lines)
    for e in entries:
        lines.append(f"## {e['created_at'][:10]} — {e['problem'][:60]}")
        lines.append(f"**Problem:** {e['problem']}")
        if e.get("who_suffers"):
            lines.append(f"**Ko trpi:** {e['who_suffers']}")
        if e.get("current_solution"):
            lines.append(f"**Trenutno rešenje:** {e['current_solution']}")
        if e.get("why_bad"):
            lines.append(f"**Zašto je loše:** {e['why_bad']}")
        if e.get("my_idea"):
            lines.append(f"**Moja ideja:** {e['my_idea']}")
        lines.append(f"**Potencijal kao proizvod:** {e.get('product_potential', 0)}/5")
        if e.get("tags"):
            lines.append(f"**Tagovi:** {', '.join(e['tags'])}")
        lines.append("")
    return "\n".join(lines)
