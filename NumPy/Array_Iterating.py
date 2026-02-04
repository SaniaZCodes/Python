import numpy as np 

# NumPy Iteration: Drill 1 of 5 (The Basics)
print("Drill 1")
d_1_array=np.array([[1, 2, 3], [4, 5, 6]])
for x in d_1_array:
    for y in x:
        print(y)


print("\n")


# NumPy Iteration: Drill 2 of 5 (nditer)
print("Drill 2")
d_2_array=np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(d_2_array):
    print(x)


print("\n")


# NumPy Iteration: Drill 3 of 5 (flags & op_dtypes)
print("Drill 3")

d_3_array=np.array([1, 2, 3])
for x in np.nditer(d_3_array, flags=['buffered'], op_dtypes=['S']):
    print(x)


print("\n")


# NumPy Iteration: Drill 4 of 5 (Step Size)
print("Drill 4")

d_4_array=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
for x in np.nditer(d_4_array[:, ::2]):
    print(x)


print("\n")


# NumPy Iteration: Drill 5 of 5 (ndenumerate)
print("Drill 5")

d_5_array=np.array([[10, 20], [30, 40]])
for index, x in np.ndenumerate(d_5_array):
    print("Index:",index,"Value:",x)
