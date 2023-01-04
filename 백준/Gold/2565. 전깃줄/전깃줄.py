# 2565 전깃줄
# gold 5
# dp
# 하나의 전봇대를 기준으로 정렬했을때 나머지 전봇대에서 연속으로 증가하는 수열만큼은 전깃줄이 겹치지 않게 된다.

import sys
input = sys.stdin.readline

def solution(n, maps):
    # 첫번째 전봇대로 정렬
    maps.sort(key=lambda x:x[0])
    # 두번째 전봇대
    map2 = []
    for i in range(n):
        map2.append(maps[i][1])
    dp = [0]*n
    # 두번째 전봇대 최장증가수열
    for i in range(n):
        for j in range(n):
            if map2[i] > map2[j] and dp[i] < dp[j]:
                dp[i] = dp[j]
        dp[i] += 1
    
    return (n-max(dp))

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, maps))