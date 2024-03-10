# boj 11003 최소값 찾기 platinum 5

import sys
input = sys.stdin.readline
from collections import deque

n, l = map(int, input().split())
array = list(map(int, input().split()))

q = deque()
for i in range(n):
    while q and q[-1][0] > array[i]: # 어차피 최소값 구하니까 큰 값은 필요가 없음
        q.pop() # 그러므로 현재 넣을 값보다 큰 값이 있으면 다 제거
    q.append((array[i], i))
    if q[0][1] <= i-l: # 문제에서 정해준 앞쪽 범위를 넘어가면 제거
        q.popleft()   

    # 여기까지 하면 작은 순으로 정렬이 된다. 맨 앞의 값을 빼면 된다.
    print(q[0][0], end=' ')