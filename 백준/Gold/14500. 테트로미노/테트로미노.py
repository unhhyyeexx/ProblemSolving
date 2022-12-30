dir = [[0,1],[0,-1],[1,0],[-1,0]]
def solution(y, x, depth, sumvalue):
    global answer
    if answer >= sumvalue + maxvalue*(4-depth):
        return
    if depth == 4:
        answer = max(answer, sumvalue)
        return
    for d in dir:
        ny = y + d[0]
        nx = x + d[1]
        if nx<0 or ny<0 or nx>=M or ny>=N or visit[ny][nx]:
            continue
        if depth == 2:
            visit[ny][nx] = 1
            new_sum = sumvalue + maps[ny][nx]
            solution(y, x, depth+1, new_sum)
            visit[ny][nx] = 0
        visit[ny][nx] = 1
        new_sum = sumvalue + maps[ny][nx]
        solution(ny, nx, depth+1, new_sum)
        visit[ny][nx] = 0


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
answer = 0
maxvalue = max(map(max, maps))
for i in range(N):
    for j in range(M):
        visit[i][j] = 1
        solution(i, j, 1, maps[i][j])
        visit[i][j] = 0
print(answer)