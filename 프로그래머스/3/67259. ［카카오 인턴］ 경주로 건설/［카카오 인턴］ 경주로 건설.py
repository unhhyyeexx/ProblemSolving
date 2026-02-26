from collections import deque

def bfs(n, board):
    q = deque()
    
    # visit[i][j][d]
    visit = [[[-1]*4 for _ in range(n)] for _ in range(n)]
    
    dirs = [[0,1], [1,0], [-1,0], [0,-1]]
    
    if board[0][1] == 0: 
        visit[0][1][0] = 100
        q.append([0,1,0])
        
    if board[1][0] == 0: 
        visit[1][0][1] = 100
        q.append([1,0,1])
    
    while q:
        ci, cj, cd = q.popleft()
        cv = visit[ci][cj][cd]
        
        for d in range(4):
            di, dj = dirs[d]
            ni, nj = ci+di, cj+dj
            
            if (0<=ni<n and 0<=nj<n and board[ni][nj]==0):
                cost = cv + (100 if cd == d else 600)
                if (visit[ni][nj][d] == -1 or visit[ni][nj][d] > cost):
                    visit[ni][nj][d] = cost
                    q.append([ni, nj, d])
                    
    return min(x for x in visit[n-1][n-1] if x != -1)
    

def solution(board):
    answer = 0
    n = len(board)
    answer = bfs(n, board)
    
    return answer