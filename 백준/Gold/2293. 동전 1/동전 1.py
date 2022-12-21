# 2293 동전
# gold 5
# dp

import sys
input = sys.stdin.readline

def solution(values, k):
    dp = [0] * (k+1)
    dp[0] = 1
    for v in values:
        for i in range(1, k+1):
            if i-v >= 0:
                dp[i] += dp[i-v]
    return dp[k]

n, k = map(int, input().split())
values = list(int(input()) for _ in range(n))
print(solution(values, k))