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
    
    def __len__(self):
        return len(self.__expenses)
    
    def __eq__(self, other):
        if not isinstance(other, ExpenseManager):
            return False
        return self.__expenses == other.get_expenses()

    
class BusinessExpenseManager(ExpenseManager):
    def __init__(self, tax_rate):
        super().__init__()
        self.tax_rate = tax_rate
    
    def get_total_with_tax(self):
        return int(self.get_total() * (1 + self.tax_rate))
    
    def __str__(self):
        total = self.get_total()
        total_with_tax = self.get_total_with_tax()
        return f"{super().__str__()}, Tax: Rp{total_with_tax - total}, Total with tax: Rp{total_with_tax}"
    
manager1 = ExpenseManager()
manager1.add_expense(50000, "food", "nasi goreng")

manager2 = ExpenseManager()
manager2.add_expense(50000, "food", "nasi goreng")

manager3 = ExpenseManager()
manager3.add_expense(99999, "transport", "angkot")

print(manager1 == manager2)   # isi sama
print(manager1 == manager3)   # isi berbeda
print(manager1 == "hello")    # bukan ExpenseManager