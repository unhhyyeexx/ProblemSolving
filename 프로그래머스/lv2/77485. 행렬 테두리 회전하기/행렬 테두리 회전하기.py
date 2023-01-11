def solution(r, c, queries):
    answer = []
    maps = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            maps[i][j] = c*i + j + 1
    for q in queries:
        b, a, d, c = q[0]-1, q[1]-1, q[2]-1, q[3]-1
        tmp = maps[b][a]
        minnum = tmp
        i, j = b, a
        for k in range(a+1, c+1):
            now = maps[i][k]
            maps[i][k] = tmp
            tmp = now
            j = k
            minnum = min(minnum, tmp)
        for k in range(b+1, d+1):
            now = maps[k][j]
            maps[k][j] = tmp
            tmp = now
            i = k
            minnum = min(minnum, tmp)
        for k in range(c-1, a-1, -1):
            now = maps[i][k]
            maps[i][k] = tmp
            tmp = now
            j = k
            minnum = min(minnum, tmp)
        for k in range(d-1, b-1, -1):
            now = maps[k][j]
            maps[k][j] = tmp
            tmp = now
            i = k
            minnum = min(minnum, tmp)
        answer.append(minnum)
    return answer