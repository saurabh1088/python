import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def type_of_none():
    logging.info('This is about_none.type_of_none()')
    logging.info(f'Type of None is {type(None)}')

def singleton_nature_of_none():
    objectOne = None
    objectTwo = None
    objectThree = None
    # The is keyword is used to test if two variables refer to the same object.
    # is operator checks for identity, meaning it determines whether two variables point to the same object in memory.
    # The output of the below print statement will be True, because None is a singleton.
    assert objectOne is objectTwo is objectThree
    logging.info(f'objectOne is objectTwo is objectThree: {objectOne is objectTwo is objectThree}')

def result_type_of_functions_without_any_return():
    # The return value of a function without a return statement is None.
    # The output of the below print statement will be None.
    output = sample_function_not_returning_any_value()
    assert output is None
    if output is None:
        logging.info("Output of sample_function_not_returning_any_value() is None")
        logging.info(f'Type of output is {type(output)}')

def usage_as_variable_initialisation():
    # None can be used to initialise a variable. Here object is initialised with None till it is assigned a value.
    object = None
    logging.info(f'Value of object at beginning is {object}')
    logging.info('Assigning value to object...')
    object = 10
    logging.info('Value assigned to object')
    logging.info(f'Value of object is {object}')

def usage_as_in_boolean_context():
    # None is considered as False in a boolean context.
    if None:
        logging.info("None is True")
    else:
        logging.info("None is False")

def sample_function_not_returning_any_value():
    pass

