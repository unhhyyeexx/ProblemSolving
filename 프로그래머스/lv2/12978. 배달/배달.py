import heapq

def solution(N, road, K):
    answer = 0
    distance = [int(1e9)]*(N+1)
    graph = [[] for _ in range(N+1)]
    for r in road:
        graph[r[0]].append((r[1], r[2]))
        graph[r[1]].append((r[0], r[2]))
        
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, node = heapq.heappop(q)
            if distance[node] < dist:
                continue
            for next in graph[node]:
                cost = distance[node] + next[1]
                if cost < distance[next[0]]:
                    distance[next[0]] = cost
                    heapq.heappush(q, (cost, next[0]))       
    
    dijkstra(1)
    answer = len([i for i in distance if i<=K])
    return answer