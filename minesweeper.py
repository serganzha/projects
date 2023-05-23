def mine_sweeper(grid):
    # Create a new grid to store the counts
    rows = len(grid)
    columns = len(grid[0])
    counts = [[0] * columns for _ in range(rows)]

    # Loop over each position in the grid
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == '#':
                # Mark the mine
                counts[i][j] = '#'
            else:
                # Count the adjacent mines
                mine_count = 0
                for ii in range(max(0, i-1), min(rows, i+2)):
                    for jj in range(max(0, j-1), min(columns, j+2)):
                        if (ii, jj) == (i, j):
                            continue  # skip current cell
                        if grid[ii][jj] == '#':
                            mine_count += 1

                counts[i][j] = str(mine_count)

    # Create a new array with the same dimensions as the input grid
    return [[str(counts[i][j]) if grid[i][j] == '-' else grid[i][j] for j in range(len(row))] for i, row in enumerate(grid)]


# sample grid
grid = [["-", "-", "-", "-", "#"],
        ["-", "#", "-", "#", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "#", "-", "-", "-"]]
result = mine_sweeper(grid)
for row in result:
    print(' '.join(row))
