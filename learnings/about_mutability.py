import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def example_immutable_new_variable_assignment_type_int():
    logging.info('--- Executing example_immutable_type_int ---')
    x = 10
    logging.info(f"x value: {x}")
    logging.info(f"x identity: {id(x)}")
    logging.info(f'Assigning x to new variable y')
    y = x
    logging.info(f"y value: {y}")
    logging.info(f"y identity: {id(x)}")
    if id(x) == id(y):
        if x == y:
            logging.info("x and y are having equal identity and value")
    logging.info('----------------------------------------------')

def example_immutable_modify_variable_type_int():
    """
        Demonstrates the immutability of integers in Python.

        This example shows that when one modifies an integer variable,
        Python creates a new integer object rather than changing the
        original object in place. The function logs the value and
        identity (memory address) of the integer variable before and
        after modification, illustrating that the identity changes,
        which is characteristic of immutable types.
    """
    logging.info('--- Executing example_immutable_modify_variable__type_int ---')
    x = 10
    logging.info(f"x value: {x}")
    logging.info(f"x identity: {id(x)}")
    logging.info(f'Modifying value of x')
    x = x + 1
    logging.info(f"x value: {x}")
    logging.info(f"x identity: {id(x)}")
    logging.info(f'Identity of x before and after modifying value is changed')
    logging.info('----------------------------------------------')