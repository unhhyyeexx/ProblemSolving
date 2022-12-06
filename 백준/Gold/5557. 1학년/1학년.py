import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [[0]*21 for _ in range(N+1)]

dp[1][nums[0]] = 1

for i in range(1, N):
    for j in range(21):
        if dp[i][j] > 0:
            if 0 <= j-nums[i] <= 20:
                dp[i+1][j-nums[i]] += dp[i][j]
            if 0<= j+nums[i] <= 20:
                dp[i+1][j+nums[i]] += dp[i][j]
                
print(dp[N-1][nums[N-1]])