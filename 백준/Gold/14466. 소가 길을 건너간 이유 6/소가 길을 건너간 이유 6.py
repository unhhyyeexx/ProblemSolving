# boj 14466 소가 길을 건너간 이유 6 gold 3

import sys
input = sys.stdin.readline
from collections import deque

dir = [[0,1], [0,-1], [1,0], [-1,0]]
def bfs(r, c):
    q = deque()
    q.append((r, c))
    visit[r][c] = 1

    while q:
        i, j = q.popleft()
        for di, dj in dir:
            ni, nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<n and not visit[ni][nj] and (ni, nj) not in board[i][j]:
                q.append((ni, nj))
                visit[ni][nj] = 1



n, k, t = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
answer = 0

for _ in range(t):
    r1, c1, r2, c2 = map(int, input().split())
    board[r1-1][c1-1].append((r2-1, c2-1))
    board[r2-1][c2-1].append((r1-1, c1-1))

cow = []
for _ in range(k):
    x, y = map(int, input().split())
    cow.append((x-1, y-1))

for i, c in enumerate(cow):
    visit = [[0]*n for _ in range(n)]
    bfs(c[0], c[1])
    for r2, c2 in cow[i+1:]:
        if not visit[r2][c2]:
            answer += 1

print(answer)