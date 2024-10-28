# Project Requirements:
# User Stories:

# As a user, I can add a new expense with details such as the amount, category (e.g., Food, Transport), and description.
# As a user, I can view all my expenses in a list format.
# As a user, I can delete an expense by its ID.
# As a user, I can generate a report that summarizes the total amount spent in each category.
# As a user, I can save my expenses to a file and load them when the application starts.
# As a user, I can edit an existing expense (change amount, category, or description).
# Main Features:

# Add, view, delete, edit, and categorize expenses.
# Data persistence with JSON.
# Simple report generation based on expense categories.

import expense
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def main():
    logging.info('Arrived at entry point for expense tracker app')
    expenseTracker = expense.Expense(databaseFileName='expenses.json')
    expenseTracker.load_expenses_from_json_database()

    while True:
        print('***********************************************************')
        print('Welcome to Expense tracker')
        print("\nExpense Tracker Options:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Edit Expense")
        print("5. Generate Report")
        print("6. Exit")

        choice = input('Choose a suitable option from 1 to 6:')

        if choice == '1':
            logging.info('Selected option 1 : Add Expense')
            typeOfExpense = input('Enter type of expense to add: ')
            amountOfExpense = input('Enter expense amount: ')
            expenseDescription = input('Enter a suitable description for expense: ')
            expenseTracker.add_new_expense(type=typeOfExpense, amount=amountOfExpense, description=expenseDescription)
        elif choice == '2':
            logging.info('Selected option 2 : View Expenses')
            expenseTracker.display_all_current_expenses()
        elif choice == '3':
            logging.info('Selected option 3 : Delete Expense')
            expenseId = input('Enter ID of expense to delete: ')
            expenseTracker.delete_expense_from_json_database(expenseId=expenseId)
        elif choice == '4':
            logging.info('Selected option 4 : Edit Expense')
            expenseId = input('Enter ID of expense to edit: ')
            typeOfExpense = input('Enter type of expense: ')
            amountOfExpense = input('Enter expense amount: ')
            expenseDescription = input('Enter a suitable description for expense: ')
            expenseTracker.edit_expense_details(expenseId=expenseId, type=typeOfExpense, amount=amountOfExpense, description=expenseDescription)
        elif choice == '5':
            logging.info('Selected option 5 : Generate Report')
            expenseTracker.generate_expense_report()
        elif choice == '6':
            logging.info('Selected option 6 : Exit')
            break
        else:
            logging.info('Invalid option : Please select a valid option from 1 to 6')

if __name__ == '__main__':
    main()

