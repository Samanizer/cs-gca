def even_odd_sub(arr):
    if len(arr) == 0:
        return 0
    
    max_len = 1
    curr_len = 1

    for i in range(1, len(arr)):
        if arr[i] % 2 != arr[i-1] % 2:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1
    
    return max_len

print(even_odd_sub([4, 3, 2, 5, 6, 7, 8]))  # ✅ 7
print(even_odd_sub([1, 2, 3, 4, 5]))        # ✅ 5
print(even_odd_sub([2, 4, 6, 8]))           # ✅ 1 (all even, no alternation)
print(even_odd_sub([1]))                   # ✅ 1
print(even_odd_sub([]))                    # ✅ 0
