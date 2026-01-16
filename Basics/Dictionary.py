# Drill 1: The "Digital ID Card" (Basic & Access)
# Goal: Practice creating, accessing, and modifying dictionary data.

user = {
    "name": "Zain", 
    "age": 20, 
    "city": "Haripur", 
    "is_student": True
}
print("User's City: ",user["city"])
user["age"]=21
user["skills"]=["Python", "HTML"]
user.pop("is_student")
print(user)


print("\n")


# Drill 2: The "Inventory Manager" (Loops & Methods)
# Goal: Learn how to iterate through keys and values efficiently.

stock = {
    "Apples": 50, 
    "Bananas": 30, 
    "Oranges": 40
    }
print("List of Fruits:")
for x in stock.keys():
    print(x)

total=0

for x in stock.values():
    total=total+1

print("Total number of fruits: ",total)

for x,y in stock.items():
    print("We have",x,"units of",y)


print("\n")


# Drill 3: The "Nested Database" (Complexity & Safety)
# Goal: Handle nested data and prevent code crashes.

employees={
    101:{"name": "Ali", "role": "Dev"},
    102:{"name": "Sania","role": "Python"}
}

print(employees[101]["role"])
print(employees.get(103,"Employee not found"))
employees[103]={"name": "Jinnah","role": "Flutter"}

print(employees.items())
