# Refactor Expense Tracker v4 with OOP

class ExpenseManager:

    def __init__(self):
        self.__expenses = []

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
        self.__expenses.append(expense)

    def get_expenses(self):
        return self.__expenses.copy()

    def get_total(self):
        return sum(expense["amount"] for expense in self.__expenses)

    def get_by_category(self, category):
        return [
            expense 
            for expense in self.__expenses 
            if expense["category"] == category
        ]
    
    def __str__(self):
        return f"{len(self.__expenses)} expenses, Total: Rp{self.get_total()}"
    
class BusinessExpenseManager(ExpenseManager):
    def __init__(self, tax_rate):
        super().__init__()
        self.tax_rate = tax_rate
    
    def get_total_with_tax(self):
        return int(self.get_total() * (1 + self.tax_rate))
    
    def __str__(self):
        return f"{len(self._ExpenseManager__expense)} expenses, Total: Rp{self.get_total()}, Tax: Rp{self.get_total_with_tax() - self.get_total()}"
    
    def __str__(self):
        total = self.get_total()
        total_with_tax = self.get_total_with_tax()
        return f"{super().__str__()}, Tax: Rp{total_with_tax - total}, Total with tax: Rp{total_with_tax}"
    
business = BusinessExpenseManager(0.1)
business.add_expense(100000, "equipment", "laptop stand")
business.add_expense(50000, "food", "client lunch")

print(business)