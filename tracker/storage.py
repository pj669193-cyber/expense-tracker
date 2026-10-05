"""Save and load expenses from a JSON file."""

import json
from pathlib import Path

DATA_FILE = Path("expenses.json")


def load():
    """Read expenses from disk. Return an empty list if none exist."""
    try:
        return json.loads(DATA_FILE.read_text())
    except FileNotFoundError:          # first run: no file yet, which is normal
        return []
    except json.JSONDecodeError:       # file exists but is broken
        print("⚠ Data file corrupted, starting fresh.")
        return []


def save(expenses):
    """Write expenses to disk as readable JSON."""
    DATA_FILE.write_text(json.dumps(expenses, indent=2))