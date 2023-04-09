from collections import deque

def solution(board):
    answer = 0
    n = len(board)
    dirs = [[0,1], [1,0], [0,-1], [-1,0]]
    visit = [[0]*n for _ in range(n)]
    q = deque([])
    # i, j, direction, cost//100
    q.append([0,0,-1,0])
    
    while q:
        i, j, d, c = q.popleft()
        
        if i==n-1 and j==n-1 and (answer==0 or answer>c):
            answer = c
        
        for didx, di in enumerate(dirs):
            ni, nj = i+di[0], j+di[1]
            if 0<=ni<n and 0<=nj<n and board[ni][nj]==0:
                if d==didx or d==-1: cost = c + 1
                else: cost = c + 6
                
                if visit[ni][nj] == 0 or visit[ni][nj] >= cost-4:
                    visit[ni][nj] = cost
                    q.append([ni,nj,didx,cost])
                
    return answer*100