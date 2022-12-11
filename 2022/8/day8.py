def isVisible(row,col): 
    '''
    print(row,col,rows[row][:col],cols[col][row+1:])
    '''

    val = rows[row][col]
    if val > max(rows[row][:col]):
        return True 
    elif val > max(rows[row][col+1:]):
        return True 
    elif val > max(cols[col][:row]):
        return True 
    elif val > max(cols[col][row+1:]):
        return True

    else:
        print("false\n")
        return False 

rows = [[]]
cols = [[]]
numRows, numCols = 0, 0

with open("input","r") as infile:
    col = 0
    while True: 
        tree = infile.read(1)
        if not tree:
            rows.pop()
            break 
        elif tree=="\n": 
            rows.append([])
            col = 0

            if numCols == 0:
                numCols = len(rows[0])
        else: 
            rows[-1].append(int(tree))

            if numCols == 0:
                cols.append([])
            cols[col].append(int(tree)) 
            col += 1

    numRows = len(rows)

visibleTrees = numRows*2+numCols*2-4
for i in range(1,numRows-1):
    for j in range(1,numCols-1):
        if isVisible(i,j): 
            visibleTrees += 1
print(visibleTrees)


