import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def example_simple_generator():
    for value in simple_generator():
        print(value)

def example_generator_behaviour():
    for value in sequence_generator(10):
        print(value)

def sequence_generator(n):
    value = 0
    while value < n:
        yield value
        value += 1

def simple_generator():
    print("simple_generator starting generator...")
    yield 1
    print("simple_generator continuing generator...")
    yield 2
    print("simple_generator finishing generator...")
    yield 3
