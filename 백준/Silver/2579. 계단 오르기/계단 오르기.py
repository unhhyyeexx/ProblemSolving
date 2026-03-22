import sys
input = sys.stdin.readline

n = int(input())
values = [0] + [int(input()) for _ in range(n)]

if n == 1:
    print(values[1])
elif n==2:
    print(values[1] + values[2])
else:
    dp = [[0]*2 for _ in range(n+1)] # 연속 밟은 거 / 연속 안밟은거

    dp[1][0], dp[1][1] = values[1], values[1]
    dp[2][0], dp[2][1] = values[1] + values[2], values[2]
    
    for i in range(3, n+1):
        dp[i][0] = dp[i-1][1] + values[i]
        dp[i][1] = max(dp[i-2]) + values[i]
    
    print(max(dp[n]))