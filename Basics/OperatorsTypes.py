# Arithmetic operator,  Assignment operator
radius=7.2
pi=3.14
Area=pi*(radius**2)
print("Radius: ",radius)
print("Area: ",Area)

print("\nAfter using assignment operator on radius value")
radius+=3
print("Radius: ",radius)
Area=pi*(radius**2)
print("Area: ",Area)


# Comparison operator, Logical operator 
num= int(input("\nEnter number: "))
print((num > 10 and num < 50) or (num == 100))


# Membership operator, Identity operator
message="Python is amazing"
print("\nMessage",message)
print("Is the word 'is' in the message: ", ('is' in message))
x=500
y=500
print("x: ",x)
print("y: ",y)
print("x is y: ",(x is y))
