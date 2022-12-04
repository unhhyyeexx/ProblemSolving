# 1647 도시분할계획
# gold 4
# 그래프 이론, 최소 스패닝 트리 (MST, minimum spanning tree)

# 최소 신장트리 구현 후,
# 마을을 두개로 분리하면서 길의 유지비 합을 최소로 하기 위해 마지막으로 추가된 간선을 빼서 집 하나를 분리한다.

import sys
input = sys.stdin.readline


n, m = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (n + 1)
for i in range(1, n+1):
    parent[i] = i

# find 연산 (특정 원소가 속한 집합 찾기)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산 (두 원소가 속한 집합 찾기)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    if b < a:
        parent[a] = b

# 간선 정보를 담을 리스트와 최소 신장 트리 계산 변수 정의
edges = []
costs = []

# 간선 정보가 주어지고 비용을 기준으로 정렬
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# 간선 정보 비용을 기준으로 오름차순으로 정렬한다.
edges.sort()

# 간선 정보를 하나씩 확인하면서 크루스칼 알고리즘 수행
for i in range(m):
    c, a, b = edges[i]
    # find연산 후, 부모 노드가 다르면 사이클이 발생하지 않으므로 union 연산으 수행한다. => 최소 신장 트리에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        costs.append(c)
        now_cost = c

# 마지막에 추가된 간선비용을 빼준다.
print(sum(costs[:-1]))