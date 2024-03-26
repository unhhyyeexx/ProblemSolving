# boj 1005 ACM Craft gold 3
# 위상정렬, dp
# 진입차수(해당 노드를 향하는 간선개수)가 0인 모든 노드를 큐에 넣고, 큐가 빌 때까지
# 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거, 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    n, k = map(int, input().split())
    duration = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    q = deque()
    for i in range(1, n+1):
        if not indegree[i]:
            q.append(i)
            dp[i] = duration[i-1]
    
    while q:
        now = q.popleft()
        for next in graph[now]:
            indegree[next] -= 1
            dp[next] = max(dp[next], dp[now]+duration[next-1])
            if indegree[next] == 0:
                q.append(next)
    
    w = int(input())
    print(dp[w])
        
