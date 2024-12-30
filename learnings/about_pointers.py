import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def example_pointer_behaviour_over_int_types():
    numberOne = 10
    numberTwo = numberOne

    logging.info(f'numberOne is {numberOne}')
    logging.info(f'numberTwo is {numberTwo}')

    logging.info(f'Address of numberOne is {id(numberOne)}')
    logging.info(f'Address of numberTwo is {id(numberTwo)}')

    logging.info('Updating numberTwo...')

    numberTwo = 20

    logging.info('Values after update of numberTwo are:')
    logging.info(f'numberOne is {numberOne}')
    logging.info(f'numberTwo is {numberTwo}')

    logging.info(f'Address of numberOne is {id(numberOne)}')
    logging.info(f'Address of numberTwo is {id(numberTwo)}')

    logging.info('Checking if numberOne and numberTwo are pointing to the same memory location...')
    if id(numberOne) == id(numberTwo):
        logging.info('numberOne and numberTwo are pointing to the same memory location')
    else:
        logging.info('numberOne and numberTwo are pointing to different memory locations')

