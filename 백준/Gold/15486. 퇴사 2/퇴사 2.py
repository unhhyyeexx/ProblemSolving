import sys
input = sys.stdin.readline

def solution(n, info):

    dp = [0 for _ in range(n+1)]
    for i in range(n):
        dp[i] = max(dp[i], dp[i-1])
        fin_date = i + info[i][0] - 1
        if fin_date < n:
            dp[fin_date] = max(dp[fin_date], dp[i-1] + info[i][1])
    return max(dp)

n = int(input())
info = []
for _ in range(n):
    info.append(list(map(int, input().split())))

print(solution(n, info))