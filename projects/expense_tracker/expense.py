import os
import json
import pathlib
import logging
import uuid
import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

class Expense:

    def __init__(self, databaseFileName):
        logging.info('Initialising class Expense...')
        self.databaseFileName = databaseFileName
        self.expenses = []

    def load_expenses_from_json_database(self):
        logging.info('Loading expenses from json database file expenses.json')
        filepath = pathlib.Path.cwd() / self.databaseFileName
        logging.info(f'Calculated filepath for file {self.databaseFileName} : {filepath}')
        if os.path.exists(filepath):
            logging.info('Found file expenses.json')
            with open(self.databaseFileName, 'r') as file:
                self.expenses = json.load(file)
                pretty_json = json.dumps(self.expenses, indent=2)
                logging.info('Successfully read contents for expenses.json')
                logging.info(f'{pretty_json}')
        else:
            logging.error('Not able to find file expenses.json')
            self.expenses = []


    def delete_expense_from_json_database(self, expenseId):
        logging.info(f'Deleting expenses with ID : {expenseId} from json database file expenses.json')
        self.expenses = [expense for expense in self.expenses if expense["id"] != expenseId]
        self.save_expenses_to_json_database()

    
    def display_all_current_expenses(self):
        if not self.expenses:
            logging.info('There are currently no expense added')
        else:
            for expense in self.expenses:
                logging.info(f"\ID : {expense['id']}")
                logging.info(f"\Type : {expense['type']}")
                logging.info(f"\Amount : {expense['amount']}")
                logging.info(f"\Date : {expense['date']}")
                logging.info(f"\Description : {expense['description']}")
                

    def add_new_expense(self, type, amount, description):
        logging.info(f'Adding new expense of type : {type} with amount : {amount}')
        newExpense = {
            "id": str(uuid.uuid1()),
            "type": type,
            "amount": amount,
            "date": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            "description": description
        }
        logging.info(f'Created new expense : {newExpense}')
        self.expenses.append(newExpense)
        self.save_expenses_to_json_database()

    
    def save_expenses_to_json_database(self):
        logging.info('Saving expenses to json database expenses.json')
        filepath = pathlib.Path.cwd() / self.databaseFileName
        logging.info(f'Calculated filepath for file {self.databaseFileName} : {filepath}')
        if os.path.exists(filepath):
            logging.info('Found file expenses.json')
            with open(self.databaseFileName, 'w') as file:
                json.dump(self.expenses, file, indent=4)
                logging.info('Successfully saved expenses to expenses.json')
        else:
            logging.error('Not able to find file expenses.json')

    
    def edit_expense_details(self, expenseId, type=None, amount=None, description=None):
        logging.info(f'Editing details of expense with ID : {expenseId}')
        for expense in self.expenses:
            if expense['id'] == expenseId:
                if type is not None:
                    expense['type'] = type
                if amount is not None:
                    expense['amount'] = amount
                if description is not None:
                    expense['description'] = description
                self.save_expenses_to_json_database()
                return
            

    def generate_expense_report(self):
        report = {}
        for expense in self.expenses:
            type = expense['type']
            report[type] = report.get(type, 0) + float(expense['amount'])
        for type, expense in report.items():
            logging.info(f'Type : {type}, Expense : {expense}')
