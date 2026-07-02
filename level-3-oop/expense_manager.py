# Refactor Expense Tracker v4 ke dalam OOP

class ExpenseManager:

    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        elif category.strip() == "":
            raise ValueError("Category cannot be empty")
        elif description.strip() == "":
            raise ValueError("Description cannot be empty")
        
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
    
manager = ExpenseManager()

# Test 1 - amount negatif
try:
    manager.add_expense(-50000, "food", "burger")
except ValueError as e:
    print(f"Error: {e}")

# Test 2 — category kosong
try:
    manager.add_expense(50000, "", "nasi goreng")
except ValueError as e:
    print(f"Error: {e}")

# Test 3 — expense valid
manager.add_expense(50000, "food", "nasi goreng")
print(manager)

manager.add_expense(50000, "   ", "nasi goreng")
print(manager)