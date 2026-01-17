# Drill 1: The "Simple Sequence" (Basics)
# Goal: Understand the default behavior of range.

x= range(0,5)
print("Range Object: ",x)
print("Printing Each number in range using for loop: ")
for i in x:
    print(i)


print("\n")


# Drill 2: The "Custom Jump" (Start & Step)
# Goal: Use all three parameters to control the sequence.

drill_2_range= range(10,50,5)
print(list(drill_2_range))
another_range= range(10,0,-1)
print(list(another_range))


print("\n")


# Drill 3: The "Index Master" (Range with Len)
# Goal: Use range to iterate through the indexes of a list.

fruits = ["Apple", "Banana", "Cherry", "Date"]
for x in range(len(fruits)):
    print("Index: ",x,": ",fruits[x])
