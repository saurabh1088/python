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

# Python dictionaries are ordered in Python 3.7 and later versions
def example_dictionary_order():
    logging.info('--- Executing example_dictionary_order ---')

    my_ordered_dict = {}
    my_ordered_dict['first'] = 10
    my_ordered_dict['second'] = 20
    my_ordered_dict['third'] = 30
    my_ordered_dict['fourth'] = 40
    my_ordered_dict['fifth'] = 50
    logging.info('--- Dictionary created with insertion order ---')
    logging.info(f"my_ordered_dict: {my_ordered_dict}")

    logging.info('--- Iterating over items (key-value pairs) ---')
    for key, value in my_ordered_dict.items():
        logging.info(f"key: {key}, value: {value}")

    logging.info('----------------------------------------------')

def example_dictionary_comprehension():
    logging.info('--- Executing example_dictionary_comprehension ---')
    squares = {x: x ** 2 for x in range(1, 11)}
    logging.info(f"Dictionary comprehension (squares): {squares}")
    logging.info('----------------------------------------------')

def example_dictionary_get_method():
    logging.info('--- Executing example_dictionary_get_method ---')
    simple_dictionary = {"name": "Batman", "age": 25, "power": "Rich"}
    logging.info(f'Who am I? : Because I am {simple_dictionary.get("name")}')

    # Accessing a key which isn't present in dictionary using [] notation will throw KeyError
    logging.info('Accessing key which is not in the dictionary')
    try:
        key_not_there = simple_dictionary["key_not_there"]
    except KeyError as e:
        logging.error(f"KeyError: {e}")
        logging.info('It seems that the key is not in the dictionary')
        logging.info('Better to use get() instead to avoid this error')

    logging.info(f'Accessing key which is not there : {simple_dictionary.get("key_not_there")}')
    logging.info('----------------------------------------------')

