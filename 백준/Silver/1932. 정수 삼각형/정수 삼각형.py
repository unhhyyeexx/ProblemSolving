import sys
input = sys.stdin.readline

n = int(input())
costs = [[0]] + [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*i for i in range(n+1)]
dp[1] = costs[1]

for i in range(2, n+1):
    dp[i][0] = dp[i-1][0] + costs[i][0]
    dp[i][i-1] = dp[i-1][i-2] + costs[i][i-1]
    for j in range(1, i-1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + costs[i][j]

print(max(dp[n]))