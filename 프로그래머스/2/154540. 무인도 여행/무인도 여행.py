import sys
sys.setrecursionlimit(10**6)  

def solution(maps):
    answer = [-1]
    dir = [[0,1], [0,-1], [1,0], [-1,0]]
    n, m = len(maps), len(maps[0])
    visit = [[0]*m for _ in range(n)]
    
    def dfs(i, j):
        if maps[i][j] == 'X':
            return 0
        
        food = int(maps[i][j])
        for di, dj in dir:
            ni, nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<m and not visit[ni][nj]:
                visit[ni][nj] = 1
                food += dfs(ni, nj)
        return food
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visit[i][j]:
                visit[i][j] = 1
                answer.append(dfs(i, j))
                visit[i][j] = 0
    if len(answer) == 1:
        return answer
    return sorted(answer[1:])