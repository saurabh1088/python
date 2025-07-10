import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def example_calculator_static_methods():
    print(Calculator.add(10, 20))
    print(Calculator.is_positive(100))
    print(Calculator.is_positive(-20))

def example_static_methods_called_on_instance():
    instance = Calculator()
    print(instance.add(10, 20))
    print(instance.is_positive(100))
    print(instance.is_positive(-20))

class Calculator:
    # A static method for a mathematical operation addition
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_positive(num):
        return num > 0

