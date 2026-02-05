import numpy as np 

# NumPy Splitting: Drill 1 of 5 (The Basics)
print("Drill 1")
d_1_arr1=np.array([1,2,3,4,5,6])
new_d_1_array=np.array_split(d_1_arr1,3)
print(new_d_1_array)


print("\n")


# NumPy Splitting: Drill 2 of 5 (Uneven Splits)
print("Drill 2")
d_2_array=np.array([1,2,3,4,5])
new_d_2_array=np.array_split(d_2_array,3)
print(new_d_2_array)
print(new_d_2_array[0])


print("\n")


# NumPy Splitting: Drill 3 of 5 (Splitting 2D Arrays)
print("Drill 3")
d_3_array=np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15],
                    [16,17,18]])

new_d_3_array=np.array_split(d_3_array,3,axis=1)
print(new_d_3_array)
print(new_d_3_array[0].shape)


print("\n")


# NumPy Splitting: Drill 4 of 5 (The Horizontal Shortcut)
print("Drill 4")
d_4_array=np.array([[1,2,3,4,5,6],
                    [7,8,9,10,11,12],
                    [13,14,15,16,17,18]])
new_d_4_array=np.hsplit(d_4_array,3)
print(new_d_4_array)


print("\n")


# NumPy Splitting: Drill 5 of 5 (vsplit)
print("Drill 5")
d_5_array=np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
new_d_5_array=np.vsplit(d_5_array,2)
print(new_d_5_array)
print(new_d_5_array[1].shape)
