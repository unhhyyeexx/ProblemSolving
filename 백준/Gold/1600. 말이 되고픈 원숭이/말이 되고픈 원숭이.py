import sys
input = sys.stdin.readline
from collections import deque

k = int(input())
w, h = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(h)]

monkeyDir = [(1,0), (-1,0), (0,1), (0,-1)]
horseDir = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

visit = [[[False] * (k+1) for _ in range(w)] for _ in range(h)]

q = deque()
q.append((0,0,0,0)) # r, c, 움직인횟수, 말쓴횟수
visit[0][0][0] = True

while q:
    i, j, dist, horse = q.popleft()

    if i == h-1 and j == w-1:
        print(dist)
        exit()

    if horse < k:
        for hi, hj in horseDir:
            ni, nj = i + hi, j + hj
            if 0<=ni<h and 0<=nj<w and board[ni][nj] == 0 and not visit[ni][nj][horse+1]:
                visit[ni][nj][horse+1] = True
                q.append((ni, nj, dist+1, horse+1))
        
    for mi, mj in monkeyDir:
        ni, nj = i + mi, j + mj
        if 0<=ni<h and 0<=nj<w and board[ni][nj] == 0 and not visit[ni][nj][horse]:
            visit[ni][nj][horse] = True
            q.append((ni, nj, dist+1, horse))

print(-1)