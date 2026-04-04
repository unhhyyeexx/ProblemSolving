import sys
input = sys.stdin.readline
INF = float("inf")

n = int(input())
matrix = [list(map(int, input().split(" "))) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
# dp[i][j]: i번째~j번째 행렬을 곱하는 최소 비용

for length in range(2, n+1):
    for i in range(n-length+1):
        j = i + length - 1
        dp[i][j] = INF

        for k in range(i, j):
            cost = (
                dp[i][k]
                + dp[k+1][j] 
                + matrix[i][0] * matrix[k][1] * matrix[j][1]
            )
            dp[i][j] = min(dp[i][j], cost)
        
print(dp[0][n-1])