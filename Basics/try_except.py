# Drill 1: The "Crash Proof" Input
# Goal: Prevent the program from breaking if someone types letters into an int() input.

try:
    age = input("Enter age: ")
    age_int=int(age)
except ValueError:
    print("Error: Please enter numbers only!")
else:
    print("Age saved successfully!")


print("\n")


# Drill 2: The "Safe Division"
# Goal: Handle specific mathematical errors.

try:
    num=10/0
except ZeroDivisionError:
    print("Math Error: Cannot divide by zero!")


print("\n")


# Drill 3: The "Final Message" (Finally)
# Goal: Use the block that runs no matter what happens.

try:
    num=10/0
except ZeroDivisionError:
    print("Math Error: Cannot divide by zero!")
finally:
    print("System: Process Finished.")
