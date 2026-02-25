from collections import deque

def bfs(start, end, maps, n, m):
    visit = [[0] * m for _ in range(n)]
    q = deque()
    q.append(start)
    dirs = [[0,1], [0,-1], [1,0], [-1,0]]
    while len(q) > 0:
        ci, cj = q.popleft()
        cv = visit[ci][cj]
        for di, dj in dirs:
            ni, nj = ci+di, cj+dj
            if (0<=ni<n and 0<=nj<m):
                if (maps[ni][nj] == "X"): continue
                if (ni==end[0] and nj==end[1]):
                    return cv+1
                else:
                    if visit[ni][nj] == 0:
                        visit[ni][nj] = cv + 1
                        q.append([ni, nj])
            
def solution(maps):
    n, m = len(maps), len(maps[0])
    start, end, lever = [], [], []
    
    # find start point
    for i in range(n):
        if (start and end and lever): break
        for j in range(m):
            if maps[i][j] == 'S':
                start = [i, j]
            elif maps[i][j] == 'E':
                end = [i, j]
            elif maps[i][j] == 'L':
                lever = [i, j]
                
    stol = bfs(start, lever, maps, n, m)
    ltoe = bfs(lever, end, maps, n, m)
    
    if not stol or not ltoe:
        return -1
    else:
        return stol + ltoe
