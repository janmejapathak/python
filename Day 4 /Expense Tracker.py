import json
from datetime import datetime

FILE = "expenses.json"


def load_data():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(data):
    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_expense(data):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    data.append(expense)
    save_data(data)

    print("Expense added successfully!")


def show_expenses(data):
    if not data:
        print("No expenses found.")
        return

    total = 0

    print("\n========== EXPENSES ==========")

    for expense in data:
        print(
            f"{expense['date']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']} | "
            f"{expense['description']}"
        )

        total += expense["amount"]

    print("------------------------------")
    print(f"Total Expense: ₹{total:.2f}")


def category_summary(data):
    summary = {}

    for expense in data:
        category = expense["category"]

        summary[category] = summary.get(category, 0) + expense["amount"]

    print("\n====== CATEGORY SUMMARY ======")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


def main():
    data = load_data()

    while True:
        print("""
==============================
       EXPENSE TRACKER
==============================

1. Add Expense
2. Show Expenses
3. Category Summary
4. Exit
""")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense(data)

        elif choice == "2":
            show_expenses(data)

        elif choice == "3":
            category_summary(data)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
