# 0 blank 1 enemy
from itertools import combinations
from copy import deepcopy

def solution():
    answer = 0

    originenemies = []
    for i in range(N):
        for j in range(M):
            if maps[i][j]:
                originenemies.append([i, j])

    archers_list = map(list, combinations([i for i in range(M)], 3))
    for archer in archers_list:
        shootcnt = 0
        enemies = deepcopy(originenemies)
        while enemies:
            die_enemy = []
            for idx in archer:
                dieable = []
                for id in range(len(enemies)):
                    dist = abs(enemies[id][0] - N) + abs(enemies[id][1] - idx)
                    if dist <= D:
                        dieable.append([dist, enemies[id][1], id])
                if dieable:
                    dieable.sort(reverse=True)
                    ddist, enemycol, id = dieable.pop()
                    if id not in die_enemy:
                        die_enemy.append(id)
                        shootcnt += 1

            for id in range(len(enemies)):
                if id not in die_enemy:
                    enemies[id][0] += 1
                    if enemies[id][0] == N:
                        die_enemy.append(id)

            if die_enemy:
                for dieid in sorted(die_enemy, reverse=True):
                    enemies.pop(dieid)

        answer = max(answer, shootcnt)
    return answer


N, M, D = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
maps.append([0]*N)

result = solution()
print(result)