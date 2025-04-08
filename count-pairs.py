from collections import defaultdict

words = ["abca", "cba", "aaabb", "baba", "xyz", "zyx"]

def count_pairs(arr):
    freq = defaultdict(int)
    for word in arr:
        freq[frozenset(word)] += 1
    
    total = 0
    for count in freq.values():
        total += count * (count - 1) // 2
    
    return total