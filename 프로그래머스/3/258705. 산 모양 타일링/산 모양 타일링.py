def solution(n, tops):
    mod = 10007
    dp = [[0]*n for _ in range(2)]
    
    dp[0][0] = 1
    dp[1][0] = 3 if tops[0] else 2
    
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + dp[1][i-1]
        if tops[i]:
            dp[1][i] = dp[0][i-1] * 2 + dp[1][i-1] * 3
        else:
            dp[1][i] = dp[0][i-1] + dp[1][i-1] * 2
            
        dp[0][i] %= mod
        dp[1][i] %= mod
            
    return (dp[0][-1] + dp[1][-1]) % mod