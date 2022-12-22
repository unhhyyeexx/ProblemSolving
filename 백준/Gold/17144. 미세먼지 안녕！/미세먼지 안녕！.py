#미세먼지 안녕! 송화가루 안녕!
from copy import deepcopy

dir = [[-1,0],[1,0],[0,1],[0,-1]]
ccw = [[0,1],[-1,0],[0,-1],[1,0]]
cw = [[0,1],[1,0],[0,-1],[-1,0]]
def solution():
    originmaps = deepcopy(maps)
    for r in range(R):
        for c in range(C):
            if originmaps[r][c] <= 0:
                continue
            cnt = 0
            for d in dir:
                nr, nc = r+d[0], c+d[1]
                if nr<0 or nc<0 or nr>=R or nc>=C or maps[nr][nc]==-1:
                    continue
                maps[nr][nc] += originmaps[r][c]//5
                cnt += 1
            maps[r][c] = maps[r][c] - ((originmaps[r][c]//5)*cnt)

    originmaps = deepcopy(maps)
    #top counterclockwise
    r1 = cleaner[0]
    maps[r1][1] = 0
    r, c = r1, 1
    idx = 0
    while True:
        nr, nc = r+ccw[idx][0], c+ccw[idx][1]
        if nr<0 or nc<0 or nr>=R or nc>=C:
            idx = (idx+1)%4
            continue
        if maps[nr][nc] == -1:
            break
        maps[nr][nc] = originmaps[r][c]
        r, c = nr, nc
    #bottom clockwise
    r2 = cleaner[1]
    maps[r2][1] = 0
    r, c = r2, 1
    idx = 0
    while True:
        nr, nc = r+cw[idx][0], c+cw[idx][1]
        if nr<0 or nc<0 or nr>=R or nc>=C:
            idx = (idx+1)%4
            continue
        if maps[nr][nc] == -1:
            break
        maps[nr][nc] = originmaps[r][c]
        r, c = nr, nc


R, C, T = map(int, input().split())
maps = []
cleaner = []
for i in range(R):
    tmp = list(map(int, input().split()))
    maps.append(tmp)
    if -1 in tmp:
        cleaner.append(i)
for _ in range(T):
    solution()

result = 0
for i in range(R):
    for j in range(C):
        if maps[i][j] <= 0:
            continue
        result += maps[i][j]

print(result)