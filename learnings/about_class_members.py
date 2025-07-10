import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

# MARK: - Example 1: Calculator with Class Property and Class Methods
# Scenario: A utility class where certain operations or configurations
#           might need to be aware of the class itself or its shared state,
#           and could potentially be extended by subclasses.

class Calculator:
    """
    A utility class for performing common mathematical operations.
    It includes a class property for a global limit and class methods
    that operate on their input arguments or refer to the class property.
    """
    # Class Property (acts as a static property):
    # This value is shared across all instances and the class itself.
    # It's suitable for global configurations or constants.
    MAX_CALCULABLE_VALUE = 1_000_000

    def __init__(self, name="Default Calculator"):
        """
        An instance method. Instances can also access class properties.
        """
        self.name = name
        logging.info(f"Calculator instance '{self.name}' created.")

    # Class Method: `add`
    # Now takes `cls` as the first argument. This allows it to access
    # class properties like `MAX_CALCULABLE_VALUE` using `cls.MAX_CALCULABLE_VALUE`.
    @classmethod
    def add(cls, a, b):
        """
        Adds two numbers. Includes a check against the class's MAX_CALCULABLE_VALUE.
        """
        if a > cls.MAX_CALCULABLE_VALUE or b > cls.MAX_CALCULABLE_VALUE:
            # Using cls.MAX_CALCULABLE_VALUE ensures it respects potential subclass overrides
            # if MAX_CALCULABLE_VALUE were to be overridden (though not typical for constants).
            logging.warning(f"Input value(s) exceed {cls.__name__}.MAX_CALCULABLE_VALUE ({cls.MAX_CALCULABLE_VALUE}).")
            # In a real app, you might raise an error or handle differently
            # raise ValueError(f"Input exceeds {cls.__name__}'s MAX_CALCULABLE_VALUE")
        return a + b

    # Class Method: `is_positive`
    # While it doesn't strictly need `cls`, it's defined as a class method
    # to demonstrate the decorator's usage.
    @classmethod
    def is_positive(cls, num):
        """Checks if a number is positive."""
        # This method doesn't use 'cls' but is still a class method.
        # It could be overridden by subclasses if they had a different definition of "positive".
        return num > 0

    # Class Method: `get_limits_info`
    # Demonstrates a class method providing information derived from a class property.
    # Using `cls.MAX_CALCULABLE_VALUE` makes it robust if subclasses inherit/override.
    @classmethod
    def get_limits_info(cls):
        """Returns information about the calculator's operational limits."""
        return f"This {cls.__name__} operates within a maximum value of: {cls.MAX_CALCULABLE_VALUE}"

    # Instance Method: `perform_calculation`
    # Shows an instance method accessing class methods and properties.
    def perform_calculation(self, x, y):
        """Performs an addition using the class's add method and reports on limits."""
        logging.info(f"[{self.name}] Performing addition: {x} + {y}")

        # Calling a class method from an instance method.
        # Python automatically passes the class (Calculator in this case) as 'cls'.
        result = self.add(x, y) # Can call via self, Python resolves to class method

        logging.info(f"[{self.name}] Result: {result}")
        # Accessing class method via self or class name is fine
        logging.info(f"[{self.name}] Limits Info: {self.get_limits_info()}")
        return result

# --- Example function ---

def example_calculator_class_methods():
    logging.info('--- Executing example_calculator_class_methods ---')
    # Call class methods directly on the class
    calculated_sum = Calculator.add(10, 20)
    logging.info(f'Sum using Calculator.add: {calculated_sum}')
    logging.info(f'Is 100 positive: {Calculator.is_positive(100)}')
    logging.info(f'Is -20 positive: {Calculator.is_positive(-20)}')
    logging.info(Calculator.get_limits_info())
    logging.info('----------------------------------------------')

def example_class_methods_called_on_instance():
    logging.info('--- Executing example_class_methods_called_on_instance ---')
    logging.info('Creating calculator instance, class methods will be called over this instance')
    instance = Calculator() # Create an instance

    # Call class methods on an instance. Python automatically passes the class.
    logging.info(f'Sum using instance.add: {instance.add(10, 20)}')
    logging.info(f'Is 100 positive: {instance.is_positive(100)}')
    logging.info(f'Is -20 positive: {instance.is_positive(-20)}')
    logging.info(instance.get_limits_info())
    logging.info('----------------------------------------------------')

def example_calculator_instances_with_class_methods():
    logging.info('--- Executing example_calculator_instances_with_class_methods ---')
    some_calculator_instance = Calculator(name='scientific calculator')
    # Call instance method, which internally uses class methods
    some_calculator_instance.perform_calculation(10, 20)
    some_calculator_instance.perform_calculation(900_000, 200_000) # Will trigger warning
    logging.info('---------------------------------------------------------')

