import numpy as np 

# NumPy Copy vs View: Drill 1 of 5

drill_1_array=np.array([1, 2, 3, 4, 5])
copy_of_drill_1_array=drill_1_array.copy()
copy_of_drill_1_array[0]=100
print("Original Array: ",drill_1_array)
print("Copy Array: ",copy_of_drill_1_array)


print("\n")

# NumPy Copy vs View: Drill 2 of 5

drill_2_array=np.array([10,20,30,40,50])
view_of_drill_2_array=drill_2_array.view()
view_of_drill_2_array[0]=99
print("Original Array: ",drill_2_array)
print("Copy Array: ",view_of_drill_2_array)


print("\n")


# NumPy Copy vs View: Drill 3 of 5

drill_3_array=np.array([5,10,15])
arr_copy=drill_3_array.copy()
arr_view=drill_3_array.view()
print(arr_copy.base)
print(arr_view.base)


print("\n")


# NumPy Copy vs View: Drill 4 of 5

drill_4_array=np.array([1,2,3,4,5])
my_slice = drill_4_array[0:2]
my_slice[0] = 999
print(drill_4_array)
print(my_slice.base)


print("\n")


# NumPy Copy vs View: Drill 5 of 5

drill_5_array=np.array([100,200,300,400])
print("Original Array: ",drill_5_array)
new=drill_5_array[2:4].copy()
print(new)
new[0]=0
print(new)
print(new.base)
