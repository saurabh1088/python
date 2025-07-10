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
    logging.info('Executing method example_calculator_static_methods')
    calculated_sum = Calculator.add(10, 20)
    logging.info(f'Sum using Calculator static method is {calculated_sum}')
    logging.info(f'Is 100 positive {Calculator.is_positive(100)}')
    logging.info(f'Is -20 positive {Calculator.is_positive(-20)}')

def example_static_methods_called_on_instance():
    logging.info('Executing method example_static_methods_called_on_instance')
    logging.info('Creating calculator instance, static methods will be called over this instance')
    instance = Calculator()

    logging.info(f'Sum using Calculator static method on instance is {instance.add(10, 20)}')
    logging.info(f'Is 100 positive {instance.is_positive(100)}')
    logging.info(f'Is -20 positive {instance.is_positive(-20)}')

def example_calculator_instances():
    logging.info('Executing method example_calculator_instances')
    some_calculator_instance = Calculator(name='scientific calculator')
    print(some_calculator_instance.add(10, 20))

class Calculator:
    """
    A utility class for performing common mathematical operations.
    It includes a static property for a global limit and static methods
    that operate purely on their input arguments or refer to the static property.
    """
    # This is a class variable, acting as a static property.
    # It is shared by all instances and the class itself.
    MAX_CALCULABLE_VALUE = 1_000_000

    def __init__(self, name="Default Calculator"):
        """
        An instance method to demonstrate that instances can also access static properties.
        """
        self.name = name
        print(f"Calculator instance '{self.name}' created.")

    # A static method for a mathematical operation addition
    # Operates purely on input parameters. Does not need 'self' or 'cls'.
    @staticmethod
    def add(a, b):
        if a > Calculator.MAX_CALCULABLE_VALUE or b > Calculator.MAX_CALCULABLE_VALUE:
            raise ValueError("Invalid arguments")
        return a + b

    @staticmethod
    def is_positive(num):
        return num > 0

    # Static Method: `get_limits_info`
    # Demonstrates a static method providing information derived from a static property.
    @staticmethod
    def get_limits_info():
        """Returns information about the calculator's operational limits."""
        return f"This calculator operates within a maximum value of: {Calculator.MAX_CALCULABLE_VALUE}"

    # Instance Method: `perform_calculation`
    # Shows an instance method accessing a static property.
    def perform_calculation(self, x, y):
        """Performs an addition using the static add method and reports on limits."""
        print(f"[{self.name}] Performing addition: {x} + {y}")

        # Calling a static method from an instance method
        result = Calculator.add(x, y)
        print(f"[{self.name}] Result: {result}")

        # Accessing static method
        print(f"[{self.name}] Limits Info: {Calculator.get_limits_info()}")
        return result


