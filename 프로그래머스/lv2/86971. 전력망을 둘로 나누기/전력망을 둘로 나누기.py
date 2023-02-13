from collections import deque

def solution(n, wires):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start):
        visit = [0]*(n+1)
        q = deque([start])
        visit[start] = 1
        cnt = 1
        while q:
            now = q.popleft()
            for i in graph[now]:
                if visit[i] == 0:
                    q.append(i)
                    visit[i] = 1
                    cnt += 1
        return cnt
    
    answer = n
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        answer = min(abs(bfs(a)-bfs(b)), answer)
        
        graph[a].append(b)
        graph[b].append(a)
            
    return answer