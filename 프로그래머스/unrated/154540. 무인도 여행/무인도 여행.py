from collections import deque

dirs = [[0,1], [0,-1], [1,0], [-1,0]]
def bfs(x, y, visit, maps, n, m):
    q = deque([])
    q.append([x, y])
    visit[x][y] = 1
    food = 0
    while q:
        i, j = q.popleft()
        food += int(maps[i][j])
        for d in dirs:
            ni, nj = i+d[0], j+d[1]
            if 0<=ni<n and 0<=nj<m and visit[ni][nj] == 0 and maps[ni][nj] != 'X':
                q.append([ni, nj])
                visit[ni][nj] = 1
    return food
    
def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    visit = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visit[i][j] == 0:
                answer.append(bfs(i,j,visit,maps,n,m))
                
    if answer: 
        return sorted(answer)
    else:
        return [-1]