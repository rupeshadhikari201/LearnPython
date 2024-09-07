# The deque, short for double-ended queue, is a Python data structure that efficiently adds and removes elements from both ends.
# It is a component of the collections module and serves as an alternative to the list for scenarios where frequent insertions and deletions occur at both ends.
from collections import deque

# Create a deque using a tuple of integers
q1 = deque((1,2,3,4,5))
print(q1)

# Create a deque using a list of integers
q2 = deque([1,2,3,4,5])
print(q2)

# Create a deque using a range of integers from 5 to 9
q3 = deque(range(5,10))
print(q3)

# Create a deque using a string, which will be split into individual characters
q4 = deque("abcde")
print(q4)

# Create a deque containing the keys of the dictionary
my_dict = {'name':'Rupesh', 'age': 25}
q5 = deque(my_dict.keys())
print(q5)

# Create a deque containing the values of the dictionary
q6 = deque(my_dict.values())
print(q6)

# Create a deque containing the items (key-value pairs) of the dictionary
q7 = deque(my_dict.items())
print(q7)