# 2470 두 용액
# gold 5
# 투 포인터, 이분탐색, 정렬

import sys
input = sys.stdin.readline

def solution(n, arr):
    arr.sort()
    left, right = 0, n-1
    total = 2000000001
    answer = [arr[left], arr[right]]

    while left < right:
        lv, rv = arr[left], arr[right]
        sum_v = lv + rv
        if (abs(sum_v) < total):
            total = abs(sum_v)
            answer = [lv, rv]
            if total == 0:
                return answer

        if sum_v < 0:
            left += 1
        else: 
            right -= 1
        
    return answer

n = int(input())
value = list(map(int, input().split()))
print(*solution(n, value))