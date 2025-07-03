import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def example_generator_behaviour():
    for value in sequence_generator(10):
        print(value)

def sequence_generator(n):
    value = 0
    while value < n:
        yield value
        value += 1
