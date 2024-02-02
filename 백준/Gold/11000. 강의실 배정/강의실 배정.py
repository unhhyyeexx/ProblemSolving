import sys
input = sys.stdin.readline
import heapq


n = int(input())
lecture = []
for _ in range(n):
    lecture.append(list(map(int, input().split())))

answer = 0
lecture.sort()

room = []
heapq.heappush(room, lecture[0][1])

for i in range(1, n):
    # 현재 회의실 끝나는 시간보다 다음 회의 시작 시간이 빠르면 방 하나 더 필요
    if lecture[i][0] < room[0]:
        heapq.heappush(room, lecture[i][1])
    # 다음 회의 시작시간이 현재 회의 끝나는 시간보다 늦으면 한 방으로 가능
    else:
        heapq.heappop(room)
        heapq.heappush(room, lecture[i][1])

print(len(room))