# Expense Tracker CLI

A command-line expense tracker built with pure Python (standard library only).
Add, list, delete and summarize expenses, with data saved to JSON and CSV export.

## Features
- Add expenses with category and optional note
- List all expenses or filter by category
- Delete by id
- Spending summary per category with total
- Export to CSV
- Input validation and friendly error messages

## Setup
```bash
git clone https://github.com/pj669193-cyber/expense-tracker.git
cd expense-tracker
python3 -m venv .venv
source .venv/bin/activate
```

## Usage
```bash
python3 -m tracker add 250 food -n "lunch"
python3 -m tracker list
python3 -m tracker list -c food
python3 -m tracker summary
python3 -m tracker delete 1
python3 -m tracker export my_report.csv
```

## Project structure
```
tracker/
├── core.py      # business logic (add, delete, filter, summary)
├── storage.py   # JSON persistence
├── export.py    # CSV export
├── cli.py       # argparse commands
└── __main__.py  # entry point
```

## Concepts used
Functions, dicts and lists, comprehensions, `defaultdict`, error handling,
file I/O (JSON, CSV), modules and packages, `argparse`, virtual environments.

## Screenshot
(add a terminal screenshot here)
