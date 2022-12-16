import sys

def dfs(idx, depth):
    global answer
    if depth == 5:
        answer = 1
        return
    for j in graph[idx]:
        if not visit[j]:
            visit[j] = 1
            dfs(j, depth+1)
            visit[j] = 0


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
visit = [0]*N
answer = 0

for n in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    if answer == 1:
        break
    visit[i] = 1
    dfs(i, 1)
    visit[i] = 0

print(answer)