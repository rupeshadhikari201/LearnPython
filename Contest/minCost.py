from typing import List


n =  4
a = [1,2,2,2]
b = [1,2,4,4]

def minCost(n : int, a : List[int], b : List[int]) -> int:
        # code here
        cnt = 0
        d = dict()
        for i in range(n):
            if a[i] != b[i]:
                ele = tuple(sorted((a[i],b[i])))
                if ele in d:
                    d[ele] +=1
                else:
                    d[ele] = 1
        for i in d:
            if d[i] %2 == 0:
                cnt+=2
        return cnt if cnt>0 else  -1
            
d = minCost(n,a,b)
print(d)
