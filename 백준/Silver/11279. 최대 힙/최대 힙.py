# boj 11279 최대 힙 silver 2

import sys
input = sys.stdin.readline
import heapq

n = int(input())
q = []
for i in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(q, (-x, x))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])