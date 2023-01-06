n, k = map(int, input().split())
value = [int(input()) for _ in range(n)]

dp = [int(1e9)]*(k+1)
dp[0] = 0

for i in range(n):
    for j in range(value[i], k+1):
        dp[j] = min(dp[j], dp[j-value[i]] + 1)

if dp[-1] == int(1e9):
    print(-1)
else:
    print(dp[-1])