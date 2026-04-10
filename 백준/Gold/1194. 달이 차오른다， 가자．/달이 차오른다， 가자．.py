import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]

visited = [[[False]*64 for _ in range(m)] for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j]=='0':
            q.append((i,j,0,0))  # r,c,key,dist
            visited[i][j][0] = True

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

while q:
    r,c,key,dist = q.popleft()

    if board[r][c]=='1':
        print(dist)
        exit()

    for dr,dc in dirs:
        nr = r+dr
        nc = c+dc

        if not (0<=nr<n and 0<=nc<m):
            continue

        tile = board[nr][nc]

        if tile=='#':
            continue

        new_key = key

        if 'a' <= tile <= 'f':
            new_key |= (1<<(ord(tile)-ord('a')))

        if 'A' <= tile <= 'F':
            if not (key & (1<<(ord(tile)-ord('A')))):
                continue

        if not visited[nr][nc][new_key]:
            visited[nr][nc][new_key] = True
            q.append((nr,nc,new_key,dist+1))

print(-1)