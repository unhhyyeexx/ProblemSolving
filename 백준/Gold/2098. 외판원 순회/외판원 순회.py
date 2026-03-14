import sys
input = sys.stdin.readline

INF = 10**9

def dfs(now, visit):
    # 모든 도시 방문
    if visit == (1<<n) - 1:
        if weights[now][0] == 0:
            return INF
        return weights[now][0]
    
    # 이미 계산된 상태
    if dp[now][visit] != -1:
        return dp[now][visit]
    
    dp[now][visit] = INF

    for next in range(n):
        # 이미 방문
        if visit & (1<<next):
            continue
        # 길 없음
        if weights[now][next] == 0:
            continue

        cost = weights[now][next] + dfs(next, visit|(1<<next))
        dp[now][visit] = min(dp[now][visit], cost)
    
    return dp[now][visit]

n = int(input())
weights = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*(1<<n) for _ in range(n)]

print(dfs(0, 1))