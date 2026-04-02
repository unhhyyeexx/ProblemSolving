import sys
input = sys.stdin.readline
import heapq

n, e = map(int, input().split(" "))
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split(" "))
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split(" "))

def dijkstra(s, e) :
    pq = []
    dist = [float("inf")] * (n+1)

    dist[s] = 0
    heapq.heappush(pq, (0, s))

    while len(pq) > 0:
        cost, now = heapq.heappop(pq)

        if cost > dist[now]:
            continue
        
        for c, next in graph[now]:
            new_cost = dist[now] + c

            if new_cost < dist[next]:
                dist[next] = new_cost
                heapq.heappush(pq, (new_cost, next))
    
    return dist[e]

route1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
route2 = dijkstra(1, v2)  +dijkstra(v2, v1) + dijkstra(v1, n)

if route1 >= float("inf") and route2 >= float("inf"):
    print(-1)
else:
    print(min(route1, route2))