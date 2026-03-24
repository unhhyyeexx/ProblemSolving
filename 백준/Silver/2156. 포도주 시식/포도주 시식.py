import sys
input = sys.stdin.readline

n = int(input())
amounts = [0] + list(int(input()) for _ in range(n))


if n == 1:
    print(amounts[1])
elif n==2:
    print(amounts[1] + amounts[2])
else:
    dp = [0] * (n+1)
    dp[1] = amounts[1]
    dp[2] = dp[1] + amounts[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-2]+amounts[i], dp[i-3]+amounts[i-1]+amounts[i], dp[i-1])
    
    print(dp[n])