import sys
input = sys.stdin.readline
from collections import deque

def solution(graph, root):
    q = deque()
    q.append(1)

    while q:
        now = q.popleft()
        for next in graph[now]:
            if root[next] == 0:
                root[next] = now
                q.append(next)

n = int(input())
graph = [[] for _ in range(n+1)]
root = [0] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

solution(graph, root)
for r in root[2:]:
    print(r)