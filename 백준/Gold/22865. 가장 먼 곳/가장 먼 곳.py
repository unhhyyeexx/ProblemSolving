# dijkstra
import sys
import heapq
INF = int(1e9)

def solution(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))



N = int(sys.stdin.readline())
A, B, C = map(int, sys.stdin.readline().split())
M= int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    D, E, L = map(int, sys.stdin.readline().split())
    graph[D].append((E, L))
    graph[E].append((D, L))

d1 = [INF] * (N+1)
solution(A, d1)
d2 = [INF] * (N+1)
solution(B, d2)
d3 = [INF] * (N+1)
solution(C, d3)

total_d = [0] * (N+1)
for n in range(1, N):
    total_d[n] = min(d1[n], d2[n], d3[n])

result = total_d.index(max(total_d))
print(result)