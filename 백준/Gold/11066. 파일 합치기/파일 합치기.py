import sys
input = sys.stdin.readline
INF = 10**9

t = int(input())
for _ in range(t):
    n = int(input())
    files = [0]+list(map(int, input().split(" ")))

    prefix = [0] * (n+1) # 각 비용을 이용한 부분합을 담고있는 리스트

    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + files[i]

    dp = list([0]*(n+1) for _ in range(n+1))

    for length in range(1, n):
        for i in range(1, n-length+1):
            j = i + length

            dp[i][j] = INF

            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j]

                dp[i][j] = min(dp[i][j], cost)
            
            dp[i][j] += prefix[j] - prefix[i-1]

    print(dp[1][n])