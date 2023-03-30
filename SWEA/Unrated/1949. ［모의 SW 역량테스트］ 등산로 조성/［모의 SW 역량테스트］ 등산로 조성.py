
def dfs(i, j, chance):
    global answer, visit
    answer = max(answer, visit[i][j])
    for d in dir:
        ni, nj = i+d[0], j+d[1]
        if 0<=ni<n and 0<=nj<n and not visit[ni][nj]:
            if maps[i][j] > maps[ni][nj]:
                visit[ni][nj] = visit[i][j] + 1
                dfs(ni, nj, chance)
                visit[ni][nj] = 0
            elif chance and maps[ni][nj]-k < maps[i][j]:
                tmp = maps[ni][nj]
                maps[ni][nj] = maps[i][j] - 1
                visit[ni][nj] = visit[i][j] + 1
                dfs(ni, nj, chance-1)
                visit[ni][nj] = 0
                maps[ni][nj] = tmp

    return

for t in range(int(input())):
    n, k = map(int, input().split())
    maps = []
    top = 0
    for i in range(n):
        tmp = list(map(int, input().split()))
        maps.append(tmp)
        top = max(max(tmp), top)

    answer = 0
    visit = [[0]*n for _ in range(n)]

    dir = [[0,1], [0,-1], [1,0], [-1,0]]
    for i in range(n):
        for j in range(n):
            if maps[i][j] == top:
                visit[i][j] = 1
                dfs(i, j, 1)
                visit[i][j] = 0

    print(f'#{t+1} {answer}')