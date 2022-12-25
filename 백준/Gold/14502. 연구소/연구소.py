#0:빈칸 1:벽 2:바이러스
#벽을 임의의 칸에 세우고 바이러스를 퍼뜨리고 안전영역 크기 구하기,,,
#오래 걸릴 것 같은데 좋은 방법을 못찾겠다ㅠ

import copy
from collections import deque

answer = 0

#상하좌우
dir = [[0,-1],[0,1],[-1,0],[1,0]]
#바이러스 퍼트리기
def bfs():
    global answer
    bfsmap = copy.deepcopy(maps)
    virus = copy.deepcopy(virusorigin)
    while virus:
        vxy = virus.popleft()
        x, y = vxy[0], vxy[1]
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if nx<0 or nx>=M or ny<0 or ny>=N or bfsmap[ny][nx]:
                continue
            bfsmap[ny][nx] =2
            virus.append([nx, ny])

    zerocnt = 0
    for oneline in bfsmap:
        zerocnt += oneline.count(0)
    answer = max(answer, zerocnt)


#벽세우기
def wall(now, cnt):
    if cnt == 3:
        bfs()
        return
    for idx in range(now, N*M):
        i = idx // M #행
        j = idx % M #열
        if maps[i][j] == 0:
            maps[i][j] = 1
            wall(idx, cnt+1)
            maps[i][j] = 0


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
virusorigin = deque()
for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            virusorigin.append([j,i])

wall(0,0)
print(answer)