# -------- Unpacking --------

# Unpacking is the process of assigning values from a collection (like a list or tuple) to individual variables in a single line of code.

# Example of unpacking a list
my_list = [1, 2, 3]
a, b, c = my_list
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Example of unpacking a tuple
my_tuple = ('Alice', 30, 'Engineer')
name, age, profession = my_tuple
print(name)       # Output: Alice
print(age)        # Output: 30
print(profession) # Output: Engineer

# Unpacking multiple values from a list
numbers = [10, 20, 30, 40, 50]
first, second, *rest = numbers
print(first)  # Output: 10
print(second) # Output: 20
print(rest)   # Output: [30, 40, 50]

