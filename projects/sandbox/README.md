# Python Sandbox Project

A learning and practice sandbox project containing Python exercises, object-oriented programming concepts, and a simple HTTP server implementation.

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Examples](#examples)

## 🎯 Overview

This project serves as a sandbox for Python learning and experimentation. It includes:

- **Object-Oriented Programming Concepts**: Demonstrations of class inheritance, class variables vs instance variables, abstract methods, and async programming
- **Practice Exercises**: Various Python programming exercises including FizzBuzz, string manipulation, list comprehensions, and more
- **Simple HTTP Server**: A basic web server implementation using Python's built-in `http.server` module

## 📁 Project Structure

```
sandbox/
├── class_concepts.py      # OOP concepts and demonstrations
├── main.py                # Practice exercises and algorithms
├── server/
│   ├── server.py         # HTTP server implementation
│   └── index.html        # Simple web page served by the server
└── README.md             # This file
```

## ✨ Features

### Class Concepts (`class_concepts.py`)
- **Inheritance**: Vehicle base class with Car and Bike subclasses
- **Abstract Methods**: Demonstration of abstract methods using `NotImplementedError`
- **Class Variables vs Instance Variables**: Multiple examples showing the difference and behavior
- **Async Programming**: Example of async/await with asyncio

### Practice Exercises (`main.py`)
- FizzBuzz implementation
- String reversal and palindrome checking
- Character frequency counting
- List comprehensions and filtering
- Dictionary operations
- Vowel counting in strings
- Integer division and string comparison
- Power operations and string indexing

### HTTP Server (`server/server.py`)
- Simple HTTP server using Python's built-in `http.server`
- Custom request handler for routing
- Serves static HTML files
- Configurable port (default: 8000)

## 🔧 Requirements

- Python 3.7+ (for asyncio support)
- No external dependencies required (uses only Python standard library)

## 🚀 Usage

### Running Class Concepts Examples

```bash
# Run the async function demonstration
python class_concepts.py
```

To use specific functions from `class_concepts.py`, you can import and call them:

```python
from class_concepts import example_car, example_bike, class_variables_playground

example_car()
example_bike()
class_variables_playground()
```

### Running Practice Exercises

```bash
# Run the main practice exercises
python main.py
```

The main script currently runs `count_vowels_with_logging()` by default. You can modify the `main()` function to run other exercises.

**Note**: The `fizz_bizz()` function requires user input, so it's not run by default.

### Running the HTTP Server

```bash
# Navigate to the server directory
cd server

# Run the server
python server.py
```

The server will start on port 8000 by default. Open your browser and navigate to:
- `http://localhost:8000/` - Serves the index.html page

To stop the server, press `Ctrl+C` in the terminal.

## 📄 File Descriptions

### `class_concepts.py`

Demonstrates object-oriented programming concepts in Python:

- **Vehicle Class**: Base class with abstract methods `start_engine()` and `stop_engine()`
- **Car and Bike Classes**: Concrete implementations of the Vehicle class
- **Example Functions**:
  - `example_vehicle()`: Shows what happens when calling abstract methods
  - `example_car()` / `example_bike()`: Demonstrates concrete implementations
  - `class_variables_playground()`: Shows how class variables work across inheritance
  - `instance_variables_playground()`: Demonstrates instance variable behavior
  - `can_instance_access_class_variable()`: Shows instance access to class variables
  - `can_instance_update_class_variable()`: Demonstrates that modifying via instance creates a new instance variable
  - `check_if_all_instance_member_get_new_instance_variable_when_class_variable_is_modified_via_instance()`: Tests class variable modification behavior
  - `override_behaviour_for_class_variables_via_subclasses()`: Shows class variable overriding in subclasses
  - `an_async_function_showing_coroutine()`: Async/await demonstration

### `main.py`

Contains various Python practice exercises with logging:

- **String Operations**: Reversal, palindrome checking, character frequency
- **List Operations**: Filtering, comprehensions, flattening 2D lists
- **Dictionary Operations**: Creating, accessing items, keys, and values
- **Algorithm Exercises**: FizzBuzz, vowel counting, digit sum calculation
- **Utility Functions**: Integer division, string comparison, power operations

All functions use Python's `logging` module, which writes to both `debug.log` file and console output.

### `server/server.py`

A simple HTTP server implementation:

- Uses Python's `http.server.SimpleHTTPRequestHandler`
- Custom handler that redirects root path (`/`) to `/index.html`
- Configurable via `use_custom_handler` flag
- Default port: 8000

### `server/index.html`

A simple, modern HTML page with:
- Responsive design
- Basic JavaScript interactivity
- "Say Hello" button that displays current time
- Clean, minimal styling

## 💡 Examples

### Example 1: Using Class Concepts

```python
from class_concepts import Car, Bike

# Create instances
car = Car()
bike = Bike()

# Call methods
car.start_engine()  # Output: Car is started
bike.start_engine()  # Output: Bike is started
```

### Example 2: Running Practice Functions

```python
from main import reverse_string, character_frequency, count_vowels_in_string

reverse_string("Hello")
character_frequency("programming")
count_vowels_in_string()
```

### Example 3: Custom Server Configuration

Edit `server/server.py` to change the port:

```python
PORT = 8080  # Change default port
```

## 📝 Notes

- The `main.py` file creates a `debug.log` file in the project root when executed
- Some functions in `main.py` use `logging.info()` extensively, which may produce verbose output
- The async function in `class_concepts.py` includes a 10-second sleep for demonstration purposes
- The server uses Python's built-in HTTP server, which is suitable for development but not production use

## 🔗 Author

Created by [Saurabh Verma](https://github.com/saurabh1088)

---

**Note**: This is a learning/practice project. Code may contain examples and experiments rather than production-ready implementations.

