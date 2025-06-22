# type_casting_and_identity.py
"""
This file covers:
- Type casting (converting between data types)
- Type coercion (automatic conversion in expressions)
- Identity and memory addresses in Python
- Use of id() and isinstance()
"""

# ----------------------------
# 1. Type Casting (Explicit Conversion)
# ----------------------------

# int → str
num = 100
str_num = str(num)
print(str_num, type(str_num))

# str → int
str_val = "50"
int_val = int(str_val)
print(int_val, type(int_val))

# int → float
f = float(7)
print(f, type(f))

# str → float
s = "3.14"
f2 = float(s)
print(f2, type(f2))

# int → complex
c = complex(10)
print(c, type(c))

# ----------------------------
# 2. Type Coercion (Implicit Conversion)
# ----------------------------

# Python automatically converts int to float during operations
result = 10 + 3.5
print(result, type(result))

# Mixing integer and complex
complex_result = 5 + 2j + 10
print(complex_result, type(complex_result))

# ----------------------------
# 3. Identity in Python
# ----------------------------

# Every object has a unique identity (memory address)
a = 200
b = 200
print(id(a))
print(id(b))  # might be same due to interning of small integers
print(a is b)  # True in case of small integers (interned), may differ for large

# For strings (also interned in some cases)
x = "hello"
y = "hello"
print(id(x), id(y))
print(x is y)  # True (strings are immutable and reused)

# For new string objects
x = str("hello world")
y = str("hello world")
print(id(x), id(y))  # might differ
print(x is y)  # possibly False

# ----------------------------
# 4. isinstance() Function
# ----------------------------

# Used to check the data type of a variable
num = 42
print(isinstance(num, int))     # True
print(isinstance(num, float))   # False
print(isinstance("42", str))    # True

# ----------------------------
# 5. Exercise
# ----------------------------
# 1. Convert your name to a list of characters using list() and print it
# 2. Add an int and a float, print the result and its type
# 3. Check whether a variable is a complex number using isinstance()
