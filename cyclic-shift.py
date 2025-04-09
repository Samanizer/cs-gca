'''
Given an array of integers, determine the smallest 
number of cyclic left shifts required to make the 
array sorted in non-decreasing order. 
If it’s not possible, return -1.
'''

def min_cyclic_shift(arr):
    n = len(arr)
    target = sorted(arr)
    
    for i in range(n):
        rotated = arr[i:] + arr[:i]
        if rotated == target:
            return i
    
    return -1