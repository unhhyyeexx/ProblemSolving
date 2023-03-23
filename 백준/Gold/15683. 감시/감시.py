import sys
import copy

input = sys.stdin.readline

def dfs(depth, maps):
    global answer

    if depth == len(cctv):
        cnt = 0
        for i in range(n):
            cnt += maps[i].count(0)
        answer = min(answer, cnt)
        return

    tmp = copy.deepcopy(maps)
    cctvn, x, y = cctv[depth]
    for i in mode[cctvn]:
        see(tmp, i, x, y)
        dfs(depth+1, tmp)
        tmp = copy.deepcopy(maps)

    return

def see(maps, direction, x, y):
    for d in direction:
        nx, ny = x, y
        while True:
            nx, ny = nx+dir[d][0], ny+dir[d][1]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                break
            if maps[nx][ny] == 6:
                break
            elif maps[nx][ny] == 0:
                maps[nx][ny] = -1

n, m = map(int, input().split())
cctv = []
maps = []
for i in range(n):
    tmp = list(map(int, input().split()))
    maps.append(tmp)
    for j in range(m):
        if tmp[j] in [1,2,3,4,5]:
            cctv.append([tmp[j], i, j])

dir = [[-1,0], [0,1], [1,0], [0,-1]]
mode = [[], [[0],[1],[2],[3]], [[0,2], [1,3]], [[0,1], [1,2], [2,3], [3,0]], [[0,1,2], [1,2,3], [2,3,0], [0,1,3]], [[0,1,2,3]]]


answer = int(1e9)
dfs(0, maps)
print(answer)