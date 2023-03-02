from collections import deque

def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    visit = [[1]*m for _ in range(n)]
    q = deque([[0,0,1]])
    visit[0][0] = 0
    dir = [[0,1], [0,-1], [1,0], [-1,0]]
    
    while q:
        i, j, cnt = q.popleft()
        if i == n-1 and j == m-1:
            answer = cnt
            break
        for d in dir:
            ni, nj = i+d[0], j+d[1]
            if 0<=ni<n and 0<=nj<m and maps[ni][nj] == 1 and visit[ni][nj] == 1:
                visit[ni][nj] = 0
                q.append([ni,nj,cnt+1])
    return answer