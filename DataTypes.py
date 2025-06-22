# dataTypes.py
"""
Covers all built-in data types in Python with examples:
- Numeric (int, float, complex)
- Sequence (str, list, tuple, range)
- Set (set, frozenset)
- Mapping (dict)
- Boolean (bool)
- Binary (bytes, bytearray, memoryview)
- NoneType
"""

# Numeric Types
num_int = 10
num_float = 3.14
num_complex = 2 + 3j
print("Integer:", num_int, type(num_int))
print("Float:", num_float, type(num_float))
print("Complex:", num_complex, type(num_complex))

# Sequence Types
s = "Hello"
l = [1, 2, 3]
t = (1, 2, 3)
r = range(5)
print("String:", s, type(s))
print("List:", l, type(l))
print("Tuple:", t, type(t))
print("Range:", list(r), type(r))

# Set Types
set_mutable = {1, 2, 3}
set_immutable = frozenset([1, 2, 3])
print("Set:", set_mutable, type(set_mutable))
print("Frozenset:", set_immutable, type(set_immutable))

# Mapping Type
d = {"name": "Harshita", "age": 22}
print("Dictionary:", d, type(d))

# Boolean Type
is_true = True
is_false = False
print("Boolean True:", is_true, type(is_true))
print("Boolean False:", is_false, type(is_false))

# Binary Types
byte_data = b"Hello"
byte_array = bytearray([65, 66, 67])
memory = memoryview(byte_array)
print("Bytes:", byte_data, type(byte_data))
print("Bytearray:", byte_array, type(byte_array))
print("Memoryview:", memory, type(memory))

# NoneType
nothing = None
print("NoneType:", nothing, type(nothing))

# Type conversion examples
print("int(3.9):", int(3.9))
print("float('2.5'):", float("2.5"))
print("str(100):", str(100))
