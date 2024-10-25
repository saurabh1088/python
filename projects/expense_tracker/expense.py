import os
import json
import pathlib

class Expense:

    def __init__(self, databaseFileName):
        print('Initialising class Expense...')
        self.databaseFileName = databaseFileName
        self.expenses = []

    def load_expenses_from_json_database(self):
        print('Loading expenses from json database file expenses.json')
        filepath = pathlib.Path.cwd() / self.databaseFileName
        if os.path.exists(filepath):
            print('Found file expenses.json')
            with open(self.databaseFileName, 'r') as file:
                self.expenses = json.load(file)
                print('Successfully read contents for expenses.json')
                print(f'{self.expenses}')
        else:
            print('Not able to find file expenses.json')
            self.expenses = []

