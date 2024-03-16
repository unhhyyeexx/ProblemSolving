# boj 13549 숨바꼭질 3 gold 5 다익스트라
# dist: 걸리는 최소시간 저장할 배열
# dist[n]이 누나위치이므로 0으로 초기화
# q는 힙큐로 최소값정렬되도록 하고, 처음에 (0초, 누나위치 n)을 넣어서 시작
# while안에서 (n+1, 1)(n-1, 1)(n*2, 0) // (가는 위치, 걸리는 시간) 돌면서
# if문으로 지정 거리 벗어나지 않을 동안만, q에 저장된 최소시간보다 현재 걸리는 시간이 더 적다면 업데이트 후 q에 추가


import sys
input = sys.stdin.readline
import heapq

n, k = map(int, input().split())
INF = int(1e9)

def dijkstra(n, k):
    dist = [INF] * (100001)
    dist[n] = 0
    q = []
    heapq.heappush(q, (0, n))
    while q:
        t, d = heapq.heappop(q)
        for now, time in [(d+1, 1), (d-1, 1), (d*2, 0)]:
            if 0<=now<100001 and dist[now]>t+time:
                dist[now] = t + time
                heapq.heappush(q, (dist[now], now))
    print(dist[k])

dijkstra(n, k)