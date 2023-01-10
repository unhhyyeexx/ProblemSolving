def solution(n):
    answer = []
    maps = [[0]*(i+1) for i in range(n)]
    sumv = 0
    for i in range(n):
        sumv += (i+1)
    d = 0
    i, j = 0, 0
    dir = [[1,0], [0,1], [-1,-1]]
    maps[0][0] = 1
    while True:
        now = maps[i][j]
        if now == sumv:
            break
        ni, nj = i+dir[d][0], j+dir[d][1]
        if 0<=ni<n and 0<=nj<n and maps[ni][nj] == 0:
            maps[ni][nj] = now + 1
            i, j = ni, nj
        else:
            d = (d+1)%3
    for i in maps:
        answer += i
    return answer