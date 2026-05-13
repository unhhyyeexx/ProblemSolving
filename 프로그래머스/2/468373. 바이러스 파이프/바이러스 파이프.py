from collections import deque

def solution(n, infection, edges, k):
    answer = 0
    
    graph = list([[], [], []] for _ in range(n+1))
    for x, y, t  in edges:
        graph[x][t-1].append(y)
        graph[y][t-1].append(x)
    
    visited = [0 for _ in range(n+1)]
    visited[infection] = 1
    
    def spread(pipe, infections, visited):
        q = deque(infections)
        
        new_visited = visited[:]
        new_infections = infections[:]
        
        while q:
            x = q.popleft()
            
            for y in graph[x][pipe]:
                if not new_visited[y]:
                    new_visited[y] = 1
                    new_infections.append(y)
                    q.append(y)
        return new_visited, new_infections
    
    def dfs(depth, visited, infections):
        nonlocal answer
        
        if depth == k:
            answer = max(answer, visited.count(1))
            return
        
        for pipe in range(3):
            new_visited, new_infections = spread(pipe, infections, visited)
            dfs(depth+1, new_visited, new_infections)
        
    dfs(0, visited, [infection])
        
        
    return answer