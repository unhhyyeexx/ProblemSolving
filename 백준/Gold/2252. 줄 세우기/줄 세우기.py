# boj 2252 줄 세우기 gold3

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
pre = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    pre[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

answer = []
while q:
    now = q.popleft()
    answer.append(now)
    for i in pre[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(*answer)