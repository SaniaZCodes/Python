import math 

# Drill 1: The "Rounding Duo" (ceil & floor)
#  Goal: Understand the difference between rounding up and rounding down regardless of decimals.   

val=7.1
print("Using ceil(): ", math.ceil(val))
print("Using floor(): ", math.floor(val))


print("\n")

# Drill 2: Power and Roots
# Goal: Use specialized functions for exponents and square roots.

x=math.sqrt(144)
print("Square root of 144: ",x)
y=math.pow(2,5)
print("2^5 = ",y)


print("\n")


# Drill 3: Constants & Absolute Values
# Goal: Use built-in mathematical constants and the absolute value function.


print("Value of pi: ", math.pi)
z=abs(-50)
print("Using abs(): ",z)
area=(math.pi)*(math.pow(z,2))
print("Area: ",area)
