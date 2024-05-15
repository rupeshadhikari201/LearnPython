import numpy as np

print(np.__version__)

# 1-D  ARRAY CREATION METHODS IN NUMPY

# array
arr1 = np.array([1,3,4,6,7], dtype=int)
print("using array function : ", arr1)

# linspace
'''
linspace() Function is used to create an array with evenly spaced numbers between a start pointand stop point.
Syntax:- numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
'''
arr2 = np.linspace(start=1, stop=100, num=5, endpoint=True, dtype=int)
print('arr using linspace : ', arr2)


# logspace
'''
logspace ( ) Function is used to create an array with evenly spaced numbers logarithmically. The sequence starts at base ** start (base to the power of start) and ends with base ** stop.
Syntax:- numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, axis=0)
'''
arr3 = np.logspace(start=1, stop=5, num=5, endpoint=True, base=2, dtype=int)
print("arr using logspace : ", arr3)

# arrange
'''
arange ( ) Function is used to create an array with a group of elements from start to one element prior to stop in steps of stepsize.
Syntax:- numpy.arange(start, stop, stepsize, dtype=None)
'''
arr4 = np.arange(start=1, stop=10, step=2, dtype=int)
print("using arange function : ", arr4)

# zeros
'''
zeros ( ) Function is used to create an array with all zeros. C=Rows, F=Cols
Syntax:- numpy.zeros(shape, dtype=float, order='C/F')
'''
arr5 = np.zeros(shape=(2,5), dtype=int, order='C')
arr6 = np.zeros(shape=(2,5), dtype=int, order='F')
print("using zeros with C: ", arr5)
print("using zeros with F: ", arr6)


# ones
'''
ones() Function is used to create an array with all zeros. C=Rows, F=Cols
Syntax:- numpy.ones(shape, dtype=float, order='C/F')
'''
arr7 = np.ones(shape=(1,5), dtype=int, order='C')
arr8 = np.ones(shape=(1,5), dtype=int, order='F')
print("using zeros with C: ", arr7)
print("using zeros with F: ", arr8)


# any and all of python core
'''
any() Function — This function returns True, if any one element of the iterable is True. If iterable is empty then returns False.
all() Function — This function returns True, if any all element of the iterable is True. If iterable is empty then returns False.
'''
arr9 =  np.array([1,2,4,5])
arr10 = np.array([3,7,4,6])
res1 = arr9 == arr10
print(res1)
print("the element wise comparison of {a} and {b} is {res} ".format(a=arr9, b=arr10, res=res1))
print("the result of any is : ", any(res1))
print("the result of all is : ", all(res1))

# where
'''
where() Function- This function is used to create a new Array which contains, returned element chosen from expressionl or expression2 depending on condition. If condition is True expressionl is executed else expression 2.
Syntax:- numpy.where(condition, expressionl, expression2)
'''
arr11 = np.array([3,5,7,9, 13])
arr12 = np.array([5,1,8,1, 43])
res2 = np.where(arr11>arr12, arr11, arr12)
print("the element wise greater value from arr11 and arr12 is : ", res2)

# nonzero
'''
nonzero() Function- This function is used to determine the positions ofelements which are non zero. This function returns an array that contains the indexes of the element of the array which are not equal to zero
'''
arr13 = np.array([4, 6, 0, 2, 4, 0, 4])
print("the result of nonzero function : ", np.nonzero(arr13))


# view() in python numpy
'''
view() :— This method is used to construct a new view of array with same data of existing array. 
The existing array and new array will share different memory locations.
If the new array get modified, the existing will also be modified as the elements in both the arrays will be like mirror image.
'''
arr14 = np.array([3,4,6,4,2])
arr15 = arr14.view()
print("the memory location of arr14 : ",arr14, id(arr14))
print("the memory location of arr15 : ",arr15, id(arr15))


# copy() in python numpy
'''
copy() — This method is used to create a copy of an existing array. 
If the new array get modified, the existing array will not be affected or vice versa. 
Both the arrays are independent.
Memory Locations are not same.
'''
arr16 = np.array([3,4,6,4,2])
arr17 = arr16.copy()
print("the memory location of arr16 : ",arr16, id(arr16))
print("the memory location of arr17 : ",arr17, id(arr17))

# N-D  ARRAY CREATION METHODS IN NUMPY
'''
    1. array() Function
    2. zeros() Function
    3. ones() Function
    4. reshape() Function
'''

# reshape
'''
This function is used to change the shape of array. We can convert ID array to 2D or 3D array and vice versa. 
The new array should have the same number of elements as in the original array.
Syntax:- reshape(array_name, (n, r, c))
Where,
    array_name : It represents the name of the array whose elements to be converted.
    n : n is the number of arrays in the resultant array
    r : r is the number of rows
    c : c is the number of cols
'''
arr18 = np.array([1,2,3,4,5,6,7,8,9])
arr20 = np.array([1,2,3,4,5,6,7,8])
arr19 = np.array([[5,3,6],[7,5,9]])
print("reshape to 2D array : \n", np.reshape(arr18,(3,3)))            # two rows three columns
print("reshape to 3D array : \n", np.reshape(arr20,(2,2,2)))          # tow array of 4*4
print("reshape to 1D array : ", np.reshape(arr19, (6)))


# flatten
'''
The flatten() method is used to convert 2D or 3D array to ID array.
Syntax:- array name.flatten()
'''
arr21 = np.ones((3,3), dtype=int)
print("to 2D array of 1D array using flatten : ", arr19.flatten())
print("3D array before flatterning : \n", arr21)
print("to 3D array of 1D array using flatten : ", arr21.flatten())


# slicing in 2D Array
arr22 = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90],
])
# res = arr[row,col]
print("first row all column :  ", arr22[1, :])          # first row all column
print("all row zeroth column : ", arr22[:, 0])          # first row all column
print("first 2*2 matrix : \n", arr22[0:2,0:2])            # first 2*2 matrix


# Attributes of Numpy Array
'''
    1. ndim
    2. shape
    3. size
    4. itemsize
    5. dtype
    6. nbytes
'''
print(arr22.nbytes)
print(arr22.itemsize)