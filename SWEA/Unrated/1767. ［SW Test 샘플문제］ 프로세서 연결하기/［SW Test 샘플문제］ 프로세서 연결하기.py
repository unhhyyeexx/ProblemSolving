def check(i, j):
    d_len = [0, 0, 0, 0]
    for idx, d in enumerate(dir):
        ni, nj = i, j
        length = 0
        while 0<ni<n-1 and 0<nj<n-1:
            length += 1
            ni += d[0]
            nj += d[1]
            if maps[ni][nj]: break
        else: d_len[idx] = length
    return d_len


def reverse(i, j, d):
    ni, nj = i, j
    while 0<ni<n-1 and 0<nj<n-1:
        ni += d[0]
        nj += d[1]
        maps[ni][nj] ^= 1


def dfs(depth, min_v, cnt):
    global answer
    
    if cnt > answer[0]:
        answer = [cnt, min_v]
    elif cnt == answer[0]:
        answer[1] = min(answer[1], min_v)
    
    if depth == core_cnt: return

    i, j = core[depth][0], core[depth][1]
    d_len = check(i, j)
    for d_idx, d in enumerate(dir):
        if d_len[d_idx] == 0: continue
        reverse(i, j, d) # 라인 연결
        dfs(depth+1, min_v+d_len[d_idx], cnt+1)
        reverse(i, j, d) # 라인 지우기
    dfs(depth+1, min_v, cnt) 



for t in range(int(input())):
    answer = [0, 0] #연결된 코어 개수, 라인 길이
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    dir = [[0,1],[1,0],[0,-1],[-1,0]]
    core_cnt = 0
    core = []
    for i in range(1, n-1):
        for j in range(1, n-1):
            if maps[i][j] == 1: 
                core.append([i,j])
                core_cnt += 1
    
    dfs(0,0,0)

    print(f"#{t+1} {answer[1]}")