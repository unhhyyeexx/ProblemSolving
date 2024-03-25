# boj 1202 보석 도둑 gold 2

import sys
input = sys.stdin.readline
import heapq

n, k = map(int, input().split())

gems, bags = [], []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(gems, (m, v))

for _ in range(k):
    bags.append(int(input()))
bags.sort()

answer = 0
tmp = []
for bag in bags:
    while gems:
        if bag >= gems[0][0]:
            heapq.heappush(tmp, -heapq.heappop(gems)[1])
        else:
            break
    if tmp:
        answer -= heapq.heappop(tmp)

print(answer)