data = open("Day_4.txt").readlines()
H, W = len(data), len(data[0]) - 1
grid = {(y, x): data[y][x] for y in range(H) for x in range(W)}
T, D = "XMAS", [(dy, dx) for dy in [-1, 0, 1] for dx in [-1, 0, 1] if dy or dx]

print("Part 1:", sum("".join(grid.get((y + dy * i, x + dx * i), "") for i in range(len(T))) == T for y, x in grid for dy, dx in D))
print("Part 2:", sum({grid.get((y - 1, x - 1), "") + grid.get((y + 1, x + 1), ""), grid.get((y - 1, x + 1), "") + grid.get((y + 1, x - 1), "")} <= {"MS", "SM"} for y, x in grid if grid[y, x] == "A"))
