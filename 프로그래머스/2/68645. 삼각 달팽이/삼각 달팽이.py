def solution(n):
    answer = []
    graph = [[0]*(i+1) for i in range(n)]
    finish = 0
    for i in range(1, n+1):
        finish += i
    
    dir = [[1,0], [0,1], [-1,-1]]
    d, i, j = 0, 0, 0
    now = 1
    graph[i][j] = now
    while True:
        if now == finish:
            break
        ni, nj = i+dir[d][0], j+dir[d][1]
        if 0<=ni<n and 0<=nj<n and graph[ni][nj] == 0:
            graph[ni][nj] = now + 1
            i, j = ni, nj
            now += 1
        else:
            d = (d+1)%3
    
    for i in range(n):
        answer += graph[i]
    return answer