def solution(n):
    dp = [1 for _ in range(n+1)]
    if n in [0, 1]:
        return dp[n]
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) %1000000007
    return dp[n]