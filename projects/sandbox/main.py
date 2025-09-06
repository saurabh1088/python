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

def some_other_function():
    value = 'saurabh'
    logging.info(f"Value is {value}")

    # reversed_value = value[::-1]
    reversed_value = ''
    for char in value:
        reversed_value = char + reversed_value
    logging.info(f"Reversed value is {reversed_value}")

# --------------------------------------------------------------------------------
# --- Main Functionality ---
def main():
    logging.info("Application started")
    some_other_function()
    logging.info("Application finished")


if __name__ == "__main__":
    main()

