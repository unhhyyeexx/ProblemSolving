import sys
input = sys.stdin.readline

# 인덱스 기준 직진 방향
dir = [[-1,0],[0,1],[1,0],[0,-1]]
def robot(r, c, d):
    clean = 0
    stop = 0

    while not stop:
        blank = 1
        # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        if maps[r][c] == 0:
            maps[r][c] = 2
            clean += 1

        # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
        for _ in range(4):
            # 3-1. 반시계 방향으로 90도 회전한다.
            d = (d+3)%4
            ni, nj = r + dir[d][0], c + dir[d][1]
            # 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            if 0<=ni<N and 0<=nj<M and maps[ni][nj] == 0:
                r, c = ni, nj
                blank = 0
                break    
        
        # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우, (blank = 1)
        if blank == 1:
        # 2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            bi, bj = r-dir[d][0], c-dir[d][1]
            if 0<=bi<N and 0<=bj<M and maps[bi][bj] != 1:
                r, c = bi, bj
                continue
            # 2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            else:
                stop = 1
    
    return clean


N, M = map(int, input().split())
R, C, D = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
print(robot(R, C, D))