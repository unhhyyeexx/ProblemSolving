from collections import deque

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    
    s, l = [], []
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S': s = [i, j]
            elif maps[i][j] == 'L': l = [i, j]
    
    dir = [[0,1], [0,-1], [1,0], [-1,0]]
    # 시작부터 레버까지
    visit = [[0]*m for _ in range(n)]
    q = deque()
    q.append(s)
    visit[s[0]][s[1]] = 1
    while q:
        i, j = q.popleft()
        lcheck = 0
        for d in dir:
            ni, nj = i+d[0], j+d[1]
            if 0<=ni<n and 0<=nj<m:
                if maps[ni][nj] == 'L':
                    answer += visit[i][j]
                    lcheck = 1
                    break
                if maps[ni][nj] in ['O', 'E'] and visit[ni][nj] == 0:
                    visit[ni][nj] = visit[i][j] + 1
                    q.append([ni, nj])
        if lcheck: 
            break
    if answer == 0:
        return -1
    
    # 레버부터 출구까지
    q = deque()
    q.append(l)
    visit = [[0]*m for _ in range(n)]
    visit[l[0]][l[1]] = 1
    while q:
        i, j = q.popleft()
        for d in dir:
            ni, nj = i+d[0], j+d[1]
            if 0<=ni<n and 0<=nj<m:
                if maps[ni][nj] == 'E':
                    return answer+visit[i][j]
                if maps[ni][nj] in ['S', 'O'] and visit[ni][nj] == 0:
                    q.append([ni, nj])
                    visit[ni][nj] = visit[i][j] + 1
    return -1