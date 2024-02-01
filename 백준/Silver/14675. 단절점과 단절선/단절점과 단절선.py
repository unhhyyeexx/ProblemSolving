import sys
input = sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# 1정점 2간선
q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 2:
        print('yes')
    elif t == 1:
        if len(graph[k]) == 1:
            print('no')
        else:
            print('yes')