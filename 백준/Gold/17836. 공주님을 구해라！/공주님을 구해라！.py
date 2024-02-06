from collections import deque
from copy import deepcopy

dir = [[0,-1],[0,1],[-1,0],[1,0]] #상하좌우
def nogram(s):
    board = deepcopy(maps)
    q = deque()
    q.append(s)
    board[s[1]][s[0]] = 1
    answer = 1e9
    check = 0
    
    while q:
        now = q.popleft()
        x, y = now[0], now[1]
        if board[y][x] >= T:
            break
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            if board[ny][nx] != 0 and board[ny][nx] != -1:
                continue
            if board[ny][nx] == -1:
                check = 1
                answer = board[y][x] + 1 + ((M-1) - nx) + ((N-1) - ny)
            board[ny][nx] = board[y][x] + 1
            q.append([nx, ny])

    if board[N-1][M-1] != 0:
        return min(board[N-1][M-1], answer)
    if check == 1:
        return answer
    return 0

N, M, T = map(int, input().split())
maps = []
start = (0, 0)
for i in range(N):
    tmp = list(map(int, input().split()))
    maps.append(tmp)
    for j in range(M):
        if tmp[j] == 2:
            maps[i][j] = -1

result = nogram(start)
if result == 0:
    print('Fail')
elif result - 1 <= T:
    print(result - 1)
else:
    print('Fail')