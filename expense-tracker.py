# Description: A simple expense tracker program that allows users to add expenses, list all expenses, show total expenses, and filter expenses by category.


# Function to add a new expense to the list of expenses
def add_expense(expenses, amount, category):
    expenses.append({"amount": amount, "category": category})


# Function to print all expenses
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')


# Function to calculate the total expenses
def total_expenses(expenses):
    return sum(map(lambda expense: expense["amount"], expenses))


# Function to filter expenses by category
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense["category"] == category, expenses)


# Main function to run the program
def main():
    expenses = []  # List to store all expenses
    while True:  # Run the program in an infinite loop
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. List all expenses")
        print("3. Show total expenses")
        print("4. Filter expenses by category")
        print("5. Exit")

        choice = input("Enter your choice: ")  # Ask the user to enter a choice

        # Check the user's choice and call the appropriate function
        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            add_expense(expenses, amount, category)

        elif choice == "2":
            print("\nAll Expenses:")
            print_expenses(expenses)

        elif choice == "3":
            print("\nTotal Expenses: ", total_expenses(expenses))

        elif choice == "4":
            category = input("Enter category to filter: ")
            print(f"\nExpenses for {category}:")
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == "5":
            print("Exiting the program.")
            break


if __name__ == "__main__":
    main()  # Run the main function
