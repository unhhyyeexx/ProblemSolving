# 28325 호숫가의 개미굴 gold 5 KOI 2023 2차

import sys
input = sys.stdin.readline

def solution(arr):
    total = sum(arr)
    if total == 0:
        return n//2
    
    i = 0
    for i, c in enumerate(arr):
        if c:
            break
    arr = arr[i+1:] + arr[:i+1]

    dp = [0] * n
    for i in range(n):
        if arr[i] or dp[i]:
            continue

        for j in range(i, n):
            if arr[i]:
                break
            dp[j] = 1
        total += (j-i+1) // 2

    return total
    

n = int(input())
cs = list(map(int, input().split()))

print(solution(cs))