# boj 16236 아기상어 gold 3

import sys
input = sys.stdin.readline
from collections import deque

# 1개밖에 없으면 그거
# 그 이상이면 가까운거
# 가까운게 많으면 가장 위 왼쪽에 잇는거

dir = [[-1,0], [0,1], [1,0], [0,-1]]
def bfs(x, y):
    visit = [[0]*n for _ in range(n)]
    q = deque([[x,y]])
    able = []
    baby = board[x][y]

    visit[x][y] = 1

    while q:
        i, j = q.popleft()
        for di, dj in dir:
            ni, nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<n and visit[ni][nj] == 0:
                if baby > board[ni][nj] and board[ni][nj] != 0:
                    visit[ni][nj] = visit[i][j] + 1
                    able.append((visit[ni][nj] - 1, ni, nj))
                elif baby == board[ni][nj] or board[ni][nj] == 0:
                    visit[ni][nj] = visit[i][j] + 1
                    q.append([ni, nj])
                

    return sorted(able, key=lambda x:(x[0], x[1], x[2]))


n = int(input())
board = []
bi, bj = 0, 0
for i in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    for j in range(n):
        if tmp[j] == 9:
            bi, bj = i, j

cnt = 0
size = [2, 0]
while True:
    board[bi][bj] = size[0]
    able = deque(bfs(bi, bj))

    if not able:
        break

    step, ni, nj = able.popleft()
    cnt += step
    size[1] += 1

    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    board[bi][bj] = 0
    bi, bj = ni, nj

print(cnt)