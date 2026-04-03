n = 4
result = []
board = [["." for _ in range(n)] for _ in range(n)]
def isSafe(row, col):
    for i in range(row):
        if board[i][col] == "Q":
            return False   
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1    
    i, j = row-1, col+1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1    
    return True
def solve(row):
    if row == n:
        temp = []
        for r in board:
            temp.append("".join(r))
        result.append(temp)
        return    
    for col in range(n):
        if isSafe(row, col):
            board[row][col] = "Q"
            solve(row+1)
            board[row][col] = "."
solve(0)
print(result)
