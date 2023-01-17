import heapq
INF = int(1e9)

def solution(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        time, now = heapq.heappop(q)
        if distance[now] < time:
            continue
        for i in graph[now]:
            cost = time + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
graph_re = [[] for _ in range(N+1)]
distance_re = [INF] * (N+1)

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))
    graph_re[e].append((s, t))

solution(X, graph, distance)
solution(X, graph_re, distance_re)

result = 0
for i in range(1, N+1):
    result = max(result, distance[i] + distance_re[i])

print(result)