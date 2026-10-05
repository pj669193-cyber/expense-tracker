"""Command-line interface for the expense tracker."""

import argparse

from . import core, export, storage


def build_parser():
    """Define the commands the user can run."""
    parser = argparse.ArgumentParser(prog="tracker", description="Expense Tracker CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="Add an expense")
    add.add_argument("amount", type=float)
    add.add_argument("category")
    add.add_argument("-n", "--note", default="")

    lst = sub.add_parser("list", help="List expenses")
    lst.add_argument("-c", "--category")

    delete = sub.add_parser("delete", help="Delete an expense by id")
    delete.add_argument("id", type=int)

    sub.add_parser("summary", help="Show totals per category")

    exp = sub.add_parser("export", help="Export expenses to CSV")
    exp.add_argument("path", nargs="?", default="expenses.csv")

    return parser


def main():

    """Read the command, run it, and save the result."""
    args = build_parser().parse_args()
    expenses = storage.load()

    try:
        if args.command == "add":
            e = core.add_expense(expenses, args.amount, args.category, args.note)
            print(f"✔ Added #{e['id']}: {e['amount']} on {e['category']}")

        elif args.command == "list":
            rows = expenses
            if args.category:
                rows = core.filter_by_category(expenses, args.category)
            if not rows:
                print("No expenses found.")
            for e in rows:
                print(f"#{e['id']:<3} {e['date']}  {e['category']:<12} {e['amount']:>9.2f}  {e['note']}")

        elif args.command == "delete":
            core.delete_expense(expenses, args.id)
            print(f"✔ Deleted #{args.id}")

        elif args.command == "summary":
            totals = core.summary(expenses)
            for cat, total in sorted(totals.items(), key=lambda item: -item[1]):
                print(f"{cat:<12} {total:>9.2f}")
            print(f"{'TOTAL':<12} {sum(totals.values()):>9.2f}")

        elif args.command == "export":
            export.to_csv(expenses, args.path)
            print(f"✔ Exported {len(expenses)} expenses to {args.path}")


        storage.save(expenses)

    except (ValueError, KeyError) as err:
        print(f"✖ {err.args[0]}")