import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split(" "))) for _ in range(n)]

dp_max = board[0][:]
dp_min = board[0][:]

for i in range(1, n):
    one, two, three = dp_max
    dp_max[0] = max(one, two) + board[i][0]
    dp_max[1] = max(one, two, three) + board[i][1]
    dp_max[2] = max(two, three) + board[i][2]

    one, two, three = dp_min
    dp_min[0] = min(one, two) + board[i][0]
    dp_min[1] = min(one, two, three) + board[i][1]
    dp_min[2] = min(two, three) + board[i][2]


print(max(dp_max), min(dp_min))