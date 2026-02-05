import numpy as np 

# NumPy Joining: Drill 1 of 5 (concatenate)
print("Drill 1")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3=np.concatenate((arr1, arr2))
print(arr3)


print("\n")


# NumPy Joining: Drill 2 of 5 (axis=1)
print("Drill 2")
d_2_arr1 = np.array([[1, 2], [3, 4]])
d_2_arr2 = np.array([[5, 6], [7, 8]])
d_2_arr3=np.concatenate((d_2_arr1, d_2_arr2), axis=1)
print(d_2_arr3)


print("\n")


# NumPy Joining: Drill 3 of 5 (stack)
print("Drill 3")
d_3_arr1=np.array([1,2,3])
d_3_arr2=np.array([4,5,6])
d_3_arr3=np.stack((d_3_arr1,d_3_arr2), axis=1)
print(d_3_arr3)


print("\n")


# NumPy Joining: Drill 4 of 5 (hstack & vstack)
print("Drill 4")
d_4_arr1=np.array([1,2,3])
d_4_arr2=np.array([4,5,6])
d_4_arr3=np.vstack((d_4_arr1,d_4_arr2))
d_4_arr4=np.hstack((d_4_arr1,d_4_arr2))
print(d_4_arr3)
print(d_4_arr4)


print("\n")


# NumPy Joining: Drill 5 of 5 (dstack)
print("Drill 5")
array1=np.array([1,2,3])
array2=np.array([4,5,6])
array3=np.dstack((array1, array2))
print(array3)
print(array3.shape)
