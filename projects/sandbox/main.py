"""
Practice exercises and algorithms module.

This module contains various Python programming exercises and practice functions
demonstrating string manipulation, list operations, dictionary usage, and
algorithm implementations. All functions use Python's logging module for output,
writing to both a debug.log file and the console.
"""

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
# --- Practice Area ---
def fizz_bizz():
    """
    Implement the FizzBuzz algorithm.
    
    Prompts the user for a number and prints numbers from 1 to that number.
    For multiples of 3, prints "Fizz"; for multiples of 5, prints "Buzz";
    for multiples of both 3 and 5, prints "FizzBuzz"; otherwise prints the number.
    
    The function reads input from stdin and requires user interaction.
    All output is logged using the logging module.
    
    Note:
        This function will raise ValueError if the input cannot be converted
        to an integer. No input validation is performed.
    """
    logging.info("Starting FizzBuzz")
    logging.info("Enter a number:")
    number = int(input())
    for i in range(1, number + 1):
        logging.info(f'Value of i: {i}')
        if i % 3 == 0 and i % 5 == 0:
            logging.info("FizzBuzz")
        elif i % 3 == 0:
            logging.info("Fizz")
        elif i % 5 == 0:
            logging.info("Buzz")
        else:
            logging.info(i)
    logging.info("FizzBuzz completed")

def reverse_string(str):
    """
    Reverse a string character by character.
    
    Takes a string and reverses it by iterating through each character
    and building a new string in reverse order. The result is logged.
    
    Args:
        str: The input string to be reversed.
    
    Note:
        The parameter name 'str' shadows Python's built-in str type.
        Consider using a different parameter name like 'text' or 'input_string'.
    """
    logging.info(f"Reversing string {str}")

    # reversed_value = str[::-1]
    reversed_value = ''
    for char in str:
        reversed_value = char + reversed_value
    logging.info(f"Reversed value is {reversed_value}")

def some_method(str):
    """
    Check if a string is a palindrome.
    
    Determines whether the input string reads the same forwards and backwards.
    Uses string slicing to reverse the string and compares it with the original.
    
    Args:
        str: The input string to check for palindrome property.
    
    Note:
        The function name 'some_method' is not descriptive. Consider renaming
        to 'check_palindrome' or 'is_palindrome'. The parameter name 'str'
        shadows Python's built-in str type.
    """
    reverse_string = str[::-1]
    if str == reverse_string:
        logging.info(f"{str} is a palindrome")
    else:
        logging.info(f"{str} is not a palindrome")

def some_method_with_several_params(first_name, last_name, age, address, phone_number):
    """
    Log personal information parameters.
    
    Takes multiple parameters representing personal information and logs
    each one separately. This function demonstrates handling multiple
    function parameters.
    
    Args:
        first_name: The person's first name.
        last_name: The person's last name.
        age: The person's age.
        address: The person's address.
        phone_number: The person's phone number.
    
    Note:
        The function name 'some_method_with_several_params' is not descriptive.
        Consider renaming to 'log_personal_info' or 'display_person_details'.
        For better structure, consider using a dataclass or named tuple
        to group related parameters.
    """
    logging.info(f"First Name: {first_name}")
    logging.info(f"Last Name: {last_name}")
    logging.info(f"Age: {age}")
    logging.info(f"Address: {address}")
    logging.info(f"Phone Number: {phone_number}")

def some_method_with_integer_param(value):
    """
    Calculate the sum of digits in an integer.
    
    Converts an integer to a string, iterates through each digit character,
    converts it back to an integer, and sums all the digits. Logs each
    character and the final sum.
    
    Args:
        value: An integer whose digits will be summed.
    
    Returns:
        None. The result is logged, not returned.
    
    Note:
        The function name 'some_method_with_integer_param' is not descriptive.
        Consider renaming to 'sum_digits' or 'calculate_digit_sum'.
        The variable name 'sum' shadows Python's built-in sum() function.
    """
    value_str = str(value)
    sum = 0
    for char in value_str:
        logging.info(f"Character: {char}")
        sum += int(char)
    logging.info(f"Sum of digits is: {sum}")

def character_frequency(str):
    """
    Count the frequency of each character in a string.
    
    Iterates through each character in the input string and counts how many
    times each character appears. Uses a dictionary to store character
    frequencies and logs each character as it's processed.
    
    Args:
        str: The input string to analyze for character frequencies.
    
    Returns:
        None. The character frequencies dictionary is logged, not returned.
    
    Note:
        The parameter name 'str' shadows Python's built-in str type.
        Consider using collections.Counter for a more Pythonic implementation.
    """
    logging.info("Starting programming session three")
    # Add your code here
    some_dictionary = dict()
    for char in str:
        logging.info(f"Character: {char}")
        some_dictionary[char] = some_dictionary.get(char, 0) + 1
    logging.info(f"Character frequencies: {some_dictionary}")

    logging.info("Programming session three completed")

def grab_even_from_list(list_of_numbers):
    """
    Filter a list to extract only even numbers.
    
    Uses a list comprehension to create a new list containing only the
    even numbers from the input list. An even number is one that is
    divisible by 2 (i.e., number % 2 == 0).
    
    Args:
        list_of_numbers: A list of integers to filter.
    
    Returns:
        None. The filtered list is logged, not returned.
    
    Note:
        The function name 'grab_even_from_list' could be more descriptive.
        Consider renaming to 'filter_even_numbers' or 'get_even_numbers'.
    """
    logging.info("Starting practice session one")
    refined_list = [number for number in list_of_numbers if number % 2 == 0]
    logging.info(f"Refined list of even numbers: {refined_list}")
    logging.info("Practice session one completed")

def list_and_string_practice_session():
    """
    Demonstrate various list and string operations.
    
    Performs multiple practice exercises:
    1. Filters even and odd numbers from a list using list comprehensions
    2. Extracts words longer than 3 characters from a sentence
    3. Flattens a two-dimensional list into a one-dimensional list
    
    All operations use list comprehensions and demonstrate Python's
    functional programming capabilities. Results are logged for each operation.
    
    This function serves as a practice session covering list comprehensions,
    string splitting, and nested list flattening.
    """
    logging.info("Starting practice session one - 9 September 2025")
    list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = [number for number in list_one if number % 2 == 0]
    logging.info(f"Even numbers from the list: {even_numbers}")
    odd_numbers = [number for number in list_one if number % 2 != 0]
    logging.info(f"Odd numbers from the list: {odd_numbers}")
    logging.info("Practice session one - 9 September 2025 completed")
    long_sentence = "This is a sample sentence for testing purposes, which contains several words."
    long_words = [word for word in long_sentence.split() if len(word) > 3]
    logging.info(f"Words longer than three characters: {long_words}")
    two_dimensional_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
    flattened_list = [number for sublist in two_dimensional_list for number in sublist]
    logging.info(f"Flattened list: {flattened_list}")
    logging.info("Practice session one - 9 September 2025 completed")

def integer_division_and_string_comparison():
    """
    Demonstrate integer division and string comparison operations.
    
    Shows two Python concepts:
    1. Integer division (//) which returns the floor division result
    2. String comparison which compares strings lexicographically using ASCII values
    
    The function demonstrates that:
    - Integer division 10 // 3 returns 3 (not 3.333...)
    - String comparison is case-sensitive, and lowercase letters have
      higher ASCII values than uppercase letters, so 'Python' > 'python' is False
    
    This is a practice session for understanding Python's division operators
    and string comparison behavior.
    """
    logging.info("Starting integer division and string comparison session")
    x = 10
    y = 3
    result = x // y
    logging.info(f"Result of integer division {x} // {y} is {result}")
    # Lowercase vs Uppercase comparison, lowercase letters have higher ASCII values
    result_two = 'Python' > 'python'
    logging.info(f"Is 'Python' greater than 'python'? {result_two}")
    logging.info("Integer division and string comparison session completed")

def list_and_range_practice_session():
    """
    Demonstrate range() function and list operations.
    
    Shows two concepts:
    1. Using range() to iterate through a sequence of numbers (2 to 4)
    2. Creating an empty list and appending elements to it
    
    The range(2, 5) generates numbers 2, 3, 4 (exclusive of end value).
    Elements are appended to a list one by one, demonstrating basic
    list manipulation.
    
    Note:
        This function uses print() instead of logging for the range output,
        which is inconsistent with other functions in this module.
    """
    logging.info("Starting practice session three - 9 September 2025")
    for i in range(2, 5):
        print(i, end='-')
    some_list = list()
    some_list.append(1)
    some_list.append(2)
    some_list.append(3)
    logging.info(f"List contents: {some_list}")
    logging.info("Practice session three - 9 September 2025 completed")

def dictionary_and_list_practice_session():
    """
    Demonstrate dictionary operations and list reversal.
    
    Shows two concepts:
    1. Dictionary operations: creating a dictionary, accessing items(),
       keys(), and values() methods
    2. List reversal using the reverse() method
    
    The function demonstrates:
    - Creating and populating a dictionary
    - Accessing dictionary views (items, keys, values)
    - Reversing a list in-place using reverse()
    
    Note:
        The variable name 'list' shadows Python's built-in list type.
        The variable 'reverse_list' will be None because list.reverse()
        modifies the list in-place and returns None. The reversed list
        is the original 'list' variable after modification.
    """
    logging.info("Starting practice session one - 10 September 2025")
    dictionary = dict()
    dictionary['a'] = 1
    dictionary['b'] = 2
    dictionary['c'] = 3
    items = dictionary.items()
    logging.info(f"Dictionary items: {items}")
    keys = dictionary.keys()
    logging.info(f"Dictionary keys: {keys}")
    values = dictionary.values()
    logging.info(f"Dictionary values: {values}")
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    reverse_list = list.reverse()
    logging.info(f"Reversed list: {list}")
    logging.info("Practice session one - 10 September 2025 completed")

def power_and_string_index_practice():
    """
    Demonstrate exponentiation, string indexing, and range with step.
    
    Shows three Python concepts:
    1. Exponentiation operator (**) to raise a number to a power
    2. String indexing to access a character at a specific position
    3. Range with step parameter: range(2, 16, 2) generates even numbers
       from 2 to 14 (inclusive start, exclusive end, step of 2)
    
    The function calculates 5^2 = 25, accesses the character at index 7
    of "Hello, World!" (which is 'W'), and iterates through even numbers.
    """
    logging.info("Starting practice session two - 10 September 2025")
    x = 5
    y = 2
    result = x ** y
    logging.info(f"Result of {x} raised to the power of {y} is {result}")
    some_string = "Hello, World!"
    logging.info(f'Value at index 7 is: {some_string[7]}')
    for i in range (2, 16, 2):
        logging.info(f"Current value of i: {i}")
    logging.info("Practice session two - 10 September 2025 completed")

def count_vowels_in_string():
    """
    Count the number of vowels in a predefined string.
    
    Counts lowercase vowels (a, e, i, o, u) in a hardcoded example string.
    The string is first trimmed of leading/trailing whitespace using strip(),
    then converted to lowercase before counting. Only lowercase vowels
    are counted (the function uses lowercase conversion).
    
    The function demonstrates:
    - String trimming with strip()
    - Case conversion with lower()
    - Character counting with iteration
    
    Returns:
        None. The vowel count is logged, not returned.
    """
    logging.info("Starting practice session one - 20 September 2025")
    list_of_vowels = ['a', 'e', 'i', 'o', 'u']
    some_string = " This is an example string to test vowel extraction. "
    trimmed_string = some_string.strip()
    logging.info(f"Original string: '{some_string}'")
    logging.info(f"Trimmed string: '{trimmed_string}'")
    count_of_vowels = 0
    for char in trimmed_string.lower():
        if char in list_of_vowels:
            count_of_vowels += 1
    logging.info(f"Number of vowels in the string: {count_of_vowels}")
    logging.info("Practice session one - 20 September 2025 completed")

def count_vowels_in_list_of_strings(list_of_strings):
    """
    Count vowels in each string from a list of strings.
    
    Iterates through a list of strings and counts the number of lowercase
    vowels (a, e, i, o, u) in each string. Each string is trimmed of
    whitespace and converted to lowercase before counting.
    
    Args:
        list_of_strings: A list of strings to analyze for vowel counts.
    
    Returns:
        None. The vowel count for each string is logged individually.
    
    The function processes each string independently, counting vowels
    and logging the result for each one.
    """
    logging.info("Starting practice session two - 20 September 2025")
    list_of_vowels = ['a', 'e', 'i', 'o', 'u']
    for string in list_of_strings:
        count = 0
        for char in string.strip().lower():
            if char in list_of_vowels:
                count += 1
        logging.info(f"String: '{string}' has {count} vowels")

    logging.info("Practice session two - 20 September 2025 completed")

def count_vowels_with_logging():
    """
    Count vowels in a string with detailed logging for each vowel found.
    
    Counts both uppercase and lowercase vowels (a, e, i, o, u) in a
    hardcoded example string. Unlike count_vowels_in_string(), this
    function counts vowels in their original case (both upper and lower).
    Each vowel found is logged individually, providing detailed output.
    
    The function demonstrates:
    - String trimming with strip()
    - Case-sensitive vowel detection (both upper and lowercase)
    - Detailed logging during iteration
    
    Returns:
        None. The total vowel count and individual vowel detections are logged.
    """
    logging.info("Starting practice session three - 20 September 2025")
    vowels = 'aeiouAEIOU'
    some_string = " This is another example string to test vowel extraction. "
    trimmed_string = some_string.strip()
    logging.info(f"Original string: '{some_string}'")
    logging.info(f"Trimmed string: '{trimmed_string}'")
    count = 0
    for char in trimmed_string:
        if char in vowels:
            count += 1
            logging.info(f"Vowel found: {char}")
    logging.info(f"Total number of vowels in the string: {count}")
    logging.info("Practice session three - 20 September 2025 completed")


# --------------------------------------------------------------------------------
# --- Prompts ---
# Suggest a more meaningful and descriptive name for the function based on its actual implementation details.

# --------------------------------------------------------------------------------
# --- Main Functionality ---
def main():
    """
    Main entry point for the application.
    
    Initializes the application, runs the default practice function
    (count_vowels_with_logging), and logs the application lifecycle.
    
    Currently configured to run count_vowels_with_logging() by default.
    Modify this function to call other practice functions as needed.
    """
    logging.info("Application started")
    count_vowels_with_logging()
    logging.info("Application finished")


if __name__ == "__main__":
    main()

