import os
import json
import pathlib
import logging

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

