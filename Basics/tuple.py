# The "Unchangeable" Lock (Basic & Immutability)
# Goal: Prove that tuples cannot be modified once created.

coordinates = (10.5, 20.8, 30.0)
co_list=list(coordinates)
co_list[0]=15.0
coordinates=tuple(co_list)
if 20.8 in coordinates:
    print("Yes 20.8 is present")
else:
    print("No 20.8 is present")
print("Lenght: ",len(coordinates))


print("\n")


# The "Data Unpacking" (Tuple Unpacking)
# Goal: Extract values from a tuple directly into variables.

user_profile = ("John", 25, "Software Engineer")
(name, age, job)= user_profile
print(f"User {name} is {age} years old and works as a {job}.")

numbers=(1,2,3,4,5)
(a,*middle,b)=numbers
print(a)
print(middle)
print(b)


print("\n")


# The "Tuple Hack" (Converting to List)
# Goal: Learn the only way to "edit" a tuple.

colors = ("Red", "Green", "Blue")
temp_list=list(colors)
temp_list.append("Yellow")
colors=tuple(temp_list)
print(colors)
