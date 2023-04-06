import heapq
def solution(n, s, a, b, fares):
    
    def dijkstra(start):
        res = [float('INF') for _ in range(n+1)]
        res[start] = 0
        q = []
        heapq.heappush(q, (res[start], start))
        while q:
            res_x, x = heapq.heappop(q)
            for y, cost in graph[x]:
                if res[y] > res_x + cost:
                    res[y] = res_x + cost
                    heapq.heappush(q, ([res[y], y]))
        return res
    
    answer = 200000001
    graph = [[] for _ in range(n+1)]
    for x, y, c in fares:
        graph[x].append((y, c))
        graph[y].append((x, c))
        
    dist = [[]]
    for i in range(1, n+1):
        dist.append(dijkstra(i))
    
    for i in range(1, n+1):
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])
    
    return answer
