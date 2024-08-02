import copy
def bang(m, n, board):
    dir = [[0,1], [1,0], [1,1]]
    newboard = copy.deepcopy(board)
    bangs = 0
    for i in range(m-1):
        for j in range(n-1):
            now = board[i][j]
            if not now:
                continue
            flag = 0
            for di, dj in dir:
                ni, nj = i+di, j+dj
                if 0<=ni<m and 0<=nj<n and board[ni][nj] == now:
                    flag +=1
            if flag == 3:
                bangs += 1
                newboard[i][j], newboard[i+1][j], newboard[i][j+1], newboard[i+1][j+1] = 0,0,0,0
    if not bangs:
        return newboard, False
    return newboard, True

def slide(m, n, board):
    for i in range(n):
        down = 0
        for j in range(m-1, -1, -1):
            if board[j][i] == 0:
                down += 1
            else:
                if not down:
                    continue
                else:
                    board[j+down][i] = board[j][i]
                    board[j][i] = 0
    return board

def solution(m, n, board):
    answer = 0
    board = [list(a) for a in board]
    while True:
        maps, flag = bang(m, n, board)
        if not flag:
            break
        board = slide(m, n, maps)
    for i in range(m):
        answer += board[i].count(0)
    return answer