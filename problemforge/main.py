#!/usr/bin/env python3
"""ProblemForge CLI entry point (instalira se kao console_script)."""

import sys
from problemforge.app import run

if __name__ == "__main__":
    sys.exit(run())
