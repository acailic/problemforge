"""ProblemForge — native GTK4 desktop aplikacija za Pop!_OS / GNOME.

Podržava sistem karijernog razvoja zasnovan na 5 tema, sa fokusom na
problem-sensing (problems.md dnevnik) kao glavnom funkcijom.
"""

__version__ = "0.1.0"


def __getattr__(name):
    """Lazy import — app/run se učitavaju samo kada su potrebni.

    Omogućava importovanje data i storage bez GTK zavisnosti.
    """
    if name in ("ProblemForgeApp", "run"):
        from .app import ProblemForgeApp, run

        return locals()[name]
    raise AttributeError(f"module 'problemforge' has no attribute {name!r}")
