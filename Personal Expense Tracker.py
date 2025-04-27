import os
import json
import matplotlib.pyplot as plt

class ExpenseTracker:
    def __init__(self, data_file="expenses.json"):
        self.data_file = data_file
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                return json.load(file)
        return []

    def save_expenses(self):
        with open(self.data_file, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description):
        self.expenses.append({
            "amount": amount,
            "category": category,
            "description": description
        })
        self.save_expenses()

    def view_expenses(self):
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense['amount']} - {expense['category']} - {expense['description']}")

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)
            self.save_expenses()

    def generate_report(self):
        category_totals = {}
        for expense in self.expenses:
            category = expense["category"]
            category_totals[category] = category_totals.get(category, 0) + expense["amount"]

        categories = list(category_totals.keys())
        totals = list(category_totals.values())

        plt.figure(figsize=(8, 6))
        plt.bar(categories, totals, color='skyblue')
        plt.xlabel("Categories")
        plt.ylabel("Total Amount")
        plt.title("Expense Report")
        plt.show()

# Sample CLI
if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            tracker.add_expense(amount, category, description)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            index = int(input("Enter the index of the expense to delete: ")) - 1
            tracker.delete_expense(index)
        elif choice == "4":
            tracker.generate_report()
        elif choice == "5":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
