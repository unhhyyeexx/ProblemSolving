n = int(input())

dp = [0]*(n+1)

for i in range(2, n+1):
    dp[i] = dp[i - 1] + 1
    if i%3 == 0:
        one = dp[i//3] + 1
        dp[i] = min(dp[i], one)
    if i%2 == 0:
        two = dp[i//2] + 1
        dp[i] = min(dp[i], two)

print(dp[-1])