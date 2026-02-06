import numpy as np  

# NumPy Filtering: Drill 1 of 5 (Manual Boolean Indexing)
d_1_array=np.array([10, 20, 30, 40])
a1=[True, False, True, False]
new_array_1=d_1_array[a1]
print(new_array_1)


print("\n")


# NumPy Filtering: Drill 2 of 5 (The "Condition" Method)
drill_2_array=np.array([41, 42, 43, 44])
filter_arr = (drill_2_array > 42)
new_array_2=drill_2_array[filter_arr]
print(new_array_2)


print("\n")


# NumPy Filtering: Drill 3 of 5 (The Remainder Method)
drill_3_array=np.array( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
filter_array_3=drill_3_array %2==0
new_array_3=drill_3_array[filter_array_3]
print(new_array_3)


print("\n")


# NumPy Filtering: Drill 4 of 5 (String Length Filtering)
drill_4_array=np.array(['Python', 'C', 'Java', 'PHP', 'JavaScript'])
filter_list=[]
for x in drill_4_array:
    if len(x)>4:
        filter_list.append(True)
    else:
        filter_list.append(False)
new_array_4=drill_4_array[filter_list]
print(new_array_4)


print("\n")


# NumPy Filtering: Drill 5 of 5 (Direct Filtering)
drill_5_array=np.array([5, 10, 15, 20, 25, 30])
new_arr_5 = drill_5_array[(drill_5_array > 10) & (drill_5_array < 25)]
print(new_arr_5)
