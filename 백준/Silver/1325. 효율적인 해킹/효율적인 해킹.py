import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    cnt = 0

    visit = [0]*(n+1)
    visit[start] = 1

    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visit[next]:
                visit[next] = 1
                q.append(next)
                cnt += 1

    return cnt

n, m = map(int, input().split())
graph = list([] for _ in range(n+1))
result = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

for i in range(1, n+1):
    result[i] = bfs(i)
max_value = max(result)

answer = []
for i in range(1, n+1):
    if max_value == result[i]:
        answer.append(i)
print(*answer)