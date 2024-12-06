import sys
import heapq
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[sys.maxsize for _ in range(N)]for _ in range(N)]


def dijkstra(a, b):
    q = []
    heapq.heappush(q, (0, a, b))
    visited[a][b] = 0
    while q:
        height, x, y = heapq.heappop(q)
        if visited[x][y] < height:
            continue
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                nheight = max(height, abs(arr[nx][ny]-arr[x][y]))
                if visited[nx][ny] > nheight:
                    visited[nx][ny] = nheight
                    heapq.heappush(q, (nheight, nx, ny))


dijkstra(0, 0)
print(visited[N-1][N-1])