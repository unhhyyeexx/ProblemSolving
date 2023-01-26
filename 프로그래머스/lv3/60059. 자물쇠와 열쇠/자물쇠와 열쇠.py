def check(nlock):
    n = len(nlock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if nlock[i][j] != 1:
                return False
    return True

def rotate(m, key):
    nkey = [[0]*m for _ in range(m)]
    for r in range(m):
        for c in range(m):
            nkey[c][m - r - 1] = key[r][c]
    return nkey

def solution(key, lock):
    answer = False
    
    n, m = len(lock), len(key)
    nlock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            nlock[n+i][n+j] = lock[i][j]
    

    for i in range(1, n*2):
        for j in range(1, n*2):
            for d in range(4):
                if d != 0:
                    key = rotate(m, key)
                for x in range(m):
                    for y in range(m):
                        nlock[x+i][y+j] += key[x][y]
                if check(nlock) :
                    return True
                for x in range(m):
                    for y in range(m):
                        nlock[x+i][y+j] -= key[x][y]
    
    return answer