# comments_and_variables.py
"""
This file introduces:
- Comments in Python (single-line and multi-line)
- Variables: how to declare, assign, and print them
- Rules and naming conventions for variables
"""

# ----------------------------
# 1. Comments
# ----------------------------

# This is a single-line comment
# Comments are ignored by the Python interpreter
# Use them to explain code or leave notes

"""
This is a multi-line comment or docstring.
Used for larger documentation blocks.
It can span multiple lines.
"""

# ----------------------------
# 2. Variables
# ----------------------------

# Variables store data in memory
# Syntax: variable_name = value

name = "Harshita"         # string
age = 21                  # integer
height = 5.4              # float
is_student = True         # boolean

# Print values of variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# ----------------------------
# 3. Type Checking
# ----------------------------

print(type(name))     # <class 'str'>
print(type(age))      # <class 'int'>
print(type(height))   # <class 'float'>
print(type(is_student))  # <class 'bool'>

# ----------------------------
# 4. Variable Naming Rules
# ----------------------------

# Valid names
first_name = "Harshita"
_firstName = "Harshita"
firstName1 = "Harshita"
# Invalid names (uncomment to see errors)
# 1name = "error"     # cannot start with a number
# first-name = "error"  # hyphens not allowed
# class = "error"     # reserved keyword

# ----------------------------
# 5. Dynamic Typing in Python
# ----------------------------

# Python allows reassigning different types to the same variable
x = 10
print(x, type(x))  # int
x = "Ten"
print(x, type(x))  # str

# ----------------------------
# 6. Constants (By Convention)
# ----------------------------

# Constants are usually written in all caps (not enforced)
PI = 3.14159
GRAVITY = 9.8

# ----------------------------
# 7. Exercise
# ----------------------------

# 1. Create variables for your favorite book name, rating (out of 5), and author
# 2. Print them using formatted strings
# 3. Try using invalid variable names to see errors (comment them later)
