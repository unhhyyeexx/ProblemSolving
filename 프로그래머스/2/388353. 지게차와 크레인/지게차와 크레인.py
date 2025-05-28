def solution(storage, requests):
    answer = 0
    n, m = len(storage), len(storage[0])
    storage = [list(s) for s in storage]
    
    board = []
    for i in range(n):
        if i==0 or i==n-1:
            board.append([0]*m)
        else:
            board.append([0] + [1]*(m-2) + [0])
    
    dir = [[0,1], [0,-1], [1,0], [-1,0]]
    def makezero(i, j):
        for di, dj in dir:
            ni, nj = i+di, j+dj
            if (0<=ni<n and 0<=nj<m and board[ni][nj] == 1):
                board[ni][nj] = 0
                if storage[ni][nj] == 0:
                    makezero(ni, nj)
    
    def deleteOne(word):
        zerolist = []
        for i in range(n):
            for j in range(m):
                if storage[i][j] == word and board[i][j] == 0:
                    storage[i][j] = 0
                    zerolist.append([i, j])
        for i, j in zerolist:
            makezero(i, j)
    
    def deleteAll(word):
        zerolist = []
        for i in range(n):
            for j in range(m):
                if storage[i][j] == word:
                    storage[i][j] = 0
                    if board[i][j] == 0:
                        zerolist.append([i, j])
        for i, j in zerolist:
            makezero(i, j)
                    
    for request in requests:
        if len(request) == 1:
            deleteOne(request[0])
        else:
            deleteAll(request[0])
    
    answer = n*m
    for st in storage:
        answer -= st.count(0)
                
    return answer