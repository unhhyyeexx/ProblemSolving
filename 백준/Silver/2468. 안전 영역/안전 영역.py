# boj 2468 안전 영역 silver 1

import sys
input = sys.stdin.readline
from collections import deque

dir = [[0,1], [0,-1], [1,0], [-1,0]]
def bfs(i, j):
    q = deque([(i, j)])
    visit[i][j] = 1
    
    while q:
        x, y = q.popleft()
        for di, dj in dir:
            ni, nj = x+di, y+dj
            if 0<=ni<n and 0<=nj<n and board[ni][nj]>h and not visit[ni][nj]:
                q.append((ni, nj)) 
                visit[ni][nj] = 1

    return

n = int(input())
max_v = 0
board = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    max_v = max(max_v, max(tmp))
    board.append(tmp)

answer = 1
for h in range(1, max_v):
    tmp_answer = 0
    visit = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visit[i][j] and board[i][j] > h:
                bfs(i, j)
                tmp_answer += 1
    
    answer = max(answer, tmp_answer)
    
print(answer)