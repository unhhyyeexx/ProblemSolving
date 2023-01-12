import heapq
import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort()

queue = [0]
for i in range(N):
    if queue[0] <= arr[i][0]:
        heapq.heappop(queue)
    heapq.heappush(queue, arr[i][1])

print(len(queue))