# boj 14499 주사위 굴리기 gold 4
# east, west, north, south, top, bottom 순서대로 dice 배열
# 동서남북위아래가 주사위의 어느면인지 오더 들어올때마다 갱신
# 그리고 지도에 0이면 주사위 bottom 값(dice[5]) 복사
# 0 아니면 지도 값 주사위 bottom에 복사

import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
# 동1 서2 북3 남4
dir = [[0,0], [0,1], [0,-1], [-1,0], [1,0]]
cmd = list(map(int, input().split()))
dice = [0]*6

for d in cmd:
    ni, nj = x+dir[d][0], y+dir[d][1]
    if not 0<=ni<n or not 0<=nj<m:
        continue

    east, west, north, south, top, bottom = dice

    if d == 1: # 동 => 주사위의 남북 빼고 바뀜
        dice[0], dice[1], dice[4], dice[5] = bottom, top, east, west
    elif d == 2: # 서 => 주사위의 남북 빼고 바뀜
        dice[0], dice[1], dice[4], dice[5] = top, bottom, west, east
    elif d == 3: # 북 => 주사위의 동서 빼고 바뀜
        dice[2], dice[3], dice[4], dice[5] = bottom, top, north, south
    elif d == 4: # 남 => 주사위의 동서 빼고 바뀜
        dice[2], dice[3], dice[4], dice[5] = top, bottom, south, north
    
    if maps[ni][nj] == 0:
        maps[ni][nj] = dice[5]
    else:
        dice[5] = maps[ni][nj]
        maps[ni][nj] = 0
    
    x, y = ni, nj
    print(dice[4])