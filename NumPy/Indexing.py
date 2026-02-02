import numpy as np 

# NumPy Array Indexing: Drill 1 of 5

values=[5, 10, 15, 20, 25]
values_array=np.array(values)
print("second element: ",values[1])
print("fourth element: ",values[3])
print("result: ",values[1]+values[3])


print("\n")


# NumPy Array Indexing: Drill 2 of 5

row1=[10, 20, 30]
row2=[40, 50, 60]
array_of_drill_2=np.array([row1,row2])
print(array_of_drill_2[0][1])
print(array_of_drill_2[1][2])
print("Result: ",array_of_drill_2[0][1]*array_of_drill_2[1][2])


print("\n")


# NumPy Array Indexing: Drill 3 of 5

arr_3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr_3[0,1,2])
print(arr_3[1,1,0])


print("\n")


# NumPy Array Indexing: Drill 4 of 5

arr_4 = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
print(arr_4[1,-1])
print(arr_4[0,-2])


print("\n")


# NumPy Array Indexing: Drill 5 of 5

final_arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(final_arr[1,-5])
print(final_arr[0,-1])
print("result: ",final_arr[1,-5]+final_arr[0,-1])
