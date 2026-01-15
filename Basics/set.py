# Drill 1: The "Unique ID" Cleaner (Basic & Duplicates)
# Goal: Use a set to automatically remove duplicates from a list.

raw_ids = [101, 102, 101, 103, 104, 102, 105]
unique_ids=set(raw_ids)
unique_ids.add(106)
unique_ids.add(103)
unique_ids.remove(102)
print("Final Set: ",unique_ids)
print("Length of set: ",len(unique_ids))


print("\n")


# Drill 2: The "Circle of Friends" (Set Operations)
# Goal: Perform mathematical set operations like Union and Intersection.


python_devs = {"Ali", "Zain", "Hamza", "Bilal"} 
web_devs = {"Hamza", "Bilal", "Usman", "Sara"}
unique_developers = python_devs | web_devs
full_stack= python_devs & web_devs
only_python_devs= python_devs - web_devs

print("List of different types of developers:")
print("Unique: ",unique_developers)
print("Full Stack: ",full_stack)
print("Python: ",only_python_devs)


print("\n")


# Drill 3: The "Frozen Vault" (Frozenset)
# Goal: Understand the difference between a normal set and a frozenset.
    
active_users = {"admin", "editor"}
active_users.add("guest")
permissions = frozenset(["read", "write", "execute"])
permissions.add("delete") # this will generate error because fronzen set is the immutable version of set so you cannot add or remove any element in frozenset
