import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (k+1)

for weight, value in items:
    for w in range(k, weight-1, -1):
        dp[w] = max(dp[w], dp[w-weight] + value)
        
print(dp[k])