import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

# --------------------------------------------------------------------------------
# --- Example functions ---

def example_lists_simple_concepts():
    logging.info('--- Executing example_lists_simple_concepts ---')
    logging.info('Creating a simple list')
    simple_list_numbers = [1, 2, 3]
    simple_list_strings = ['Batman', 'Superman', 'Wonder Woman']
    simple_list_mixed_types = [1, 1.0, 'Iron Man', 200, simple_list_numbers]
    logging.info(f'simple_list_numbers = {simple_list_numbers}')
    logging.info(f'simple_list_strings = {simple_list_strings}')
    logging.info(f'simple_list_mixed_types = {simple_list_mixed_types}')
    logging.info('----------------------------------------------')

def example_lists_mutability():
    """
    Demonstrates the concept of mutability in Python lists by showing
    that multiple variables can reference the same object.

    Changes made via one variable are reflected in all other variables
    that reference the same list object. The object ID is logged to
    prove that both variables point to the exact same location in memory.
    """
    logging.info('--- Executing example_lists_mutability ---')

    # Creating a list and a second variable referencing the same list
    original_list = ['A', 'B', 'C']
    list_alias = original_list

    # Logging the initial state and IDs for original_list and list_alias
    logging.info(f'original_list = {original_list}, ID = {id(original_list)}')
    logging.info(f'list_alias = {list_alias}, ID = {id(list_alias)}')

    # Now updating the original_list
    logging.info('Updating the list `original_list`...')
    original_list[0] = '₹'

    # Showing that the change is visible through both variables
    logging.info(f'original_list after update = {original_list} ID = {id(original_list)}')
    logging.info(f'list_alias after update = {list_alias} ID = {id(list_alias)}')

    logging.info('----------------------------------------------')


# --------------------------------------------------------------------------------
# --- Entry point ---

def main():
    logging.info('This is entry point for lists examples')
    example_lists_simple_concepts()
    example_lists_mutability()


if __name__ == '__main__':
    main()

