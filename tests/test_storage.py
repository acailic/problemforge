"""Testovi za storage backend (ne zahtevaju GTK)."""

import json
import os
import tempfile
from pathlib import Path

import pytest

# koristimo XDG_DATA_HOME da preusmerimo podatke u temp dir
@pytest.fixture
def temp_storage(monkeypatch, tmp_path):
    """Preusmeri storage u privremeni direktorijum."""
    xdg_dir = tmp_path / "share"
    xdg_dir.mkdir()
    monkeypatch.setenv("XGL_DATA_HOME", str(xdg_dir))
    # reinicijalizuj module-level putanje
    import importlib
    from problemforge import storage
    storage._APP_DIR = xdg_dir / "problemforge"
    storage._DB_FILE = storage._APP_DIR / "problems.json"
    yield storage
    # cleanup
    if storage._DB_FILE.exists():
        storage._DB_FILE.unlink()


def test_add_and_list(temp_storage):
    s = temp_storage
    entry = s.add_problem(
        problem="Test problem",
        who_suffers="Korisnik",
        product_potential=3,
    )
    assert entry["problem"] == "Test problem"
    assert entry["id"]
    entries = s.list_problems()
    assert len(entries) == 1
    assert entries[0]["problem"] == "Test problem"


def test_update(temp_storage):
    s = temp_storage
    entry = s.add_problem(problem="Original")
    updated = s.update_problem(entry["id"], problem="Izmenjeno", product_potential=5)
    assert updated is not None
    assert updated["problem"] == "Izmenjeno"
    assert updated["product_potential"] == 5
    entries = s.list_problems()
    assert entries[0]["problem"] == "Izmenjeno"


def test_delete(temp_storage):
    s = temp_storage
    entry = s.add_problem(problem="Za brisanje")
    assert s.delete_problem(entry["id"]) is True
    assert len(s.list_problems()) == 0
    # brisanje nepostojećeg vraća False
    assert s.delete_problem("nepostojeci") is False


def test_search(temp_storage):
    s = temp_storage
    s.add_problem(problem="Auth bug u loginu", who_suffers="svi korisnici")
    s.add_problem(problem="Spor upit za penzije", who_suffers="dev tim")
    results = s.search_problems("auth")
    assert len(results) == 1
    assert "Auth" in results[0]["problem"]
    # pretraga po who_suffers
    results = s.search_problems("penzije")
    assert len(results) == 1


def test_sorting(temp_storage):
    s = temp_storage
    s.add_problem(problem="Niski potencijal", product_potential=1)
    s.add_problem(problem="Visoki potencijal", product_potential=5)
    by_potential = s.list_problems(sort_by="potential")
    assert by_potential[0]["product_potential"] == 5
    assert by_potential[1]["product_potential"] == 1


def test_stats(temp_storage):
    s = temp_storage
    s.add_problem(problem="P1", product_potential=4)
    s.add_problem(problem="P2", product_potential=5)
    s.add_problem(problem="P3", product_potential=1, tags=["auth", "bug"])
    stats = s.get_stats()
    assert stats["total"] == 3
    assert stats["high_potential"] == 2  # >= 4
    assert stats["this_week"] == 3


def test_export_markdown(temp_storage):
    s = temp_storage
    s.add_problem(problem="Test problem za export", who_suffers="Korisnik", product_potential=3)
    md = s.export_markdown()
    assert "ProblemForge" in md
    assert "Test problem za export" in md
    assert "Korisnik" in md


def test_persistence_across_loads(temp_storage):
    """Podaci preživljavaju reinicijalizaciju (simulacija restarta aplikacije)."""
    s = temp_storage
    s.add_problem(problem="Trajni problem")
    # ponovo učitaj
    entries = s._load()
    assert len(entries) == 1
    assert entries[0]["problem"] == "Trajni problem"
