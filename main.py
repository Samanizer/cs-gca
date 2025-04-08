def even_odd_sub(arr):
    if len(arr) == 0:
        return 0
    
    max_len = 1
    curr_len = 1

    for i in range(1, len(arr)):
        if arr[i] % 2 !=