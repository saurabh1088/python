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
    logging.info(f"Reversing string {str}")

    # reversed_value = str[::-1]
    reversed_value = ''
    for char in str:
        reversed_value = char + reversed_value
    logging.info(f"Reversed value is {reversed_value}")

def some_method(str):
    reverse_string = str[::-1]
    if str == reverse_string:
        logging.info(f"{str} is a palindrome")
    else:
        logging.info(f"{str} is not a palindrome")

def some_method_with_several_params(first_name, last_name, age, address, phone_number):
    logging.info(f"First Name: {first_name}")
    logging.info(f"Last Name: {last_name}")
    logging.info(f"Age: {age}")
    logging.info(f"Address: {address}")
    logging.info(f"Phone Number: {phone_number}")

def some_method_with_integer_param(value):
    value_str = str(value)
    sum = 0
    for char in value_str:
        logging.info(f"Character: {char}")
        sum += int(char)
    logging.info(f"Sum of digits is: {sum}")

def character_frequency(str):
    logging.info("Starting programming session three")
    # Add your code here
    some_dictionary = dict()
    for char in str:
        logging.info(f"Character: {char}")
        some_dictionary[char] = some_dictionary.get(char, 0) + 1
    logging.info(f"Character frequencies: {some_dictionary}")

    logging.info("Programming session three completed")

def grab_even_from_list(list_of_numbers):
    logging.info("Starting practice session one")
    refined_list = [number for number in list_of_numbers if number % 2 == 0]
    logging.info(f"Refined list of even numbers: {refined_list}")
    logging.info("Practice session one completed")

def practice_session_one_9_september_2025():
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

def practice_session_two_9_september_2025():
    logging.info("Starting practice session two - 9 September 2025")
    # Add your code here
    x = 10
    y = 3
    result = x // y
    logging.info(f"Result of integer division {x} // {y} is {result}")
    # Lowercase vs Uppercase comparison, lowercase letters have higher ASCII values
    result_two = 'Python' > 'python'
    logging.info(f"Is 'Python' greater than 'python'? {result_two}")
    logging.info("Practice session two - 9 September 2025 completed")

def practice_session_three_9_september_2025():
    logging.info("Starting practice session three - 9 September 2025")
    for i in range(2, 5):
        print(i, end='-')
    some_list = list()
    some_list.append(1)
    some_list.append(2)
    some_list.append(3)
    logging.info(f"List contents: {some_list}")
    logging.info("Practice session three - 9 September 2025 completed")

def practice_session_one_10_september_2025():
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

def practice_session_two_10_september_2025():
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

# --------------------------------------------------------------------------------
# --- Main Functionality ---
def main():
    logging.info("Application started")
    practice_session_two_10_september_2025()
    logging.info("Application finished")


if __name__ == "__main__":
    main()

