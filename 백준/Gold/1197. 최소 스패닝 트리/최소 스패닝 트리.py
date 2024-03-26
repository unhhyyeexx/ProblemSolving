# boj 1197 최소 스패닝 트리 gold4
# 최소신장트리(mst) => Kruskal & Prim 이용.
# Kruskal은 edge(간선)이 적은 문제에 적합. Prim은 많은 문제에 적합

import sys
input = sys.stdin.readline

def solution(edges, parent):
    answer = 0
    def get_parent(x):
        if parent[x] == x:
            return x
        parent[x] = get_parent(parent[x])
        return parent[x]
    
    def union_parent(a, b):
        a = get_parent(a)
        b = get_parent(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        
    def check_parent(a, b):
        return get_parent(a) == get_parent(b)

    edges.sort(key=lambda x:x[2])

    for a, b, c in edges:
        if not check_parent(a, b):
            union_parent(a, b)
            answer += c

    return answer

v, e = map(int, input().split())
edge = []
for _ in range(e):
    edge.append(list(map(int, input().split())))
parenttt = [i for i in range(v+1)]

print(solution(edge, parenttt))