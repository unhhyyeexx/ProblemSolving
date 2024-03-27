# boj 1766 문제집 gold2

import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
pre = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    pre[a].append(b)
    indegree[b] += 1

answer = []
q = []
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)
for i in range(n):
    now = heapq.heappop(q)
    answer.append(now)
    while pre[now]:
        next = pre[now].pop()
        indegree[next] -=1
        if indegree[next] == 0:
            heapq.heappush(q, next)

print(*answer)