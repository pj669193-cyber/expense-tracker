"""Core functions for the expense tracker."""

from collections import defaultdict
from datetime import date


def add_expense(expenses, amount, category, note=""):
    """Add a new expense to the expense list."""
    if amount <= 0:
        raise ValueError("Amount must be positive.")

    next_id = max([e["id"] for e in expenses], default=0) + 1

    expense = {
        "id": next_id,
        "amount": round(amount, 2),
        "category": category.lower(),
        "note": note,
        "date": date.today().isoformat(),
    }

    expenses.append(expense)
    return expense


def delete_expense(expenses, expense_id):
    """Delete an expense using its ID."""
    for i, expense in enumerate(expenses):
        if expense["id"] == expense_id:
            return expenses.pop(i)

    raise KeyError(f"No expense with id {expense_id}")



def filter_by_category(expenses, category):
    """Return expenses that belong to one category."""
    return [e for e in expenses if e["category"] == category.lower()]


def summary(expenses):
    """Return total spending per category."""
    totals = defaultdict(float)
    for e in expenses:
        totals[e["category"]] += e["amount"]
    return dict(totals)