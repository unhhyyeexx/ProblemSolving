import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split(" "))
board = [list(input().strip()) for _ in range(n)]

visit = [[float('inf')]*m for _ in range(n)]

q = deque()
visit[0][0] = 0
q.append((0,0))

dirs = [[0,1], [0,-1], [1,0], [-1,0]]
while len(q) > 0:
    i, j = q.popleft()
    for di, dj in dirs:
        ni = i + di
        nj = j + dj
        if 0<=ni<n and 0<=nj<m:

            cost = visit[i][j] + int(board[ni][nj])

            if cost < visit[ni][nj]:
                visit[ni][nj] = cost

                if board[ni][nj] == '0':
                    q.appendleft((ni, nj))
                else:
                    q.append((ni, nj))

print(visit[n-1][m-1])