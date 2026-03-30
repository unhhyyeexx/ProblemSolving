import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]

# dp[x][y] = (x,y)에서 목적지까지 가는 경로 수
dp = [[-1]*n for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    # 목적지 도착
    if x == m-1 and y == n-1:
        return 1

    # 이미 계산된 경우
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if board[nx][ny] < board[x][y]:
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0,0))