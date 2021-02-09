x = 1
y = 1
z = 1
n = 2

grid = [0,0,0]

grid = [[grid[0]+i, grid[1]+j, grid[2]+k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]

n_grid = [grid[key] for key, _ in enumerate(grid) if sum(grid[key]) != n]
print(n_grid)