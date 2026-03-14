import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
population = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for i in range(n):
    data = list(map(int, input().split()))
    for x in data[1:]:
        graph[i].append(x-1)

def bfs(group):
    visited = set()
    start = next(iter(group))
    q = deque([start])
    visited.add(start)

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if nxt in group and nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
    
    return len(visited) == len(group)

answer = float('inf')

for mask in range(1, 1<<n):
    A = set()
    B = set()

    for i in range(n):
        if mask & (1<<i):
            A.add(i)
        else:
            B.add(i)
    
    if not A or not B:
        continue

    if bfs(A) and bfs(B):
        sumA = sum(population[i] for i in A)
        sumB = sum(population[i] for i in B)

        answer = min(answer, abs(sumB - sumA))

print(answer if answer != float('inf') else -1)