import array

myarr = array.array('i',[1,3,6,2,7, 5])
uid = [11201,11810]
# take input from user in array
# for i in range(5):
#     myarr.append(int(input("Enter the elements {index} :".format(index=i))))

print(myarr)
myarr.append(10)
myarr.insert(6,15)              # insert at specific index
myarr.pop()
myarr.remove(2)                 # removes the first occurance of the element
myarr.index(5)                  # returns the index of first occurance of the element
myarr.extend(uid)               # append another array or iterable object at the end of the end


print(myarr)
print(myarr.reverse())
print(myarr)

# aliasing in python array
'''
Aliasing means giving another name to the existing object. It doesn't mean copying.
a = ([20, 30, 40, 50])
b = a
'''
arr1 = array.array('i',[3,4,5,7,8])
arr2 = arr1
print(arr1, " :: " ,id(arr1))
print(arr2, " :: " ,id(arr2))