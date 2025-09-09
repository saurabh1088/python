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

def practice_session_one_8_september_2025(list_of_numbers):
    logging.info("Starting practice session one")
    refined_list = [number for number in list_of_numbers if number % 2 == 0]
    logging.info(f"Refined list of even numbers: {refined_list}")
    logging.info("Practice session one completed")
        

# --------------------------------------------------------------------------------
# --- Main Functionality ---
def main():
    logging.info("Application started")
    reverse_string('saurabh')
    some_method('madam')
    some_method_with_several_params('Saurabh', 'Verma', 40, '123 Street', '123-456-7890')
    some_method_with_integer_param(9876543210)
    character_frequency('hello world')
    practice_session_one_8_september_2025([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    practice_session_two_8_september_2025()
    logging.info("Application finished")


if __name__ == "__main__":
    main()

