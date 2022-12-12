# 16234 인구이동
# gold 5
# 구현 그래프이론 그래프탐색 너비우선탐색 시뮬레이션

import sys
input = sys.stdin.readline

from collections import deque

dir = [[0,1], [0,-1], [1,0], [-1,0]]

def bfs (x,y, visit, people, n, l, r):
    q = deque()
    q.append([x, y])
    union = []
    union.append([x,y])

    while q:
        i, j = q.popleft()
        for d in dir:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < n and 0 <= nj < n and visit[ni][nj] == 0:
                if l <= abs(people[ni][nj] - people[i][j]) <= r:
                    visit[ni][nj] = 1
                    q.append([ni, nj])
                    union.append([ni, nj])
    return union

def solution(people, n, l, r):
    answer = 0
    while True:
        visit = [[0]*n for _ in range(n)]
        isUnion = False
        for i in range(n):
            for j in range(n):
                if visit[i][j] == 0:
                    visit[i][j] = 1
                    union = bfs(i, j, visit, people, n, l, r)
                    if len(union) > 1:
                        isUnion = True
                        avg = sum(people[ni][nj] for ni, nj in union) // len(union)
                        for ni, nj in union:
                            people[ni][nj] = avg
        if not isUnion:
            break
        answer += 1

    return answer

n, l, r = map(int, input().split())
people = []
for _ in range(n):
    people.append(list(map(int, input().split())))
print(solution(people, n, l, r))