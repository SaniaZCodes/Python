import numpy as np 

# NumPy Array Slicing: Drill 1 of 5

numbers=[10, 20, 30, 40, 50, 60, 70]
numbers_array=np.array(numbers)
print(numbers_array[1:5])


print("\n")


# NumPy Array Slicing: Drill 2 of 5

print(numbers_array[:4])
print(numbers_array[3:])


print("\n")


# NumPy Array Slicing: Drill 3 of 5

numbers_3=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
numbers_arrays_3=np.array(numbers_3)
print(numbers_arrays_3[::2])
print(numbers_arrays_3[1:8:2])


print("\n")


# NumPy Array Slicing: Drill 4 of 5

arr_2d = np.array([[10, 20, 30, 40, 50], [60, 70, 80, 90, 100]])
print(arr_2d[1, 1:4])
print(arr_2d[0:2, 2])


print("\n")


# NumPy Array Slicing: Drill 5 of 5

big_arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(big_arr[1:4,1:3 ])
