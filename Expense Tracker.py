expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Summary")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        item = input("Expense name: ")
        category = input("Category: ")
        amount = float(input("Amount: "))

        expenses.append({
            "item": item,
            "category": category,
            "amount": amount
        })

        print("Expense added!")

    elif choice == "2":
        for e in expenses:
            print(f"{e['item']} | {e['category']} | ₹{e['amount']:.2f}")

    elif choice == "3":
        if not expenses:
            print("No expenses recorded.")
            continue

        total = sum(e["amount"] for e in expenses)
        highest = max(expenses, key=lambda x: x["amount"])

        print(f"Total Spending: ₹{total:.2f}")
        print(f"Highest Expense: {highest['item']} - ₹{highest['amount']:.2f}")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
