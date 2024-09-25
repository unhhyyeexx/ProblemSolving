import heapq

def solution(N, road, K):
    answer = 0
    INF = 1e9
    
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)
    
    for i in range(len(road)):
        a, b, c = road[i]
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
                
                
    for d in distance:
        if d <= K:
            answer += 1
    
    return answer