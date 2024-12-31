import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

# Pointers behaviour against immutable data types
# ----------------------------------------------------------------------------------------------------------------------

# In the example below we are going to see how pointers behave over int types.
# Here numberOne is assigned a value of 10 and numberTwo is assigned the value of numberOne.
# At this point both numberOne and numberTwo are pointing to the same memory location.
# This can be verified by checking the address of numberOne and numberTwo which comes out to be same.
# Further when numberTwo is updated to 20, numberOne still holds the value 10 as numberTwo is pointing to a different memory location.
# This can be verified by checking the address of numberOne and numberTwo which comes out to be different.
# This behaviour is different from the behaviour of pointers over dict types or some other types.
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


def example_pointer_behaviour_over_string_types():
    stringOne = 'Hello'
    stringTwo = stringOne

    logging.info(f'stringOne is {stringOne}')
    logging.info(f'stringTwo is {stringTwo}')

    logging.info(f'Address of stringOne is {id(stringOne)}')
    logging.info(f'Address of stringTwo is {id(stringTwo)}')

    logging.info('Updating stringTwo...')

    stringTwo = 'World'

    logging.info('Values after update of stringTwo are:')
    logging.info(f'stringOne is {stringOne}')
    logging.info(f'stringTwo is {stringTwo}')

    logging.info(f'Address of stringOne is {id(stringOne)}')
    logging.info(f'Address of stringTwo is {id(stringTwo)}')

    logging.info('Checking if stringOne and stringTwo are pointing to the same memory location...')
    if id(stringOne) == id(stringTwo):
        logging.info('stringOne and stringTwo are pointing to the same memory location')
    else:
        logging.info('stringOne and stringTwo are pointing to different memory locations')


# Pointers behaviour against mutable data types
# ----------------------------------------------------------------------------------------------------------------------

# This example shows how pointers behave over dict types, which is different from the behaviour of pointers over int types.
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


# This example shows how pointers behave over list types, which is different from the behaviour of pointers over int types.
# Behaviour of pointers over list types is similar to the behaviour of pointers over dict types.
def example_pointer_behaviour_over_list_types():
    listOne = [1, 2, 3]
    listTwo = listOne

    logging.info(f'listOne is {listOne}')
    logging.info(f'listTwo is {listTwo}')

    logging.info(f'Address of listOne is {id(listOne)}')
    logging.info(f'Address of listTwo is {id(listTwo)}')

    logging.info('Updating listTwo...')

    listTwo[1] = 20

    logging.info('Values after update of listTwo are:')
    logging.info(f'listOne is {listOne}')
    logging.info(f'listTwo is {listTwo}')

    logging.info(f'Address of listOne is {id(listOne)}')
    logging.info(f'Address of listTwo is {id(listTwo)}')

    logging.info('Checking if listOne and listTwo are pointing to the same memory location...')
    if id(listOne) == id(listTwo):
        logging.info('listOne and listTwo are pointing to the same memory location')
    else:
        logging.info('listOne and listTwo are pointing to different memory locations')


# is keyword is used to check if two variables are pointing to the same memory location.
def example_pointers_check_reference_equality():
    dictOne = {'value': 10}
    dictTwo = dictOne

    logging.info(f'dictOne is {dictOne}')
    logging.info(f'dictTwo is {dictTwo}')

    logging.info(f'Address of dictOne is {id(dictOne)}')
    logging.info(f'Address of dictTwo is {id(dictTwo)}')

    logging.info('Checking if dictOne and dictTwo are pointing to the same memory location...')
    if dictOne is dictTwo:
        logging.info('dictOne and dictTwo are pointing to the same memory location')
    else:
        logging.info('dictOne and dictTwo are pointing to different memory locations')

