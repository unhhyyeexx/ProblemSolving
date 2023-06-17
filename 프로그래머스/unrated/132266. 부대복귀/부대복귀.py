# bfs
from collections import deque

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]
    visit = [-1]*(n+1)
    
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)
    
    q = deque([destination])
    visit[destination] = 0
    while q:
        now = q.popleft()
        for node in graph[now]:
            if visit[node] == -1 or visit[node] > visit[now]+1:
                visit[node] = visit[now] + 1
                q.append(node)

    return [visit[i] for i in sources]