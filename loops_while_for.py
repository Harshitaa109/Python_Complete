# loops_while_for.py
"""
This file covers:
- while loop
- for loop
- range() function
- break, continue, pass
- else with loop
- nested loops
- real-life exercises
"""

# ---------------------------
# 1. while loop
# ---------------------------
i = 1
while i <= 5:
    print("Hello,", i)
    i += 1

# Sum of numbers from 1 to n using while loop
n = int(input("Enter a number: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Sum:", total)

# ---------------------------
# 2. for loop with range()
# ---------------------------
for i in range(1, 6):  # start=1, stop=6 (exclusive)
    print(f"Square of {i} is {i*i}")

# Iterate through a string
for char in "Python":
    print(char)

# ---------------------------
# 3. break statement
# ---------------------------
for i in range(1, 10):
    if i == 5:
        print("Breaking at", i)
        break
    print("Number:", i)

# ---------------------------
# 4. continue statement
# ---------------------------
for i in range(1, 6):
    if i == 3:
        continue  # skip this iteration
    print("i:", i)

# ---------------------------
# 5. pass statement
# ---------------------------
for i in range(3):
    pass  # useful as a placeholder in loops or functions

# ---------------------------
# 6. else with loop
# ---------------------------
for i in range(3):
    print(i)
else:
    print("Loop finished without break")

# Loop with break (else won't run)
for i in range(3):
    print(i)
    if i == 1:
        break
else:
    print("This will not run because break occurred.")

# ---------------------------
# 7. Nested loops
# ---------------------------
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()

# ---------------------------
# 8. Practical Exercises
# ---------------------------

# 1. Print multiplication table
num = int(input("Enter number for multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# 2. Count digits in an integer using while
num = int(input("Enter a number to count digits: "))
count = 0
temp = num
while temp > 0:
    temp //= 10
    count += 1
print(f"{num} has {count} digits.")

# 3. Print all even numbers between 1 and 20
print("Even numbers from 1 to 20:")
for i in range(2, 21, 2):
    print(i, end=" ")
print()

# ---------------------------
# End of file
# ---------------------------
