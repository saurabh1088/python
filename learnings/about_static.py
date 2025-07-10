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
    # This is a class variable, acting as a static property.
    # It is shared by all instances and the class itself.
    MAX_VALUE = 1000

    # A static method for a mathematical operation addition
    @staticmethod
    def add(a, b):
        if a > Calculator.MAX_VALUE or b > Calculator.MAX_VALUE:
            raise ValueError("Invalid arguments")
        return a + b

    @staticmethod
    def is_positive(num):
        return num > 0

