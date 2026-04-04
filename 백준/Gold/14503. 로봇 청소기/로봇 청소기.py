import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
r, c, d = map(int, input().split(" "))
dirs = [[-1,0], [0,1], [1,0], [0,-1]] # 북, 동, 남, 서

board = [list(map(int, input().split(" "))) for _ in range(n)]

answer = 0
while True:
    # 현재칸이 청소되지 않은 경우, 현재 칸을 청소한다
    if board[r][c] == 0:
        board[r][c] = 2
        answer += 1
    
    # 현재 칸 주변 4칸 탐색
    clean = False
    for i in range(4):
        d = (d-1+4)%4
        ni = r + dirs[d][0]
        nj = c + dirs[d][1]
        # 앞에 청소되지 않은 칸이 있다면 한칸 전진 후 청소로 돌아감
        if 0<=ni<n and 0<=nj<m and board[ni][nj] == 0:
            clean = True
            r = ni
            c = nj
            break
    
    # 청소되지 않은 빈칸이 없어서 로봇청소기 방향이 원복됐다면
    # 바라보는 방향을 유지한 채 한 칸 후진 (가능하다면)
    if not clean:
        nd = (d+2)%4
        ni = r + dirs[nd][0]
        nj = c + dirs[nd][1]
        if 0<=ni<n and 0<=nj<m and board[ni][nj] != 1:
            r = ni
            c = nj
        else:
            break

print(answer)