"""Export expenses to a CSV file."""

import csv


def to_csv(expenses, path):
    """Write all expenses to a CSV file."""
    if not expenses:
        raise ValueError("Nothing to export.")

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=expenses[0].keys())
        writer.writeheader()
        writer.writerows(expenses)