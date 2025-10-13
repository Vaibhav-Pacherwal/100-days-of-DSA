## N-Queens
def isSafe(board,row,col,n):
    for i in range(0,n):
        if board[row][i] == 'Q':
            return False
        
    for j in range(0,n):
        if board[j][col] == 'Q':
            return False
        
    r1,c1 = row-1,col+1
    while r1 >= 0  and c1 < n:
        if board[r1][c1] == 'Q':
            return False
        r1 -= 1
        c1 += 1
    
    r2,c2 = row-1,col-1
    while r2 >= 0 and c2 >= 0:
        if board[r2][c2] == 'Q':
            return False
        r2 -= 1
        c2 -= 1
    
    return True

def nQueens(board,row,n,ans):
    if row == n:
        ans.append([row[:] for row in board])
        return False
    
    for i in range(0,n):
        if isSafe(board,row,i,n):
            board[row][i] = 'Q'
            nQueens(board,row+1,n,ans)
            board[row][i] = '.'

board = [['.'] * 4 for _ in range(4)]
n,ans = 4,[]
nQueens(board,0,n,ans)
actAns = []
for i in range(len(ans)):
    eachRow = []
    for j in range(len(ans[0])):
        eachRow.append("".join(ans[i][j]))
    actAns.append(eachRow)

print(actAns)
