'''
Given an array of integers arr, return true if it is possible to split it in two subarrays (without reordering the elements), such that the sum of the two subarrays are equal. If it is not possible then return false.

Input: arr = [1, 2, 3, 4, 5, 5]
Output: true
Input: arr = [4, 3, 2, 1]
Output: false

Expected Time Complexity: O(n)
Expected Space Complexity: O(1)
'''


arr = [1,2,3,4,5,5]

def canSplit2(self, arr):
        #code here
        _sum = 0
        for i in range(len(arr)):
            _sum += arr[i]
        curr_sum = 0
        
        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum == _sum -curr_sum:
                return True
        return False
    
def canSplit1(arr):
    for i in range(len(arr)):
        sub1 = arr[:i]  #O(1)
        sub2 = arr[i:]  #O(1)
        
        # sum : O(i) for the first subarray
        # sum : O(n - i) for the second subarray.
        if sum(sub1) == sum(sub2):
            return True
    return False

ans = canSplit1(arr)
print(ans)