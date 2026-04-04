import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split(" "))
board = [list(input().rstrip()) for _ in range(n)]

visit = [[[False]*(k+1) for _ in range(m)] for _ in range(n)]
q = deque()
visit[0][0][0] = True
q.append((0,0,0,0)) # r, c, 경로길이, 벽몇개 부쉈는지

dirs = [(0,1), (0,-1), (1,0), (-1,0)]
while q:
    i, j, dist, wall = q.popleft()

    if i == n-1 and j == m-1:
        print(dist + 1)
        exit()
    
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if 0<=ni<n and 0<=nj<m:
            # 벽 있어서 부숴볼게
            if wall < k and board[ni][nj] == '1' and visit[ni][nj][wall+1] == False:
                visit[ni][nj][wall+1] = True
                q.append((ni, nj, dist+1, wall + 1))
            # 벽 없네
            if board[ni][nj] == '0' and visit[ni][nj][wall] == False:
                visit[ni][nj][wall] = True
                q.append((ni, nj, dist+1, wall))
    

print(-1)
