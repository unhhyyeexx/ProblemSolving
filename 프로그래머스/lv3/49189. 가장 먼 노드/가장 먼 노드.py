from collections import deque

def solution(n, edge):
    answer = 1
    
    visit = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    
    visit[1] = 1
    q = deque([1])
    
    while q:
        now = q.popleft()
        for next in graph[now]:
            if visit[next] == 0:
                visit[next] = visit[now] + 1
                q.append(next)
    maxv = max(visit)
    answer = max(answer, visit.count(maxv))
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))