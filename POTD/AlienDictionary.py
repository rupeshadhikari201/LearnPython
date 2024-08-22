from typing import List

n = 5 
k = 4 
mydict= {"baa","abcd","abca","cab","cad"}
print(type(mydict))
def findOrder(mydict : List[str], n : int, k : int) -> str:
    valid_order = ''
    