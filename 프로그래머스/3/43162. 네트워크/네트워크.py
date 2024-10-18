
def dfs(n, computers, now, idx, graph):
    graph[now] = idx
    for i in range(n):
        if graph[i] == 0 and computers[now][i] == 1:
            graph[i] = idx
            dfs(n, computers, i, idx, graph)
    return

def solution(n, computers):
    answer = 0
    graph = [0] * (n+1)
    idx = 1
    for gi in range(n):
        if graph[gi] == 0:
            dfs(n, computers, gi, idx, graph)
            idx += 1
    
    answer = max(graph)
        
    return answer