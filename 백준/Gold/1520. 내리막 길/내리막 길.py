# dp, dfs
import sys
input = sys.stdin.readline

dir = [[0,1], [0,-1], [1,0], [-1,0]]
def solution(n, m, board, dp, i, j):
    if i == n-1 and j == m-1:
        return 1

    if dp[i][j] == -1:
        dp[i][j] = 0

        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if 0<=ni<n and 0<=nj<m:
                if board[ni][nj] < board[i][j]:
                    dp[i][j] += solution(n, m, board, dp, ni, nj)

    return dp[i][j]

n, m = map(int, input().split())
board = []
dp = [[-1]*m for _ in range(n)]
for _ in range(n):
    line = list(map(int, input().split()))
    board.append(line)

print(solution(n, m, board, dp, 0, 0))