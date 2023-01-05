# 20444 색종이와 가위
# gold 5
# 수학, 이분탐색

import sys
input = sys.stdin.readline

def solution(n, k):
    start, end = 0, n//2
    papers = 0
    while start <= end:
        mid = (start + end) // 2
        papers = (mid+1) * (n-mid+1)

        if papers < k:
            start = mid + 1
        elif papers > k:
            end = mid - 1
        else:
            break
    
    if papers == k:
        return 'YES'
    return 'NO'

n, k = map(int, input().split())
print(solution(n, k))