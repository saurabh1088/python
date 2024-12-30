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


def example_pointer_behaviour_over_dict_types():
    dictOne = {'value': 10}
    dictTwo = dictOne

    logging.info(f'dictOne is {dictOne}')
    logging.info(f'dictTwo is {dictTwo}')

    logging.info(f'Address of dictOne is {id(dictOne)}')
    logging.info(f'Address of dictTwo is {id(dictTwo)}')

    logging.info('Updating dictTwo...')

    dictTwo['value'] = 20

    logging.info('Values after update of dictTwo are:')
    logging.info(f'dictOne is {dictOne}')
    logging.info(f'dictTwo is {dictTwo}')

    logging.info(f'Address of dictOne is {id(dictOne)}')
    logging.info(f'Address of dictTwo is {id(dictTwo)}')

    logging.info('Checking if dictOne and dictTwo are pointing to the same memory location...')
    if id(dictOne) == id(dictTwo):
        logging.info('dictOne and dictTwo are pointing to the same memory location')
    else:
        logging.info('dictOne and dictTwo are pointing to different memory locations')

        