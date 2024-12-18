import heapq
import sys
input = sys.stdin.readline
n, m, a, b, c = map(int, input().split())

costs = []
road = [[] for _ in range(n + 2)]
for _ in range(m):
    from_cc, to_cc, ccost = map(int, input().split())
    costs.append(ccost)
    road[from_cc].append((to_cc, ccost))
    road[to_cc].append((from_cc, ccost))

def check_cost(mid):
    distances = [sys.maxsize for _ in range(n + 1)]
    distances[a] = 0
    edge = []
    heapq.heappush(edge, [0, a])  # 비용과 현재 노드
    while edge:
        this_cost, this_node = heapq.heappop(edge)
        # 최단경로 확인한다 : 이미 이번 노드로 가는 비용이 누적 비용보다 적다면 갱신 X
        if distances[this_node] < this_cost:
            continue
        for next_node, next_cost in road[this_node]:
            if distances[next_node] > this_cost + next_cost and next_cost <= mid:
                distances[next_node] = next_cost + this_cost
                heapq.heappush(edge, [this_cost + next_cost, next_node])
    if distances[b] > c:
        return False
    return True
road_max_min = sys.maxsize
costs.sort()
lt = 0
rt = len(costs) -1
while lt <= rt:
    mid = (lt + rt) // 2
    # mid 값을 최대로 갖는 경로가 있는지 확인한다.
    check_res = check_cost(costs[mid])
    if check_res:
        # 있다면 최대 값을 더 줄여본다
        rt = mid -1
        # 답으로 기록한다.
        road_max_min = min(road_max_min, costs[mid])
    else:
        # 없다면 최대값을 더 늘려본다
        lt = mid +1
if road_max_min == sys.maxsize:
    print(-1)
else:
    print(road_max_min)