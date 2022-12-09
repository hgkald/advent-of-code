def isVisible(row,col): 
    print("  ",grid[row-1][col])
    print(grid[row][col-1]," ",grid[row][col]," ",grid[row][col+1])
    print("  ",grid[row+1][col],"\n")

    if grid[row][col] > grid[row-1][col]:
        return True 
    elif grid[row][col] > grid[row+1][col]:
        return True 
    elif grid[row][col] > grid[row][col-1]:
        return True 
    elif grid[row][col] > grid[row][col+1]:
        return True
    else:
        print("false\n")
        return False 

grid = [[]]
numRows, numCols = 0, 0

with open("input","r") as infile: 
    while True: 
        tree = infile.read(1)
        if not tree:
            grid.pop()
            break 
        elif tree=="\n": 
            grid.append([])
        else: 
            grid[-1].append(tree)

    numRows = len(grid)
    numCols = len(grid[0])

visibleTrees = numRows*2+numCols*2-4
for i in range(1,numRows-1):
    for j in range(1,numCols-1):
        if isVisible(i,j): 
            visibleTrees += 1

print(visibleTrees)


