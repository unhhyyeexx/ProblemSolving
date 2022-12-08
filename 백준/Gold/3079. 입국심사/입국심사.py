# 3079 입국심사
# gold 5
# 이분탐색, 매개변수 탐색

import sys
input = sys.stdin.readline

def solution(t, n, m):
    left, right = min(t), max(t)*m
    answer = max(t)*m

    while left <= right:
        # total: mid시간 동안 검사할 수 있는 총 사람 수
        # mid시간 // 각 심사대의 소요 시간의 총합을 구하면 된다.
        total = 0 
        mid = (left + right) // 2
        for i in range(n):
            total += mid // t[i]
        if total >= m :
            right = mid -1
            answer = min(answer, mid)
        else:
            left = mid + 1

    return answer

n, m = map(int, input().split())    
time = list(int(input()) for _ in range(n))

print(solution(time, n, m))