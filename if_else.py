# if_else.py
"""
This script demonstrates Python's decision-making statements:
- if statement
- if-else statement
- if-elif-else ladder
- nested if
- practical and logical examples for revision
"""

# -------------------------
# 1. Simple if statement
# -------------------------
age = 20
if age >= 18:
    print("You are eligible to vote.")  # Output will be printed

# -------------------------
# 2. if-else statement
# -------------------------
temperature = 28
if temperature > 30:
    print("It's a hot day.")
else:
    print("It's a pleasant day.")  # This branch runs because 28 <= 30

# -------------------------
# 3. if-elif-else ladder
# -------------------------
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")  # This branch will run
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")

# -------------------------
# 4. Nested if example
# -------------------------
username = "harshita"
password = "admin123"

if username == "harshita":
    if password == "admin123":
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")

# -------------------------
# 5. Logical Operators in Conditions
# -------------------------
age = 22
country = "India"

if age > 18 and country == "India":
    print("You can apply for a driving license.")

# -------------------------
# 6. One-liner if-else (Ternary Operator)
# -------------------------
number = 7
parity = "Even" if number % 2 == 0 else "Odd"
print(f"{number} is {parity}")

# -------------------------
# 7. Practice Exercises
# -------------------------

# Exercise 1: Check if a number is positive, negative, or zero
n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# Exercise 2: Check if a year is a leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")

# Exercise 3: Check if character is vowel or consonant
ch = input("Enter a single character: ").lower()
if ch in 'aeiou':
    print(f"{ch} is a vowel.")
elif ch.isalpha():
    print(f"{ch} is a consonant.")
else:
    print("Not a valid alphabet.")

# -------------------------
# End of file
# -------------------------
