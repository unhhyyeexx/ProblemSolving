import sys
input = sys.stdin.readline

T, W = map(int, input().split())
info = list(int(input()) for _ in range(T))

dp = [[0]*(W+1) for _ in range(T+1)]
# 홀수번 움직이면 2번, 짝수번 움직이면 1번

for t in range(1, T+1):
    for w in range(W+1):
        # 1. 이동 안함
        dp[t][w] = dp[t-1][w]

        #2. 이동 함
        if w > 0:
            dp[t][w] = max(dp[t][w], dp[t-1][w-1])
        
        # 현재 위치
        pos = 1 if w%2 == 0 else 2

        if pos == info[t-1]:
            dp[t][w] += 1

print(max(dp[T]))