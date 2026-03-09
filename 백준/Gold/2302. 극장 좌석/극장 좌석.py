import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
vip = [int(input()) for _ in range(m)]

dp = [0] * 41
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, 41):
    dp[i] = dp[i-1] + dp[i-2]

answer = 1
prev = 0

for v in vip:
    length = v - prev - 1
    answer *= dp[length]
    prev = v

# 마지막 구간
length = n - prev
answer *= dp[length]

print(answer)