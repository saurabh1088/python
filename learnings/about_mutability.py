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
# --- Mutable/Immutable data types in Python ---

# |---------------------------------------------------------------------------------------------------------------------------------------------|
# | **Category**       | **Data Type**         | **Mutable?**        | **Notes**                                                                |
# |--------------------|-----------------------|---------------------|--------------------------------------------------------------------------|
# | **Numeric Types**  | `int`                 | ❌ Immutable        | Integers are immutable. Any arithmetic creates a new object.             |
# |                    | `float`               | ❌ Immutable        | Same as `int`; floating-point numbers cannot be modified in place.       |
# |                    | `complex`             | ❌ Immutable        | Complex numbers are immutable.                                           |
# | **Sequence Types** | `str`                 | ❌ Immutable        | Strings cannot be modified; concatenation creates a new string.          |
# |                    | `tuple`               | ❌ Immutable        | Tuples cannot be modified once created.                                  |
# |                    | `list`                | ✅ Mutable          | Lists allow in-place modifications (e.g., append, pop, slice assignment).|
# |                    | `range`               | ❌ Immutable        | Range objects are fixed after creation.                                  |
# | **Set Types**      | `set`                 | ✅ Mutable          | Supports adding/removing elements.                                       |
# |                    | `frozenset`           | ❌ Immutable        | Immutable version of `set`.                                              |
# | **Mapping Type**   | `dict`                | ✅ Mutable          | Key-value pairs can be added/removed/updated.                            |
# | **Boolean Type**   | `bool`                | ❌ Immutable        | Boolean values (`True`, `False`) are singletons and immutable.           |
# | **Binary Types**   | `bytes`               | ❌ Immutable        | Similar to strings, immutable sequence of bytes.                         |
# |                    | `bytearray`           | ✅ Mutable          | Mutable sequence of bytes.                                               |
# |                    | `memoryview`          | ✅ Mutable          | Can modify the underlying object if it’s mutable.                        |
# | **None Type**      | `NoneType`            | ❌ Immutable        | Only one instance `None`.                                                |
# |---------------------------------------------------------------------------------------------------------------------------------------------|


# --------------------------------------------------------------------------------
# --- Immutable types examples ---

def example_immutable_new_variable_assignment_type_int():
    """
    Demonstrates the behavior of variable assignment with immutable types (integers) in Python.

    This function logs the following steps:
    - Assigns an integer value to variable `x` and logs its value and identity (memory address).
    - Assigns `x` to a new variable `y` and logs `y`'s value and identity.
    - Checks and logs if both variables share the same identity and value.

    Key Concept:
    In Python, integers are immutable objects. Assigning one variable to another (e.g., `y = x`) does not create a new object;
    both variables reference the same integer object in memory. This is verified by comparing their identities using the `id()` function.
    """
    logging.info('--- Executing example_immutable_type_int ---')
    x = 10
    logging.info(f"x value: {x}")
    logging.info(f"x identity: {id(x)}")
    logging.info(f'Assigning x to new variable y')
    y = x
    logging.info(f"y value: {y}")
    logging.info(f"y identity: {id(x)}")
    if id(x) == id(y):
        if x == y:
            logging.info("x and y are having equal identity and value")
    logging.info('----------------------------------------------')

def example_immutable_modify_variable_type_int():
    """
        Demonstrates the immutability of integers in Python.

        This example shows that when one modifies an integer variable,
        Python creates a new integer object rather than changing the
        original object in place. The function logs the value and
        identity (memory address) of the integer variable before and
        after modification, illustrating that the identity changes,
        which is characteristic of immutable types.
    """
    logging.info('--- Executing example_immutable_modify_variable__type_int ---')
    x = 10
    logging.info(f"x value: {x}")
    logging.info(f"x identity: {id(x)}")
    logging.info(f'Modifying value of x')
    x = x + 1
    logging.info(f"x value: {x}")
    logging.info(f"x identity: {id(x)}")
    logging.info(f'Identity of x before and after modifying value is changed')
    logging.info('----------------------------------------------')


# --------------------------------------------------------------------------------
# --- Mutable types examples ---
def example_mutable_new_variable_assignment_type_list():
    """
        Demonstrates variable assignment behavior with mutable objects (specifically lists) in Python.

        In Python, variables are references to objects in memory. When a mutable object
        (e.g., a list) is assigned to another variable using the assignment operator `=`,
        both variables reference the same object. As a result, modifications made through
        one variable will affect the other since they share the same memory address.

        Steps:
            1. Create a list `list_a` and log its value and identity (memory address).
            2. Assign `list_a` to another variable `list_b`.
            3. Log the value and identity of `list_b`.
            4. Confirm that `list_a` and `list_b` refer to the same object by comparing
               their identities using the `id()` function.
            5. Log a message if both identity and value are equal.

        Key Takeaways:
            - Assignment of a mutable object to another variable does not create a copy.
            - Both variables share the same memory reference.
            - To create an independent copy, use `list.copy()` or `copy.deepcopy()`.

        Analogy:
            Think of `list_a` as a shared Google Doc. Assigning `list_a` to `list_b` is
            like sharing the same document link. Both `list_a` and `list_b` can modify
            the same content because they reference the same document (object).
    """
    logging.info('--- Executing example_mutable_new_variable_assignment_type_list ---')
    list_a = [1, 2, 3, 4, 5]
    logging.info(f"list_a value: {list_a}")
    logging.info(f"list_a identity: {id(list_a)}")
    logging.info(f'Assigning list_a to new variable list_b')
    list_b = list_a
    logging.info(f"list_b value: {list_b}")
    logging.info(f"list_b identity: {id(list_b)}")
    if id(list_a) == id(list_b):
        if list_a == list_b:
            logging.info("list_a and list_b are having equal identity and value")
    logging.info('----------------------------------------------')

