# Drill 1: The "Type Trap"
# Goal: Mastering type conversion (Casting).

birth_year=int(input("Enter your birth year: "))
age=2026-birth_year
print("You are ",age," years old.")


print("\n")


# Drill 2: The "Splitter" (Multiple Inputs)
# Goal: Capture multiple values in one single line.

colors=input("Enter three colors separated by a space: ")
colors_list=colors.split(" ")
print("Colors List: ",colors_list)
print("Second color in list: ", colors_list[1])


print("\n")


# Drill 3: The "Password Mask" (Concept)
# Goal: Handling sensitive data logic.

password=input("Set a password: ")
confirm_password=input("Enter password again to confirm it: ")
if password==confirm_password:
    print("Password set successfully!")
else:
    print("Password do not match.")
