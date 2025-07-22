import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def example_dictionary_creation_literal():
    logging.info('--- Executing example_dictionary_creation_literal ---')
    simple_dictionary = {"name": "Batman", "age": 25, "power": "Rich"}
    logging.info(f"simple_dictionary: {simple_dictionary}")
    logging.info('----------------------------------------------')

def example_dictionary_creation_constructor():
    logging.info('--- Executing example_dictionary_creation_constructor ---')
    simple_dictionary = dict(name="Batman", age=25, power="Rich")
    logging.info(f"simple_dictionary with dict(): {simple_dictionary}")
    logging.info('----------------------------------------------')
