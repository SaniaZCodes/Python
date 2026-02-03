import numpy as np 

# NumPy Data Types: Drill 1 of 5

numbers_list=[10, 20, 30, 40]
numbers_array=np.array(numbers_list)
print(numbers_array.dtype)

fruits_list=['apple', 'banana', 'cherry']
fruits_array=np.array(fruits_list)
print(fruits_array.dtype)


print("\n")


# NumPy Data Types: Drill 2 of 5

list_2=[1,2,3,4]
drill_2_array=np.array(list_2, dtype='S')
print(drill_2_array)
print(drill_2_array.dtype)


print("\n")


# NumPy Data Types: Drill 3 of 5

list_3=[1.1, 2.1, 3.1]
array_3_drill=np.array(list_3, dtype='i')
print(array_3_drill)
print(array_3_drill.dtype)


print("\n")


# NumPy Data Types: Drill 4 of 5

drill_4_list=[1, 0, 3]
drill_4_array=np.array(drill_4_list)
print(drill_4_array)
new_array_drill_4=drill_4_array.astype(bool)
print(new_array_drill_4)
print(new_array_drill_4.dtype)


print("\n")


# NumPy Data Types: Drill 5 of 5

drill_5_array=np.array(['1', '2', '3'])
new_array_of_drill_5=drill_5_array.astype('i')
for i in new_array_of_drill_5:
    print(i+10)
