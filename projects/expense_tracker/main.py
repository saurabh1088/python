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

if __name__ == '__main__':
    main()

