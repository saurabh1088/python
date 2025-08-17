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

def example_lists_comprehension():
    logging.info('--- Executing example_lists_comprehension ---')
    list_using_comprehension = [x**2 for x in range(10)]
    list_using_comprehension_and_filter = [x**2 for x in range(20) if x % 2 == 0]
    logging.info(f'list_using_comprehension = {list_using_comprehension}')
    logging.info(f'list_using_comprehension_and_filter = {list_using_comprehension_and_filter}')
    logging.info('----------------------------------------------')


# --------------------------------------------------------------------------------
# --- Challenge ---

# Write a list comprehension to extract all vowels from the string "Python is amazing!".
def challenge_lists_comprehension_and_filter():
    logging.info('--- Executing challenge_lists_comprehension_and_filter ---')
    vowels = [character for character in "Python is amazing!" if character.lower() not in 'aeiou']
    logging.info(f'vowels = {vowels}')
    logging.info('----------------------------------------------')

# Generate Fibonacci sequence using lists
def challenge_fibonacci_sequence(n=10):
    """
    Generates the Fibonacci sequence up to n elements using a list.

    The sequence starts with 0 and 1, and each subsequent number is the
    sum of the two preceding ones.

    Args:
        n (int): The number of elements to generate in the sequence.
                 Defaults to 10.
    """
    logging.info('--- Executing challenge_fibonacci_sequence ---')

    if n <= 0:
        logging.info("Please provide a positive number of elements.")
        return []

    fib_list = [0, 1]

    # Generate the sequence by appending the sum of the last two elements
    # Here fib_list[-1] is the most recent number; fib_list[-2] is the second most recent.
    while len(fib_list) < n:
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)

    logging.info(f'Fibonacci sequence up to {n} elements: {fib_list}')
    logging.info('----------------------------------------------')

    return fib_list



# --------------------------------------------------------------------------------
# --- Entry point ---

def main():
    logging.info('This is entry point for lists examples')
    example_lists_simple_concepts()
    example_lists_mutability()
    example_lists_comprehension()
    challenge_lists_comprehension_and_filter()
    challenge_fibonacci_sequence()


if __name__ == '__main__':
    main()

