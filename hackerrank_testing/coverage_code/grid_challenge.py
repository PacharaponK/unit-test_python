def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
    
    for j in range(len(grid[0])):
        for k in range(len(grid) - 1):
            if grid[k][j] > grid[k + 1][j]:
                return "NO"
    
    return "YES"
