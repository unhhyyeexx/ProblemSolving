def update1(r, c, value, board, merged):
    i, j = merged[r][c]
    board[i][j] = value
    return

def update2(v1, v2, board):
    for i in range(51):
        for j in range(51):
            if board[i][j] == v1:
                board[i][j] = v2
    return
    
def merge(r1, c1, r2, c2, board, merged):
    i1, j1 = merged[r1][c1]
    i2, j2 = merged[r2][c2]
    if board[i1][j1] == "EMPTY":
        board[i1][j1] = board[i2][j2]
    for i in range(51):
        for j in range(51):
            if merged[i][j] == (i2, j2):
                merged[i][j] = (i1, j1)
    return
    
def unmerge(r, c, board, merged):
    x, y = merged[r][c]
    value = board[x][y]
    for i in range(51):
        for j in range(51):
            if merged[i][j] == (x, y):
                merged[i][j] = (i, j)
                board[i][j] = "EMPTY"
    board[r][c] = value
    return


def solution(commands):
    answer = []
    board = [["EMPTY"]*51 for _ in range(51)]
    merged = [[(i,j) for j in range(51)] for i in range(51)]
    for command in commands:
        c = list(command.split())
        op = c[0]
        if op == 'UPDATE':
            if len(c) == 4:
                update1(int(c[1]), int(c[2]), c[3], board, merged)
            elif len(c) == 3:
                update2(c[1], c[2], board)
        elif op == 'MERGE':
            merge(int(c[1]), int(c[2]), int(c[3]), int(c[4]), board, merged)
        elif op == 'UNMERGE':
            unmerge(int(c[1]), int(c[2]), board, merged)
        elif op == 'PRINT':
            i, j = merged[int(c[1])][int(c[2])]
            answer.append(board[i][j])
    return answer