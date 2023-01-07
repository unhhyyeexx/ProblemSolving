import sys
input = sys.stdin.readline

def check(map, n, l):
    sw = [False for _ in range(n)]
    for i in range(n-1):
        if map[i] == map[i+1]:
            continue
        if abs(map[i] - map[i+1]) > 1:
            return False
        if map[i] > map[i+1]:
            tmp = map[i + 1]
            for j in range(i+1, i+1+l):
                if 0 <= j < n:
                    if map[j] != tmp:
                        return False
                    if sw[j] == True:
                        return False
                    sw[j] = True
                else:
                    return False
        else:
            tmp = map[i]
            for j in range(i, i-l, -1):
                if 0 <= j < n:
                    if map[j] != tmp:
                        return False
                    if sw[j] == True:
                        return False
                    sw[j] = True
                else:
                    return False
    return True

def solution(n, l, maps):
    cnt = 0
    for map in maps:
        if check(map, n, l):
            cnt += 1
    return cnt

n, l= map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
trans = []
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(maps[j][i])
    trans.append(tmp)
answer = 0
answer += solution(n, l, maps)
answer += solution(n, l, trans)
print(answer)