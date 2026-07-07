import click
import json
from expense_manager.manager import ExpenseManager

DATA_FILE = "expense.json"

def load_manager():
    manager = ExpenseManager()
    try:
        with open(DATA_FILE, "r") as f:
            expenses = json.load(f)
            for expense in expenses:
                manager.add_expense(
                    expense["amount"],
                    expense["category"],
                    expense ["description"]
                )
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return manager

def save_manager(manager):
    with open(DATA_FILE, "w") as f:
        json.dump(manager.get_expenses(), f)

@click.group()
def cli():
    pass

@cli.command()
@click.option("--amount", required=True, type=int, help="Expense amount")
@click.option("--category", required=True, help="Expense category")
@click.option("--description", required=True, help="Expense descrption")
def add(amount, category, description):
    manager = load_manager()
    manager.add_expense(amount, category, description)
    save_manager(manager)
    click.echo(f"Expense added: {category} - Rp{amount}")

@cli.command()
def summary():
    manager = load_manager()
    click.echo(manager)

@cli.command()
@click.option("--category", required=True)
def filter_expense(category):
    manager = load_manager()
    results = manager.get_by_category(category)
    for expense in results:
        click.echo(f"{expense['description']} - Rp{expense['amount']}")

if __name__ == "__main__":
    cli()