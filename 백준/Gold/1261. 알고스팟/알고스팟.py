import sys
input = sys.stdin.readline
import heapq

m, n = map(int, input().split(" "))
board = [list(input().strip()) for _ in range(n)]

dist = [[float("inf")] * m for _ in range(n)]
pq = []

dist[0][0] = 0
heapq.heappush(pq, (0,0,0)) # cost, x, y

dirs = [[0,1], [0,-1], [1,0], [-1,0]]
while len(pq) > 0:
    cost, i, j= heapq.heappop(pq)
    
    if cost > dist[i][j]:
        continue

    for di, dj in dirs:
        ni = i+di
        nj = j+dj
        if 0<=ni<n and 0<=nj<m:
            new_cost = cost + int(board[ni][nj])

            if new_cost < dist[ni][nj]:
                dist[ni][nj] = new_cost
                heapq.heappush(pq, (new_cost, ni, nj))

print(dist[n-1][m-1])