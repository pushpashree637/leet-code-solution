board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]
def isValid(r, c, num):
    for i in range(9):
        if board[r][i] == num or board[i][c] == num:
            return False   
    sr, sc = (r//3)*3, (c//3)*3
    for i in range(3):
        for j in range(3):
            if board[sr+i][sc+j] == num:
                return False
    return True
def solve():
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                for num in "123456789":
                    if isValid(i, j, num):
                        board[i][j] = num
                        if solve():
                            return True
                        board[i][j] = "."
                return False
    return True
solve()
for row in board:
    print(row)
