# Different_Operators_On_different_dataType.py
"""
This file demonstrates how operators behave differently across data types:
- int
- float
- str
- list
- set
- bool
"""

# ----------------------------
# 1. Arithmetic Operators
# ----------------------------
print("Integer + Integer:", 2 + 3)  # 5
print("Float + Integer:", 2.5 + 3)  # 5.5
print("String + String:", "Hello " + "World")  # Hello World
print("List + List:", [1, 2] + [3, 4])  # [1, 2, 3, 4]
# print("String + Int:", "age: " + 25) → TypeError

# ----------------------------
# 2. Multiplication (*)
# ----------------------------
print("Int * Int:", 4 * 5)  # 20
print("String * Int:", "ha" * 3)  # hahaha
print("List * Int:", [1] * 4)  # [1, 1, 1, 1]
# print([1, 2] * [2]) → TypeError

# ----------------------------
# 3. Comparison Operators
# ----------------------------
print("2 == 2.0:", 2 == 2.0)  # True (value equality)
print("2 is 2.0:", 2 is 2.0)  # False (different types)
print("[1,2] == [1,2]:", [1,2] == [1,2])  # True
print("[1,2] is [1,2]:", [1,2] is [1,2])  # False

# ----------------------------
# 4. Membership Operators
# ----------------------------
print("'a' in 'apple':", 'a' in 'apple')  # True
print("2 in [1,2,3]:", 2 in [1,2,3])  # True
print("3 in {1, 2, 4}:", 3 in {1, 2, 4})  # False

# ----------------------------
# 5. Logical Operators
# ----------------------------
print("True and False:", True and False)  # False
print("1 and 0:", 1 and 0)  # 0
print("0 or 2:", 0 or 2)  # 2
print("'' or 'yes':", '' or 'yes')  # 'yes'

# ----------------------------
# 6. Bitwise Operators (Only on int)
# ----------------------------
print("5 & 3:", 5 & 3)  # 1
# print("5.0 & 3:", 5.0 & 3) → TypeError

# ----------------------------
# 7. Identity Operators
# ----------------------------
x = 100
y = 100
print("x is y:", x is y)  # True (interned)
x = 1000
y = 1000
print("x is y:", x is y)  # False (outside interning range)

# ----------------------------
# 8. Practice
# ----------------------------
# Try: "a" * True, [1] * False, and check results
print("'a' * True:", 'a' * True)  # 'a'
print("[1] * False:", [1] * False)  # []

# Summary:
# - Operator behavior can vary by data type
# - Know which types are compatible with which operator to avoid errors
