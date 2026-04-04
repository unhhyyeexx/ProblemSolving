import sys
input = sys.stdin.readline
import heapq
INF = float("inf")

n, m, x = map(int, input().split(" "))
graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split(" "))
    graph[a].append((c, b))
    reverse_graph[b].append((c, a))

def dijkstra(start, g):
    distance = [INF] * (n+1)
    pq = []
    distance[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        cost, now = heapq.heappop(pq)
        if cost > distance[now]:
            continue
            
        for c, next in g[now]:
            new_cost = cost + c
            if distance[next] > new_cost:
                distance[next] = new_cost
                heapq.heappush(pq, (new_cost, next))
    
    return distance

# x -> i
dist_from_x = dijkstra(x, graph)
# i-> x
dist_to_x = dijkstra(x, reverse_graph)

answer = 0
for i in range(1, n+1):
    answer = max(answer, dist_to_x[i] + dist_from_x[i])

print(answer)