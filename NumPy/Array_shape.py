import numpy as np 

# Drill 1 

drill_1_array=np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print(drill_1_array.shape)


print("\n")


# Drill 2 

drill_2_array=np.array([10,20,30,40,50])
print(drill_2_array.shape)


print("\n")


# Drill 3 

drill_3_array=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(drill_3_array.shape)


print("\n")


# Drill 4 

drill_4_array=np.array([1, 2, 3, 4],ndmin=5)
print(drill_4_array)
print(drill_4_array.shape)


print("\n")


# Drill 5 

drill_5_array=np.array([[1,2],[3,4],[5,6]])
print(drill_5_array.shape)
numbers=drill_5_array.shape
count=numbers*2
print(count)
print(drill_5_array.size)
