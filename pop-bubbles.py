def pop_bubbles(grid, i, j):
    
    if grid[i][j] == 0:
        return 0
    
    n, m = len(grid), len(grid[0])
    
    def dfs(x, y):
        if x < 0 or y < 0 or x>= n or y >= m or grid[x][y] == 0:
            return 0
        
        grid[x][y] = 0
        count = 1
        
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            count += dfs(x+dx, y+dy)

        return count
    
    return dfs(i,j)

grid = [
  [1, 1, 0],
  [1, 0, 0],
  [0, 1, 1]
]

print(pop_bubbles(grid, 0, 0))  # Output: 3
print(pop_bubbles(grid, 2, 2))  # Output: 2
