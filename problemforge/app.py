"""ProblemForge — GTK4 desktop aplikacija za Pop!_OS / GNOME.

Glavni UI: 5 tabova sa navigacijom.
  1. Dnevnik — problems.md journal (GLAVNA funkcija, FORCE MULTIPLIER #1)
  2. Teme — 5 tema sa vežbama
  3. Vežbe — force multipliers + dnevni ritam
  4. Resursi — knjige, članci, eseji
  5. Šabloni — gotovi formati (ADR, post-mortem, design doc)
"""

from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gdk, Gio, GLib, GObject, Gtk, Pango

from . import storage
from .data import DAILY_RHYTHM, FORCE_MULTIPLIERS, PRIORITY_ORDER, THEMES, TEMPLATES


def _esc(s: str) -> str:
    """Escape Pango markup za bezbedno prikazivanje u ActionRow subtitle."""
    return GLib.markup_escape_text(s, -1) if s else s

APP_ID = "com.problemforge.ProblemForge"
APP_NAME = "ProblemForge"


# ════════════════════════════════════════════════════════════════════
# GLAVNA APLIKACIJA
# ════════════════════════════════════════════════════════════════════
class ProblemForgeApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id=APP_ID)
        self.connect("activate", self._on_activate)
        self.win = None

    def _on_activate(self, app):
        if not self.win:
            self.win = MainWindow(application=app)
        self.win.present()


# ════════════════════════════════════════════════════════════════════
# GLAVNI PROZOR
# ════════════════════════════════════════════════════════════════════
class MainWindow(Adw.ApplicationWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_title(APP_NAME)
        self.set_default_size(980, 700)

        # glavni layout
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # --- header bar ---
        header = Adw.HeaderBar()
        header.add_css_class("flat")
        main_box.append(header)

        # --- toolbar sa dugmićima za tabove ---
        self.toolbar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.toolbar.set_margin_start(12)
        self.toolbar.set_margin_end(12)
        self.toolbar.set_margin_bottom(6)
        self.tab_buttons: dict[str, Gtk.ToggleButton] = {}
        tabs = [
            ("journal", "📖 Dnevnik"),
            ("themes", "🎯 Teme"),
            ("exercises", "💪 Vežbe"),
            ("resources", "📚 Resursi"),
            ("templates", "📋 Šabloni"),
        ]
        for i, (tid, label) in enumerate(tabs):
            btn = Gtk.ToggleButton(label=label)
            btn.connect("toggled", self._on_tab_toggled, tid)
            if i > 0:
                btn.set_group(self.tab_buttons[tabs[0][0]])
            self.toolbar.append(btn)
            self.tab_buttons[tid] = btn
        main_box.append(self.toolbar)

        # separator
        main_box.append(Gtk.Separator())

        # --- sadržaj (stack) ---
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.CROSSFADE)
        self.stack.set_vexpand(True)

        self.views = {
            "journal": JournalView(),
            "themes": ThemesView(),
            "exercises": ExercisesView(),
            "resources": ResourcesView(),
            "templates": TemplatesView(),
        }
        for tid, view in self.views.items():
            scroll = Gtk.ScrolledWindow()
            scroll.set_child(view)
            scroll.set_vexpand(True)
            self.stack.add_named(scroll, tid)

        main_box.append(self.stack)
        self.set_content(main_box)

        # aktiviraj prvi tab
        self.tab_buttons["journal"].set_active(True)

    def _on_tab_toggled(self, btn, tab_id: str):
        if btn.get_active():
            self.stack.set_visible_child_name(tab_id)
            self.views[tab_id].refresh()


# ════════════════════════════════════════════════════════════════════
# POMOĆNE FUNKCIJE ZA STILIZOVANJE
# ════════════════════════════════════════════════════════════════════
def make_label(text: str, css_class: str = "") -> Gtk.Label:
    lbl = Gtk.Label(label=text)
    lbl.set_wrap(True)
    lbl.set_xalign(0.0)
    if css_class:
        lbl.add_css_class(css_class)
    return lbl


def make_card(*widgets, spacing: int = 12) -> Gtk.Box:
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=spacing)
    box.set_margin_start(16)
    box.set_margin_end(16)
    box.set_margin_top(12)
    box.set_margin_bottom(12)
    box.add_css_class("card")
    for w in widgets:
        box.append(w)
    return box


def section_header(text: str) -> Gtk.Label:
    lbl = Gtk.Label(label=text)
    lbl.set_xalign(0.0)
    lbl.set_margin_start(16)
    lbl.set_margin_top(20)
    lbl.set_margin_bottom(8)
    lbl.add_css_class("title-4")
    return lbl


# ════════════════════════════════════════════════════════════════════
# VIEW 1: JOURNAL — dnevnik problema (GLAVNA funkcija)
# ════════════════════════════════════════════════════════════════════
class JournalView(Gtk.Box):
    """Dnevnik loše rešenih problema — FORCE MULTIPLIER #1."""

    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)

        # --- header ---
        header_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        header_box.set_margin_start(16)
        header_box.set_margin_end(16)
        header_box.set_margin_top(16)
        header_box.set_margin_bottom(8)

        title = Gtk.Label(label="📍 Dnevnik loše rešenih problema")
        title.add_css_class("title-2")
        title.set_xalign(0.0)
        title.set_hexpand(True)
        header_box.append(title)

        self.btn_new = Gtk.Button(label="➕ Novi unos")
        self.btn_new.add_css_class("suggested-action")
        self.btn_new.connect("clicked", self._on_new)
        header_box.append(self.btn_new)

        self.btn_export = Gtk.Button(label="📤 Izvezi MD")
        self.btn_export.connect("clicked", self._on_export)
        header_box.append(self.btn_export)

        self.append(header_box)

        # --- stats bar ---
        self.stats_label = Gtk.Label()
        self.stats_label.set_xalign(0.0)
        self.stats_label.set_margin_start(16)
        self.stats_label.set_margin_end(16)
        self.stats_label.set_margin_bottom(8)
        self.stats_label.add_css_class("dim-label")
        self.append(self.stats_label)

        # --- search ---
        search_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        search_box.set_margin_start(16)
        search_box.set_margin_end(16)
        search_box.set_margin_bottom(8)
        self.search_entry = Gtk.SearchEntry(placeholder_text="Pretraži probleme…")
        self.search_entry.set_hexpand(True)
        self.search_entry.connect("search-changed", self._on_search)
        search_box.append(self.search_entry)
        self.append(search_box)

        # --- sort dropdown ---
        sort_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        sort_box.set_margin_start(16)
        sort_box.set_margin_end(16)
        sort_box.set_margin_bottom(8)
        sort_box.append(Gtk.Label(label="Sortiraj:"))
        self.sort_model = Gtk.StringList.new(["Najnovije", "Najstarije", "Potencijal"])
        self.sort_dropdown = Gtk.DropDown(model=self.sort_model)
        self.sort_dropdown.connect("notify::selected", lambda *a: self.refresh())
        sort_box.append(self.sort_dropdown)
        self.append(sort_box)

        # --- lista unosa ---
        self.list_box = Gtk.ListBox()
        self.list_box.set_selection_mode(Gtk.SelectionMode.NONE)
        self.list_box.add_css_class("boxed-list")
        self.list_box.set_margin_start(16)
        self.list_box.set_margin_end(16)
        self.list_box.set_margin_bottom(16)
        self.list_box.set_valign(Gtk.Align.START)
        self.append(self.list_box)

        self._current_query = ""

    def refresh(self):
        """Osveži prikaz iz baze."""
        stats = storage.get_stats()
        self.stats_label.set_label(
            f"📊 {stats['total']} unosa ukupno · "
            f"⭐ {stats['high_potential']} sa visokim potencijalom · "
            f"📅 {stats['this_week']} ove nedelje"
        )

        # očisti listu
        while True:
            row = self.list_box.get_first_child()
            if row is None:
                break
            self.list_box.remove(row)

        # sortiraj
        sel = self.sort_dropdown.get_selected()
        sort_map = {0: "newest", 1: "oldest", 2: "potential"}
        entries = storage.list_problems(sort_by=sort_map.get(sel, "newest"))

        # filtriraj pretragu
        if self._current_query:
            entries = storage.search_problems(self._current_query)

        if not entries:
            empty = Gtk.Label(label="Još uvek nema unosa.\n\nKlikni \"➕ Novi unos\" da počneš svoj dnevnik problema.\n\n"
                                   "Ovo je tvoj #1 prioritet za prelazak ka solo/indie radu.")
            empty.set_wrap(True)
            empty.set_justify(Gtk.Justification.CENTER)
            empty.set_margin_top(40)
            empty.set_margin_bottom(40)
            empty.add_css_class("dim-label")
            self.list_box.append(empty)
            return

        for entry in entries:
            self.list_box.append(ProblemRow(entry, on_delete=self.refresh, on_edit=self._on_edit))

    def _on_new(self, _btn):
        dialog = ProblemEditDialog(self.get_root())
        dialog.connect("saved", lambda *a: self.refresh())
        dialog.present()

    def _on_edit(self, entry: dict):
        dialog = ProblemEditDialog(self.get_root(), entry=entry)
        dialog.connect("saved", lambda *a: self.refresh())
        dialog.present()

    def _on_search(self, entry):
        self._current_query = entry.get_text().strip()
        self.refresh()

    def _on_export(self, _btn):
        md = storage.export_markdown()
        dialog = Gtk.Window(transient_for=self.get_root(), modal=True, title="Izvezi kao Markdown")
        dialog.set_default_size(600, 500)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        box.set_margin_start(12)
        box.set_margin_end(12)
        box.set_margin_top(12)
        box.set_margin_bottom(12)
        textview = Gtk.TextView()
        textview.set_editable(True)
        buf = textview.get_buffer()
        buf.set_text(md)
        scroll = Gtk.ScrolledWindow()
        scroll.set_child(textview)
        scroll.set_vexpand(True)
        box.append(scroll)
        btn_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8, halign=Gtk.Align.END)
        btn_copy = Gtk.Button(label="📋 Kopiraj")
        def _copy(*_):
            clip = self.get_display().get_clipboard()
            clip.set(md)
        btn_copy.connect("clicked", _copy)
        btn_close = Gtk.Button(label="Zatvori")
        btn_close.connect("clicked", lambda *_: dialog.destroy())
        btn_box.append(btn_copy)
        btn_box.append(btn_close)
        box.append(btn_box)
        dialog.set_child(box)
        dialog.present()


class ProblemRow(Adw.ActionRow):
    """Jedan red u listi problema."""

    def __init__(self, entry: dict, on_delete=None, on_edit=None):
        super().__init__()
        self.entry = entry
        self._on_delete = on_delete
        self._on_edit = on_edit

        problem = entry.get("problem", "(bez naziva)")
        self.set_title(problem)
        date_str = entry.get("created_at", "")[:10]
        subtitle_parts = []
        if entry.get("who_suffers"):
            subtitle_parts.append(f"Trpi: {entry['who_suffers']}")
        if entry.get("product_potential", 0) > 0:
            stars = "⭐" * entry["product_potential"]
            subtitle_parts.append(stars)
        if entry.get("tags"):
            subtitle_parts.append(" ".join(f"#{t}" for t in entry["tags"]))
        self.set_subtitle(" · ".join(subtitle_parts) if subtitle_parts else date_str)

        # dugmad
        btn_edit = Gtk.Button.new_from_icon_name("document-edit-symbolic")
        btn_edit.set_tooltip_text("Izmeni")
        btn_edit.set_valign(Gtk.Align.CENTER)
        btn_edit.add_css_class("flat")
        btn_edit.connect("clicked", lambda *_: self._on_edit and self._on_edit(self.entry))
        self.add_suffix(btn_edit)

        btn_del = Gtk.Button.new_from_icon_name("user-trash-symbolic")
        btn_del.set_tooltip_text("Obriši")
        btn_del.set_valign(Gtk.Align.CENTER)
        btn_del.add_css_class("flat")
        btn_del.connect("clicked", self._on_delete_clicked)
        self.add_suffix(btn_del)

        # ako ima ideju, dodaj u tooltip
        if entry.get("my_idea"):
            self.set_tooltip_text(entry["my_idea"])

    def _on_delete_clicked(self, _btn):
        dialog = Adw.AlertDialog(
            heading="Obrisati unos?",
            body=f"'{self.entry.get('problem', '')[:60]}'\nOva akcija je nepovratna.",
        )
        dialog.add_response("cancel", "Otkaži")
        dialog.add_response("delete", "Obriši")
        dialog.set_response_appearance("delete", Adw.ResponseAppearance.DESTRUCTIVE)
        dialog.connect("response", self._on_delete_response)
        dialog.present(self.get_root())

    def _on_delete_response(self, dialog, response):
        if response == "delete":
            storage.delete_problem(self.entry["id"])
            if self._on_delete:
                self._on_delete()


class ProblemEditDialog(Adw.Window):
    """Modal za dodavanje/izmenu unosa u dnevnik."""

    __gsignals__ = {
        "saved": (GObject.SignalFlags.RUN_FIRST, None, ()),
    }

    def __init__(self, parent, entry: dict | None = None):
        super().__init__(transient_for=parent, modal=True)
        self.entry = entry or {}
        self.set_title("Izmeni" if entry else "Novi problem")
        self.set_default_size(560, 620)

        outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        header = Adw.HeaderBar()
        outer.append(header)

        scroll = Gtk.ScrolledWindow()
        scroll.set_vexpand(True)

        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        content.set_margin_start(20)
        content.set_margin_end(20)
        content.set_margin_top(16)
        content.set_margin_bottom(16)

        self.entries: dict[str, Gtk.TextView] = {}
        fields = [
            ("problem", "Problem *", "Šta je neefikasno, bolno ili glupo?", True),
            ("who_suffers", "Ko trpi", "Korisnik? Dev tim? Biznis? Klijent?", False),
            ("current_solution", "Trenutno rešenje", "Kako se sada radi? Excel? Manual? Workaround?", False),
            ("why_bad", "Zašto je loše", "Koliko vremena/novca/stresa košta?", False),
            ("my_idea", "Moja ideja", "Ako bih rešavao — kakav pristup?", False),
        ]
        for key, label, placeholder, required in fields:
            lbl = Gtk.Label(label=label)
            lbl.set_xalign(0.0)
            lbl.add_css_class("heading")
            content.append(lbl)

            tv = Gtk.TextView()
            tv.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
            tv.set_min_content_height(60 if key == "problem" else 50)
            tv.get_buffer().set_text(self.entry.get(key, ""))
            tv.set_tooltip_text(placeholder)
            frame = Gtk.Frame()
            frame.set_child(tv)
            content.append(frame)
            self.entries[key] = tv

        # potencijal rating
        pot_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        pot_box.append(Gtk.Label(label="Potencijal kao proizvod:"))
        self.spin_potential = Gtk.SpinButton.new_with_range(0, 5, 1)
        self.spin_potential.set_value(self.entry.get("product_potential", 0))
        pot_box.append(self.spin_potential)
        content.append(pot_box)

        # tagovi
        tags_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        tags_box.append(Gtk.Label(label="Tagovi (zarezom):"))
        self.entry_tags = Gtk.Entry()
        self.entry_tags.set_text(", ".join(self.entry.get("tags", [])))
        self.entry_tags.set_hexpand(True)
        self.entry_tags.set_placeholder_text("npr. auth, performanse, UX")
        tags_box.append(self.entry_tags)
        content.append(tags_box)

        scroll.set_child(content)
        outer.append(scroll)

        # dugmad na dnu
        btn_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8, halign=Gtk.Align.END)
        btn_box.set_margin_start(20)
        btn_box.set_margin_end(20)
        btn_box.set_margin_top(8)
        btn_box.set_margin_bottom(16)
        btn_cancel = Gtk.Button(label="Otkaži")
        btn_cancel.connect("clicked", lambda *_: self.destroy())
        btn_save = Gtk.Button(label="💾 Sačuvaj")
        btn_save.add_css_class("suggested-action")
        btn_save.connect("clicked", self._on_save)
        btn_box.append(btn_cancel)
        btn_box.append(btn_save)
        outer.append(btn_box)

        self.set_child(outer)

    def _get_text(self, key: str) -> str:
        buf = self.entries[key].get_buffer()
        start, end = buf.get_bounds()
        return buf.get_text(start, end, False)

    def _on_save(self, _btn):
        problem = self._get_text("problem").strip()
        if not problem:
            dialog = Adw.AlertDialog(heading="Problem je obavezan", body="Unesi šta je problem pre snimanja.")
            dialog.add_response("ok", "U redu")
            dialog.present(self)
            return
        tags_raw = self.entry_tags.get_text()
        tags = [t.strip() for t in tags_raw.split(",") if t.strip()] if tags_raw else []
        fields = {
            "problem": problem,
            "who_suffers": self._get_text("who_suffers"),
            "current_solution": self._get_text("current_solution"),
            "why_bad": self._get_text("why_bad"),
            "my_idea": self._get_text("my_idea"),
            "product_potential": int(self.spin_potential.get_value()),
            "tags": tags,
        }
        if self.entry.get("id"):
            storage.update_problem(self.entry["id"], **fields)
        else:
            storage.add_problem(**fields)
        self.emit("saved")
        self.destroy()


# ════════════════════════════════════════════════════════════════════
# VIEW 2: TEME — 5 tematskih oblasti sa vežbama
# ════════════════════════════════════════════════════════════════════
class ThemesView(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.refresh()

    def refresh(self):
        # očisti
        while True:
            child = self.get_first_child()
            if child is None:
                break
            self.remove(child)

        self.append(section_header("🎯 5 tematskih oblasti za karijerni rast"))

        for theme in THEMES:
            self.append(self._make_theme_card(theme))

    def _make_theme_card(self, theme: dict) -> Gtk.Box:
        # header
        title_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        icon = Gtk.Label(label=theme["icon"])
        icon.add_css_class("title-1")
        title_box.append(icon)
        title_text = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        t = Gtk.Label(label=theme["title"])
        t.add_css_class("title-3")
        t.set_xalign(0.0)
        title_text.append(t)
        sub = Gtk.Label(label=theme["subtitle"])
        sub.set_xalign(0.0)
        sub.add_css_class("dim-label")
        sub.add_css_class("caption")
        title_text.append(sub)
        title_box.append(title_text)
        if theme.get("priority"):
            badge = Gtk.Label(label="⭐ TVOJ PRIORITET")
            badge.add_css_class("success")
            badge.add_css_class("caption")
            badge.set_margin_start(12)
            title_box.append(badge)

        widgets = [title_box]

        # summary
        summary = make_label(theme["summary"], "body")
        summary.set_margin_top(8)
        widgets.append(summary)

        # key principles
        if theme.get("key_principles"):
            widgets.append(make_label("Ključni principi:", "heading"))
            for p in theme["key_principles"]:
                plbl = Gtk.Label(label=f"• {p}")
                plbl.set_xalign(0.0)
                plbl.set_wrap(True)
                plbl.set_margin_start(12)
                widgets.append(plbl)

        # exercises
        if theme.get("exercises"):
            widgets.append(make_label("Vežbe:", "heading"))
            for ex in theme["exercises"]:
                ex_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
                ex_header = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                name = Gtk.Label(label=f"▸ {ex['name']}")
                name.set_xalign(0.0)
                name.add_css_class("subtitle")
                ex_header.append(name)
                freq = Gtk.Label(label=f"[{ex['frequency']}]")
                freq.add_css_class("dim-label")
                freq.add_css_class("caption")
                ex_header.append(freq)
                if ex.get("priority"):
                    star = Gtk.Label(label="📍#1")
                    star.add_css_class("error")
                    ex_header.append(star)
                ex_box.append(ex_header)
                desc = make_label(ex["desc"])
                desc.set_margin_start(16)
                ex_box.append(desc)
                ex_box.set_margin_bottom(6)
                widgets.append(ex_box)

        return make_card(*widgets)


# ════════════════════════════════════════════════════════════════════
# VIEW 3: VEŽBE — force multipliers + dnevni ritam
# ════════════════════════════════════════════════════════════════════
class ExercisesView(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.refresh()

    def refresh(self):
        while True:
            child = self.get_first_child()
            if child is None:
                break
            self.remove(child)

        self.append(section_header("💪 Force Multipliers — vežbe sa najvećim ROI"))
        intro = make_label(
            "Ovo su vežbe sa najvećim povratkom investicije. Svaka pogađa 3+ tema istovremeno. "
            "Počni sa #1 — to je tvoj najveći leverage za prelazak ka solo/indie."
        )
        intro.set_margin_start(16)
        intro.set_margin_end(16)
        intro.set_margin_bottom(8)
        self.append(intro)

        for fm in FORCE_MULTIPLIERS:
            self.append(self._make_fm_card(fm))

        self.append(section_header("📅 Dnevni ritam (10-15 minuta dnevno)"))
        for time, desc in DAILY_RHYTHM:
            row = Adw.ActionRow()
            row.set_title(desc)
            row.set_subtitle(time)
            row.add_css_class("property")
            row.set_margin_start(16)
            row.set_margin_end(16)
            self.append(row)

        self.append(section_header("🏆 Prioritet za tvoju situaciju"))
        for i, (name, why) in enumerate(PRIORITY_ORDER, 1):
            row = Adw.ActionRow()
            row.set_title(f"{i}. {name}")
            row.set_subtitle(why)
            row.set_margin_start(16)
            row.set_margin_end(16)
            self.append(row)

    def _make_fm_card(self, fm: dict) -> Gtk.Box:
        header_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        icon = Gtk.Label(label=f"{fm['icon']}")
        icon.add_css_class("title-2")
        header_box.append(icon)
        name_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        name = Gtk.Label(label=f"#{fm['priority']}: {fm['name']}")
        name.add_css_class("title-4")
        name.set_xalign(0.0)
        name_box.append(name)
        themes = Gtk.Label(label=" · ".join(fm["themes"]))
        themes.set_xalign(0.0)
        themes.add_css_class("dim-label")
        themes.add_css_class("caption")
        name_box.append(themes)
        header_box.append(name_box)

        why = make_label(fm["why"])
        why.set_margin_top(8)

        return make_card(header_box, why)


# ════════════════════════════════════════════════════════════════════
# VIEW 4: RESURSI — biblioteka svih preporuka
# ════════════════════════════════════════════════════════════════════
class ResourcesView(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.refresh()

    def refresh(self):
        while True:
            child = self.get_first_child()
            if child is None:
                break
            self.remove(child)

        self.append(section_header("📚 Biblioteka resursa — kuriran spisak"))

        for theme in THEMES:
            if not theme.get("resources"):
                continue
            th = Gtk.Label(label=f"{theme['icon']} {theme['title']}")
            th.set_xalign(0.0)
            th.set_margin_start(16)
            th.set_margin_top(16)
            th.set_margin_bottom(4)
            th.add_css_class("title-4")
            self.append(th)

            for title, author, kind, desc in theme["resources"]:
                row = Adw.ActionRow()
                row.set_title(title)
                row.set_subtitle(f"{author} — {desc}")
                badge = Gtk.Label(label=kind)
                badge.add_css_class("caption")
                badge.add_css_class("dim-label")
                badge.set_margin_end(8)
                row.add_suffix(badge)
                row.set_margin_start(16)
                row.set_margin_end(16)
                self.append(row)


# ════════════════════════════════════════════════════════════════════
# VIEW 5: ŠABLONI — gotovi formati za copy/paste
# ════════════════════════════════════════════════════════════════════
class TemplatesView(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.refresh()

    def refresh(self):
        while True:
            child = self.get_first_child()
            if child is None:
                break
            self.remove(child)

        self.append(section_header("📋 Šabloni — gotovi formati za copy/paste"))

        for key, tmpl in TEMPLATES.items():
            self.append(self._make_template_card(key, tmpl))

    def _make_template_card(self, key: str, tmpl: dict) -> Gtk.Box:
        header_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        title = Gtk.Label(label=tmpl["title"])
        title.add_css_class("title-4")
        title.set_xalign(0.0)
        title.set_hexpand(True)
        header_box.append(title)

        btn_copy = Gtk.Button(label="📋 Kopiraj")
        btn_copy.connect("clicked", lambda *_: self._copy(tmpl["body"]))
        header_box.append(btn_copy)

        desc = make_label(tmpl["desc"], "dim-label")

        # preview u monospace
        preview = Gtk.TextView()
        preview.set_editable(False)
        preview.set_wrap_mode(Gtk.WrapMode.NONE)
        preview.get_buffer().set_text(tmpl["body"])
        preview.add_css_class("monospace")
        preview_frame = Gtk.Frame()
        scroll = Gtk.ScrolledWindow()
        scroll.set_child(preview)
        scroll.set_min_content_height(140)
        scroll.set_max_content_height(200)
        preview_frame.set_child(scroll)

        return make_card(header_box, desc, preview_frame)

    def _copy(self, text: str):
        clip = self.get_display().get_clipboard()
        clip.set(text)
        # toast
        if hasattr(self.get_root(), "add_toast"):
            toast = Adw.Toast.new("Kopirano u clipboard")
            toast.set_timeout(2)
            self.get_root().add_toast(toast)


def run():
    """Entry point za pokretanje aplikacije."""
    app = ProblemForgeApp()
    return app.run()
