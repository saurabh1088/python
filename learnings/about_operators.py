import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

"""
Exponentiation Operators Across Programming Languages
=====================================================

This documentation provides an overview of popular programming languages
and whether they support a dedicated exponentiation operator.

Summary
-------
Some languages provide a dedicated operator for exponentiation (raising
numbers to a power), while others require function calls. This can affect
readability, conciseness, and consistency in mathematical expressions.

Detailed Comparison
-------------------

+-----------------+------------------------+--------------------+-----------------------------------------------------+
| Language        | Exponentiation Operator| Example            | Notes                                               |
+=================+========================+====================+=====================================================+
| Python          | **                     | 2 ** 3 → 8         | Yes, dedicated operator.                            |
+-----------------+------------------------+--------------------+-----------------------------------------------------+
| Ruby            | **                     | 2 ** 3 → 8         | Same as Python.                                     |
+-----------------+------------------------+--------------------+-----------------------------------------------------+
| Perl            | **                     | 2 ** 3 → 8         | Dedicated operator available.                       |
+-----------------+------------------------+--------------------+-----------------------------------------------------+
| PowerShell      | ** (v7+), or `-shl`    | 2 ** 3 → 8         | PowerShell 7+ supports `**`. Older versions use .NET|
+-----------------+------------------------+--------------------+-----------------------------------------------------+
| MATLAB          | ^                      | 2 ^ 3 → 8          | Uses caret `^` for exponentiation.                  |
+-----------------+------------------------+--------------------+-----------------------------------------------------+
| R               | ^                      | 2 ^ 3 → 8          | Same as MATLAB.                                     |
+-----------------+------------------------+--------------------+-----------------------------------------------------+
| Fortran         | **                     | 2 ** 3 → 8         | One of the earliest languages with `**`.            |
+-----------------+------------------------+--------------------+-----------------------------------------------------+
| Lua             | ^ (or ** in Lua 5.3+)  | 2 ^ 3 → 8          | Supports both in newer versions.                    |
+-----------------+------------------------+--------------------+-----------------------------------------------------+
| Julia           | ^                      | 2 ^ 3 → 8          | Dedicated operator.                                 |
+-----------------+------------------------+--------------------+-----------------------------------------------------+
| Visual Basic    | ^                      | 2 ^ 3 → 8          | Built-in operator.                                  |
+-----------------+------------------------+--------------------+-----------------------------------------------------+
| Swift           | No operator            | pow(2, 3) → 8.0    | Uses `pow` function from C.                         |
+-----------------+------------------------+--------------------+-----------------------------------------------------+
| JavaScript      | ** (ES2016+)           | 2 ** 3 → 8         | Introduced in ECMAScript 2016.                      |
+-----------------+------------------------+--------------------+-----------------------------------------------------+
| C / C++         | No operator            | pow(2,3) → 8.0     | Use `pow()` from `<cmath>`.                         |
+-----------------+------------------------+--------------------+-----------------------------------------------------+
| Java            | No operator            | Math.pow(2,3)      | Use `Math.pow()`.                                   |
+-----------------+------------------------+--------------------+-----------------------------------------------------+
| Go              | No operator            | math.Pow(2,3)      | Use `math.Pow()`.                                   |
+-----------------+------------------------+--------------------+-----------------------------------------------------+
| Kotlin          | No operator            | Math.pow(2.0,3.0)  | Uses Java's math library.                           |
+-----------------+------------------------+--------------------+-----------------------------------------------------+
| Rust            | No operator            | 2u32.pow(3) → 8    | Uses `.pow()` method for integers.                  |
+-----------------+------------------------+--------------------+-----------------------------------------------------+
| Haskell         | ^ or **                | 2 ^ 3 → 8          | `^` for integers, `**` for floats.                  |
+-----------------+------------------------+--------------------+-----------------------------------------------------+

Key Takeaways
-------------

- Languages with dedicated exponentiation operators:
  Python, Ruby, Perl, Fortran, JavaScript (ES7+), MATLAB, R, Julia, Visual Basic.

- Languages that require functions for exponentiation:
  Swift, C, C++, Java, Go, Kotlin.

- In some cases, both operator and function exist (e.g., Lua, Haskell).

Notes
-----
In Python:
    result = 2 ** 3  # Evaluates to 8

The `**` operator is part of Python's core syntax, making mathematical
expressions concise and readable. This is one of Python's advantages over
languages where function calls like `Math.pow()` are required.
"""
def example_exponentiation():
    logging.info('--- Executing example_exponentiation ---')
    logging.info(f'2 to the power of 16 is : {2**16}')
    logging.info('----------------------------------------------')

def example_floor_division():
    logging.info('--- Executing example_floor_division ---')
    logging.info(f'Floor division of 10 by 3 is : {10 // 3}')
    logging.info('----------------------------------------------')

