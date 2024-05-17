from collections import deque

def solution(rectangle, cx, cy, itemX, itemY):
    answer = 0
    maps = [[-1]*102 for _ in range(102)]
    
    for rec in rectangle:
        lx, ly, rx, ry = map(lambda x:x*2, rec)
        for i in range(lx, rx+1):
            for j in range(ly, ry+1):
                if lx<i<rx and ly<j<ry:
                    maps[i][j] = 0
                elif maps[i][j] == -1:
                    maps[i][j] = 1
                    
    q = deque([[cx*2, cy*2]])
    visit = [[0]*102 for _ in range(102)]
    visit[cx*2][cy*2] = 1
    dir = [[0,1], [0,-1], [1,0], [-1,0]]
    while q:
        x, y = q.popleft()
        if x == itemX*2 and y == itemY*2:
            answer = visit[x][y]//2
            break
            
        for di, dj in dir:
            ni, nj = x+di, y+dj
            if visit[ni][nj] == 0 and maps[ni][nj] == 1:
                q.append([ni,nj])
                visit[ni][nj] = visit[x][y] + 1
    
    return answer