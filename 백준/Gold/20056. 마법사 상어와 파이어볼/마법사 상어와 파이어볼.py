import sys
input = sys.stdin.readline

n, m, k = map(int, input().split(" "))
board = [list([] for _ in range(n)) for _ in range(n)]
for _ in range(m):
    r, c, mass, s, d = map(int, input().split(" "))
    board[r-1][c-1].append((mass,s,d))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
while k > 0:
    k -= 1

    # 1. 이동
    new_board = [list([] for _ in range(n)) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) == 0: continue

            while len(board[i][j]) > 0:
                mass,s,d = board[i][j].pop()
                ni = (i+(dx[d] * s)) % n
                nj = (j+(dy[d] * s)) % n
                new_board[ni][nj].append((mass,s,d))

    # 2. 파이어볼 합체 분리
    for i in range(n):
        for j in range(n):
            if len(new_board[i][j]) < 2: continue

            cnt = len(new_board[i][j])
            total_m = 0
            total_s = 0
            even = True
            odd = True

            for mass, s, d in new_board[i][j]:
                total_m += mass
                total_s += s

                if d % 2 == 0:
                    odd = False
                else:
                    even = False

            total_m //= 5
            total_s //= cnt

            new_board[i][j] = [] # 기존 파이어볼 제거

            if total_m == 0:
                continue

            if even or odd:
                dirs = [0,2,4,6]
            else:
                dirs = [1,3,5,7]

            for dd in dirs:
                new_board[i][j].append((total_m,total_s,dd))

    board = new_board

answer = 0
for i in range(n):
    for j in range(n):
        if len(board[i][j]) > 0:
            for mass,s,d in board[i][j]:
                answer += mass

print(answer)