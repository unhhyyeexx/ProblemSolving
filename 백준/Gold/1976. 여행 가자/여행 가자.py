# 여행가자
# gold 4
# 그래프 탐색, 분리 집합

import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을때까지 재귀적으로 호출
    if parent[x] != x:
        return find(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b


n = int(input())
m = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if i != j :
            graph[i][j] = graph[j][i]

# 부모 테이블 초기화
parent = [0] * (n+1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(n):
    parent[i] = i

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(parent, i+1, j+1)

# 계획 경로
trip = list(map(int, input().split()))
root = []
for i in trip:
    root.append(find(parent, i))

# 계획에 있는 모든노드의 루트노드는 key노드가 나와야 가능한 계획이 된다
key = find(parent, trip[0])

res = True
for i in root:
    if key != i :
        res = False
        break

if res :
    print("YES")
else:
    print("NO")
