# Test the class
manager = ExpenseManager()
manager.add_expense(50000, "food", "nasi goreng")
manager.add_expense(20000, "transport", "angkot")
manager.add_expense(30000, "food", "kopi")

print(manager)
print(manager.get_total())
print(manager.get_by_category("food"))