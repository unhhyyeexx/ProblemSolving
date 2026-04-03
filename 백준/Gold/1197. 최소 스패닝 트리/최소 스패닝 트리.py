import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v, e = map(int, input().split(" "))
edges = []
for _ in range(e):
    a, b, c = map(int, input().split(" "))
    edges.append((c, a, b))

edges.sort()

parent = [i for i in range(v+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rx = find(x)
    ry = find(y)

    if rx != ry:
        parent[ry] = rx

answer = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        answer += cost
    
print(answer)