# Refactor Expense Tracker v4 ke dalam OOP

class ExpenseManager:

    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }
        self.expenses.append(expense)

    def get_total(self):
        total = 0
        for expense in self.expenses:
            total += expense["amount"]
        return total

    def get_by_category(self, category):
        filtered = []
        for expense in self.expenses:
            if expense["category"] == category:
                filtered.append(expense)
        return filtered
    
    def __str__(self):
        total_expense = len(self.expenses)
        total = self.get_total()
        return f"{total_expense} expenses, Total: Rp{total}"
    

# Test the class
manager = ExpenseManager()
manager.add_expense(50000, "food", "nasi goreng")
manager.add_expense(20000, "transport", "angkot")
manager.add_expense(30000, "food", "kopi")

print(manager)
print(manager.get_total())
print(manager.get_by_category("food"))