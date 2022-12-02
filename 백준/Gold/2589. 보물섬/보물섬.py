# 2589 보물섬
# gold 5
# 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색


import sys
from collections import deque
input = sys.stdin.readline


def bfs(h, w, maps, i, j):
    dir = [[0,1], [0,-1], [1,0], [-1,0]]
    count = 1
    q = deque([])
    q.append([i, j])
    visit = [[0]*w for _ in range(h)]
    visit[i][j] = 1

    while q:
        now = q.popleft()
        x, y = now[0], now[1]
        if count < visit[x][y]:
            count = visit[x][y]
        for d in dir:
            ni, nj = x+d[0], y+d[1]
            if 0<=ni<h and 0<=nj<w and maps[ni][nj] != -1:
                if visit[ni][nj] > visit[x][y] + 1:
                    visit[ni][nj] = visit[x][y] + 1
                    q.append((ni, nj))
                elif visit[ni][nj] == 0:
                    visit[ni][nj] = visit[x][y] + 1
                    q.append((ni, nj))
    return count -1

def solution(h, w, maps):
    answer = 0

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 0:
                check = bfs(h, w, maps, i, j)
                if check > answer:
                    answer = check
    return answer

h, w = map(int, input().split())
maps = []
for i in range(h):
    tmp = []
    for j in input():
        if j == "W":
            tmp.append(-1)
        else:
            tmp.append(0)
    maps.append(tmp)

print(solution(h, w, maps))