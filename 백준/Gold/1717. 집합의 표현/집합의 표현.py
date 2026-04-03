import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split(" "))
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra > rb:
        parent[ra] = rb
    elif ra < rb:
        parent[rb] = ra

for _ in range(m):
    op, a, b = map(int, input().split(" "))
    if op == 0:
        union(a, b)
    elif op == 1:
        if find(a) == find(b):
            print("yes")
        else:
            print("no")
