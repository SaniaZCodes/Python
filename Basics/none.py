# Drill 1: The "Identity Check" (Basics)
# Goal: Learn how to correctly check for None.

user_email=None
if user_email is None:
    print("Email is not provided.")
else:
    print(user_email)


print("\n")


# Drill 2: The "Function Default" (Practical Use)
# Goal: Use None as a placeholder for optional arguments.

def greet(name=None):
    if name is None:
        print("Hello, Guest!")
    else:
        print(f"Hello, {name}!")

greet()
greet("Sania")


print("\n")


# Drill 3: The "None Return" (Logic Check)
# Goal: Understand that functions return None by default.

def do_nothing():
    pass

result = do_nothing()
print(result)
print(type(result))
