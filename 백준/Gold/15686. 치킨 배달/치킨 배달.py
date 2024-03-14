# 15686 치킨배달 gold 5

import sys
input = sys.stdin.readline
from itertools import combinations

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

answer = int(1e9)
for chichen in combinations(chickens, m):
    total = 0
    for home in homes:
        dist = int(1e9)
        for i in range(m):
            dist = min(dist, (abs(home[0]-chichen[i][0]) + abs(home[1]-chichen[i][1])))
        total += dist
    answer = min(answer, total)

print(answer)