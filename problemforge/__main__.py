#!/usr/bin/env python3
"""ProblemForge — entry point.

Pokretanje:
    python3 -m problemforge
    ili
    problemforge  (nakon pip install)
"""

import sys

from problemforge.app import run

if __name__ == "__main__":
    sys.exit(run())
