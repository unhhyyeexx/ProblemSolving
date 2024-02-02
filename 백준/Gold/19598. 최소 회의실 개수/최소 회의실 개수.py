import sys
input = sys.stdin.readline
import heapq

n = int(input())
info = []
for _ in range(n):
    info.append(list(map(int, input().split())))

info.sort()

room = []
heapq.heappush(room, info[0][1])
for i in range(1, n):
    if info[i][0] >= room[0]:
        heapq.heappop(room)
        heapq.heappush(room, info[i][1])
    else:
        heapq.heappush(room, info[i][1])

print(len(room))