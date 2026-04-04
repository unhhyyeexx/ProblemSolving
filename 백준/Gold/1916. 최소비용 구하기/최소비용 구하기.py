import sys
input = sys.stdin.readline
import heapq
INF = float("inf")

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c= map(int, input().split(" "))
    graph[a].append((c, b))
start, arrive = map(int, input().split(" "))

def dijkstra(start):
    distance = [INF] * (n+1)
    pq = []
    distance[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        dist, now = heapq.heappop(pq)

        if dist > distance[now]:
            continue

        for cost, next in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next]:
                distance[next] = new_cost
                heapq.heappush(pq, (new_cost, next))
    
    return distance[arrive]

print(dijkstra(start))