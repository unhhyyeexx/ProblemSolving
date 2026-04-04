import sys
input = sys.stdin.readline
import heapq
INF = 10e8

v, e = map(int, input().split(" "))
k = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    u, w, c = map(int, input().split(" "))
    graph[u].append((c, w))

distance = [INF] * (v+1)
def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue

        for cost, next in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next]:
                distance[next] = new_cost
                heapq.heappush(pq, (new_cost, next))

dijkstra(k)

for dist in distance[1:]:
    if dist != INF:
        print(dist)
    else:
        print("INF")