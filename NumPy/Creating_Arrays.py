import numpy as np 

# NumPy Creating Arrays: Drill 1 of 5

list=[10,20,30,40,50]
arr=np.array(list)
print(arr)
print(type(arr))


print("\n")


# NumPy Creating Arrays: Drill 2 of 5

row1=[1,2,3]
row2=[4,5,6]
two_d_array=np.array([row1,row2])
print(two_d_array)
print("Number of dimensions: ",two_d_array.ndim)


print("\n")


# NumPy Creating Arrays: Drill 3 of 5

list3=[1,2,3,4]
arr3=np.array(list3, ndmin=5)
print(arr3)
print("Number of dimensions: ",arr3.ndim)


print("\n")


# NumPy Creating Arrays: Drill 4 of 5

first=[[1, 2], [3, 4]]
second=[[5, 6], [7, 8]]
three_d_array=np.array([first,second])
print(three_d_array)
dimension=three_d_array.ndim
if dimension==3:
    print("Yes it is 3D array")
else:
    print("Not")


print("\n")


# NumPy Creating Arrays: Drill 5 of 5

t=(100,200,300)
ta=np.array(t)
print("Tuple array: ",ta)
zero=np.array(42)
print("Dimension of 0 array: ",zero.ndim)
