# boj 11286 절대값 힙

import sys
input = sys.stdin.readline
import heapq

n = int(input())
q = []
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(q, (abs(x), x))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])