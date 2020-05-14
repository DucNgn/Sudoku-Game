def solve(board):
    print('Solving')
    (subMatrixDigit, RowDigit, ColDigit) = setUpBitwises(board)

    initPos = (0, 0)
    if(backtracking(board, initPos, subMatrixDigit, RowDigit, ColDigit) is True):
        print('Solved')
        printBoard(board, 9, 9)
    else:
        print('Unsolvable')

def setUpBitwises(board):
    subMatrixDigit = [[0 for x in range(3)] for y in range(3)] 
    RowDigit = [0 for x in range(9)]
    ColDigit = [0 for x in range(9)]

    for y in range(9):
        for x in range(9):
            if(board[y][x] > 0):
                value = board[y][x]
                digitValue = 1 << (value - 1) # Move the position of bit 1 (value -1) left
                subMatrixDigit[int(y / 3)][int(x / 3)] |= digitValue
                RowDigit[y] |= digitValue
                ColDigit[x] |= digitValue

    return (subMatrixDigit, RowDigit, ColDigit)

# For Debugging
def printBitDigits(subMatrixDigit, ColDigit, RowDigit):
    print(subMatrixDigit)
    print(RowDigit)
    print(ColDigit)

# X: Num of col Y: Num of row. Loop row down row
def backtracking(board, pos, subMatrixDigit, RowDigit, ColDigit):
    (x, y) = pos
    if(y == 9):
        return True 

    if(x == 9) :
        return backtracking(board, (0, y+1), subMatrixDigit, RowDigit, ColDigit)    

    if(board[y][x] == 0):
        for i in range(1, 10):
            digit = 1 << (i - 1)
            if(not existed(digit, pos, subMatrixDigit, RowDigit, ColDigit)):
                subMatrixDigit[int(y/3)][int(x/3)] |= digit
                RowDigit[y] |= digit
                ColDigit[x] |= digit
                board[y][x] = i

                if(backtracking(board, (x+1, y), subMatrixDigit, RowDigit, ColDigit)):
                    return True
                else:
                    # back track
                    subMatrixDigit[int(y/3)][int(x/3)] &= ~digit
                    RowDigit[y] &= ~digit
                    ColDigit[x] &= ~digit
                    board[y][x] = 0
        
        return False

    return backtracking(board, (x+1, y), subMatrixDigit, RowDigit, ColDigit)

def existed(digit, pos, subMatrixDigit, RowDigit, ColDigit):
    (x, y) = pos
    return (subMatrixDigit[int(y/3)][int(x/3)] & digit) or (RowDigit[y] & digit) or (ColDigit[x] & digit)

def printBoard(board, rowsNum, colsNum):
    for i in range(rowsNum):
        for j in range(colsNum):
            print(board[i][j], end = " ")
        print("\n")

def main():
    board = [
            [3, 0, 6, 5, 0, 8, 4, 0, 0],   
            [5, 2, 0, 0, 0, 0, 0, 0, 0],   
            [0, 8, 7, 0, 0, 0, 0, 3, 1],   
            [0, 0, 3, 0, 1, 0, 0, 8, 0],   
            [9, 0, 0, 8, 6, 3, 0, 0, 5],   
            [0, 5, 0, 0, 9, 0, 6, 0, 0],   
            [1, 3, 0, 0, 0, 0, 2, 5, 0],   
            [0, 0, 0, 0, 0, 0, 0, 7, 4],   
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    solve(board)

main()
