# typesOfOperators.py
"""
This file demonstrates:
- Different types of operators in Python
- Arithmetic, Comparison, Logical, Assignment, Bitwise, Identity, Membership
- Example use cases and output explanation
"""

# ----------------------------
# 1. Arithmetic Operators
# ----------------------------
a = 10
b = 3
print("Addition:", a + b)         # 13
print("Subtraction:", a - b)      # 7
print("Multiplication:", a * b)   # 30
print("Division:", a / b)         # 3.333...
print("Floor Division:", a // b)  # 3
print("Modulus:", a % b)          # 1
print("Exponentiation:", a ** b)  # 1000

# ----------------------------
# 2. Comparison Operators
# ----------------------------
print("Equal:", a == b)           # False
print("Not Equal:", a != b)       # True
print("Greater:", a > b)          # True
print("Less:", a < b)             # False
print("Greater or Equal:", a >= b) # True
print("Less or Equal:", a <= b)   # False

# ----------------------------
# 3. Logical Operators
# ----------------------------
x = True
y = False
print("AND:", x and y)  # False
print("OR:", x or y)   # True
print("NOT:", not x)   # False

# ----------------------------
# 4. Assignment Operators
# ----------------------------
c = 5
c += 2  # c = c + 2
print("Add and assign:", c)
c *= 3  # c = c * 3
print("Multiply and assign:", c)
c -= 4
print("Subtract and assign:", c)
c /= 2
print("Divide and assign:", c)

# ----------------------------
# 5. Bitwise Operators
# ----------------------------
m = 5  # 101
n = 3  # 011
print("Bitwise AND:", m & n)   # 1
print("Bitwise OR:", m | n)    # 7
print("Bitwise XOR:", m ^ n)   # 6
print("Bitwise NOT:", ~m)      # -6
print("Left Shift:", m << 1)   # 10
print("Right Shift:", m >> 1)  # 2

# ----------------------------
# 6. Identity Operators
# ----------------------------
a = 100
b = 100
print("a is b:", a is b)       # True (due to interning)
print("a is not b:", a is not b)  # False

# ----------------------------
# 7. Membership Operators
# ----------------------------
name = "Harshita"
print("'H' in name:", 'H' in name)       # True
print("'z' not in name:", 'z' not in name) # True

# ----------------------------
# 8. Practice Exercises
# ----------------------------
# 1. Check if a given number is even using modulus.
# 2. Compare two strings lexicographically.
# 3. Use bitwise AND and OR on two user-input integers.
# 4. Write a function that demonstrates use of identity vs equality.
# 5. Try chaining multiple assignment operators (e.g., *=, -=) on a value.
