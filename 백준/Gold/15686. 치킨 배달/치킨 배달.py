# 15686 치킨배달 gold 5
# combinations대신 백트래킹으로 구현

import sys
input = sys.stdin.readline

def dfs(idx, depth):
    global answer

    if depth == m:
        total = 0

        for home in homes:
            dist = int(1e9)
            for j in range(len(visit)):
                if visit[j]:
                    dist = min(dist, (abs(home[0]-chickens[j][0]) + abs(home[1]-chickens[j][1])))
            total += dist
        answer = min(answer, total)

        return
    
    for i in range(idx, k):
        if not visit[i]:
            visit[i] = 1
            dfs(i+1, depth+1)
            visit[i] = 0



n, m = map(int, input().split())
board = []
chickens = []
homes = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 2:
            chickens.append((i, j))
        elif tmp[j] == 1:
            homes.append((i, j))

k = len(chickens)
answer = int(1e9)
visit = [0] * k
dfs(0, 0)
print(answer)