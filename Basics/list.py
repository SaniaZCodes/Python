# The "List Surgeon" (Methods & Slicing)
# Goal: Perform a series of "operations" on a list to transform it.

tools = ["Python", "Java", "C++", "HTML"]
tools.append("JavaScript")
tools.insert(1,"SQL")
web_stack=tools[1:]
web_stack.remove("Java")
print(tools)
print(web_stack)


print("\n")


# The "Guest List" Manager (Popping & Sorting)
# Goal: Manage a list dynamically.


guests = ["Ali", "Zain", "Hamza", "Bilal"]
guests.sort()
guests.append("Usman")
guests.sort()
name=guests.pop(2)
print(name," has cancelled.")
guests.reverse()
print("Final Guest List: ",guests)
print("Number of Guests: ",len(guests))


print("\n")


# The "Memory Trap" (Identity vs. Copying)
# Goal: Prove you understand how Python handles list memory (References).

list_a = [1, 2, 3]
list_b = list_a
list_c = list_a.copy()
list_a.append(4)
print(list_a)
print(list_b)
print(list_c)

# Question: Why did list_b change but list_c stayed the same? because both has same reference and list_c is the copy of list_a
