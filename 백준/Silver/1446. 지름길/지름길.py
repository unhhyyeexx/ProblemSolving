import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


# 간선의 개수, 노드의 개수 (지름길 수, 고속도로 거리)
n, d = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(d+1)]
# 0번은 취급하지 않기 위해서 n+1 길이만큼 생성

# 최단거리테이블을 모두 무한으로 초기화
distance = [INF] * (d+1)

# 일단 거리 1로 초기화
for i in range(d):
    graph[i].append((i+1, 1))

# 모든 간선정보 입력받기
for i in range(n):
    s, e, dist = map(int, input().split())
    if e > d:
        continue
    graph[s].append((e, dist))

# 다익스트라 알고리즘 = 방문처리 여부를 확인 할 필요가 없다.
def dijkstra(start):
    q = []

    # t시작 노드로 가기 위한 최단경로는 0으로 설정하고 우선순위 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # 큐가 빌 때까지
    while q:
        # 거리가 가장 짧은 노드를 큐에서 꺼낸다.
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시 (방문이 되었는지 확인하는 것과 같은 로직)
        # 현재 꺼낸 그 원소의 거리값(dist)이 테이블에 기록되어 있는 값보다 더 크다면, 이미 처리된 것
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(0)
print(distance[d])