import numpy as np 

# NumPy Searching: Drill 1 of 5 (where)
print("Drill 1")
drill_1_array=np.array([1, 2, 3, 4, 5, 4, 4])
new_drill_1_array=np.where(drill_1_array==4)
print(new_drill_1_array)


print("\n")


# NumPy Searching: Drill 2 of 5 (Searching with Logic)
print("Drill 2")
drill_2_array=np.array([1,2,3,4,5,6,7,8,9,10])
new_drill_2_array=np.where(drill_2_array%2==0)
print(new_drill_2_array)


print("\n")


# NumPy Searching: Drill 3 of 5 (searchsorted)
print("Drill 3")
drill_3_array=np.array([6,7,8,9])
new_drill_3_array=np.searchsorted(drill_3_array,8.5)
print(new_drill_3_array)


print("\n")


# NumPy Searching: Drill 4 of 5 (side='right')
print("Drill 4")
drill_4_array=np.array([1, 2, 2, 2, 3])
new_drill_4_array=np.searchsorted(drill_4_array,2,side='left')
new_new_drill_4_array=np.searchsorted(drill_4_array,2,side='right')
print(new_drill_4_array)
print(new_new_drill_4_array)


print("\n")


# NumPy Searching: Drill 5 of 5 (Multiple Values)
print("Drill 5")
drill_5_array=np.array([1, 3, 5, 7])
new_drill_5_array=np.searchsorted(drill_5_array,[2,4,6])
print(new_drill_5_array)
