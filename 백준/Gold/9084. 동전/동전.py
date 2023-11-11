# dp
import sys
input = sys.stdin.readline

def solution(coins, m):
    dp = [0] * (m+1)
    # 0원을 만드는 방법은 무조건 1개 존재
    dp[0] = 1
    for coin in coins:
        for i in range(m+1):
            if i >= coin:
                dp[i] += dp[i-coin]

    return dp[m]



for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    print(solution(coins, m))