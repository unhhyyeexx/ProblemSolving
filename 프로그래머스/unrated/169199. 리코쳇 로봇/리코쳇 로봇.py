from collections import deque

def solution(board):
    answer = 0
    n, m = len(board), len(board[0])
    ri, rj = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                ri, rj = i, j
    
    dir = [[0,1], [1,0],[0,-1], [-1,0]]
    q = deque()
    q.append([ri, rj])
    visit = [[0]*m for _ in range(n)]
    visit[ri][rj] = 1
    
    while q:
        i, j = q.popleft()
        if board[i][j] == 'G':
            answer = visit[i][j]
        for d in dir:
            ni, nj = i, j
            while True:
                ni, nj = ni+d[0], nj+d[1]
                if (0<=ni<n and 0<=nj<m and board[ni][nj] == 'D') or ni<0 or ni>=n or nj<0 or nj>=m:
                    ni -= d[0]
                    nj -= d[1]
                    break
            if not visit[ni][nj]:
                visit[ni][nj] = visit[i][j] + 1
                q.append([ni,nj])
    
    
    if answer:
        return answer - 1
    return -1