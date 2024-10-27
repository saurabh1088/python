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
                logging.info('Successfully read contents for expenses.json')
                logging.info(f'{self.expenses}')
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
            logging.info(f"\nValue : {self.expenses}")
                

    def add_new_expense(self, type, amount):
        logging.info(f'Adding new expense of type : {type} with amount : {amount}')
        newExpense = {
            "id": str(uuid.uuid1()),
            "type": type,
            "amount": amount,
            "date": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
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