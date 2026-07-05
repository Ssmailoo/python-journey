from expense_manager.manager import ExpenseManager
from expense_manager.business import BusinessExpenseManager

manager = ExpenseManager()
manager.add_expense(50000, "food", "nasi goreng")
manager.add_expense(20000, "transport", "angkot")
print(manager)

business = BusinessExpenseManager(0.1)
business.add_expense(100000, "equipment", "laptop stand")
business.add_expense(50000, "food", "client lunch")
print(business)