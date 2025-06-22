# input_output_formatting.py
"""
This file demonstrates:
- Taking user input
- Printing with separators and end parameters
- String formatting: concatenation, .format(), and f-strings
"""

# ----------------------------
# 1. Basic Input and Output
# ----------------------------

# Taking a single input
name = input("Enter your name: ")
print("Hello,", name)

# Taking multiple inputs at once
name, age = input("Enter your name and age (comma separated): ").split(",")
print("Name:", name)
print("Age:", age)

# Converting input into integers or floats
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)

# ----------------------------
# 2. The print() Function
# ----------------------------

# Default behavior
print("Python", "is", "awesome")  # space-separated

# Using sep (separator)
print("Python", "is", "awesome", sep="-")

# Using end (ending character)
print("Hello", end=", ")
print("world!")

# ----------------------------
# 3. String Concatenation
# ----------------------------

# Using + (must convert non-str to str)
name = "Harshita"
age = 22
print("Hello " + name + ", you are " + str(age) + " years old.")

# ----------------------------
# 4. String Formatting
# ----------------------------

# Using .format() - Python 3+
print("Hello {}, you are {} years old.".format(name, age))

# Using f-strings - Python 3.6+
print(f"Hello {name}, you are {age} years old.")

# ----------------------------
# 5. Practice Exercises
# ----------------------------
# 1. Ask user for their city and favorite food, print a formatted sentence.
# 2. Take two float inputs and print their product using f-strings.
# 3. Try printing 5 values separated by colon (:) and ending with a smiley.
