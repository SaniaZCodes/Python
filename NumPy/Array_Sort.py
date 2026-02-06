import numpy as np 

# NumPy Sorting: Drill 1 of 5 (Basic Sort)
print("Drill 1")
d_1_array=np.array([3, 2, 0, 1])
new_d_1_array=np.sort(d_1_array)
print("Original Array: ",d_1_array)
print("New Array: ",new_d_1_array)


print("\n")


# NumPy Sorting: Drill 2 of 5 (Alphabetical Sort)
print("Drill 2")
drill_2_array=np.array(['banana', 'cherry', 'apple'])
new_drill_2_array=np.sort(drill_2_array)
print(new_drill_2_array)


print("\n")


# NumPy Sorting: Drill 3 of 5 (Boolean Sort)
print("Drill 3")
drill_3_array=np.array([True, False, True, False, True])
new_drill_3_array=np.sort(drill_3_array)
print(new_drill_3_array)


print("\n")


# NumPy Sorting: Drill 4 of 5 (Sorting 2D Arrays)
print("Drill 4")
drill_4_array=np.array([[3, 2, 4], [5, 0, 1]])
new_drill_4_array=np.sort(drill_4_array)
print(new_drill_4_array)


print("\n")


# NumPy Sorting: Drill 5 of 5 (Descending Sort)
print("Drill 5")
drill_5_array=np.array([10, 50, 30, 20, 40])
new_drill_5_array=np.sort(drill_5_array)
print(new_drill_5_array)
print(new_drill_5_array[::-1])
