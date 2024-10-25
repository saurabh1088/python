import os
import json

class Expense:

    def __init__(self, databaseFileName):
        self.databaseFileName = databaseFileName
        self.expenses = []

    def load_expenses_from_json_database(self):
        if os.path.exists(self.databaseFileName):
            with open(self.databaseFileName, 'r') as file:
                self.expenses = json.load(file)
        else:
            self.expenses = []
