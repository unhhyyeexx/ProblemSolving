import sys
input = sys.stdin.readline

n = int(input())
costs = list(map(int, input().split()))
values = list(map(int, input().split()))

dp = [0] * (100)

for i in range(n):
    cost = costs[i]
    value = values[i]
    for w in range(99, cost-1, -1):
        dp[w] = max(dp[w], dp[w-cost] + value)

print(max(dp))