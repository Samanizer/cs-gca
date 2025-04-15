def process_queries(queries, k):
    nums = set()
    result = []
    pair_count = 0
    
    for q in queries:
        op, x = q
        
        if op == '+':
            if x + k in nums:
                pair_count += 1
            if x - k in nums:
                pair_count += 1
            nums.add(x)
        
        else:
            if x + k in nums:
                pair_count -= 1
            if x - k in nums:
                pair_count -= 1
            nums.remove(x)
            
        result.append(pair_count)
        
    return result

queries = [['+', 1], ['+', 3], ['+', 5], ['-', 3]]
k = 2
print(process_queries(queries, k))  
# Output: [0, 1, 2, 0]
