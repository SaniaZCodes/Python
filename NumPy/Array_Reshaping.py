import numpy as np 

# 🧠 NumPy Array Reshaping: Drill 1 of 5

d_1_array=np.array([1,2,3,4,5,6,7,8,9,10])
new_d_1_array=d_1_array.reshape(5,2)
print(new_d_1_array)


print("\n")


# NumPy Array Reshaping: Drill 2 of 5

d_2_array=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_d_2_array=d_2_array.reshape(2,3,2)
print(new_d_2_array)


print("\n")


# NumPy Array Reshaping: Drill 3 of 5

d_3_array=np.array([1, 2, 3, 4, 5, 6, 7, 8])
new_d_3_array=d_3_array.reshape(2,-1)
print(new_d_3_array)


print("\n")


# NumPy Array Reshaping: Drill 4 of 5

d_4_array=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_d_4_array=d_4_array.reshape(2,2,-1)
print(new_d_4_array)
print(new_d_4_array.shape)


print("\n")


# NumPy Array Reshaping: Drill 5 of 5

flat_array=new_d_4_array.reshape(-1)
print(flat_array)
print(flat_array.ndim)
