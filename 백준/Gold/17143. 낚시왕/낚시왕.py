# boj 17143 낚시왕 gold 1
# 1,2,3,4 위 아래 오른쪽 왼쪽

import sys
input = sys.stdin.readline

dir = [[-1,0], [1,0], [0,1], [0,-1]]
def solution(c):
    global board
    fish = 0
    # 상어 잡기
    for j in range(row):
        if board[j][c]:
            fish += board[j][c][2]
            board[j][c] = []
            break
    
    nboard = [[0]*col for _ in range(row)]
    # 상어 이동
    for i in range(row):
        for j in range(col):
            if board[i][j] :
                s, d, z = board[i][j]
                x, y = i, j
                if d < 2:
                    ns = s % rcycle
                else:
                    ns = s % ccycle
                
                while ns:
                    ni, nj = x+dir[d][0], y+dir[d][1]
                    if 0<=ni<row and 0<=nj<col: # 이동할 칸이 있어서 방향전환 x
                        x, y = ni, nj
                        ns -= 1
                    else: # 벽이라 방향전환
                        if d in [0,2]:
                            d += 1
                        else:
                            d -= 1
                
                if (nboard[x][y] and nboard[x][y][2] < z) or not nboard[x][y]:
                    nboard[x][y] = [s,d,z]
    
    board = nboard

    return fish

row, col, m = map(int, input().split())
rcycle, ccycle = (row-1)*2, (col-1)*2
board = [[0 for _ in range(col)] for _ in range(row)]

for _ in range(m):
    r, c, s, d, z = map(int, input().split())
    board[r-1][c-1] = [s,d-1,z]

answer = 0
for c in range(col):
    answer += solution(c)
print(answer)