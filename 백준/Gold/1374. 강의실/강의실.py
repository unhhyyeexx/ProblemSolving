# boj 1374 강의실 gold5
# 일단 시작 시간 오름차순으로 정렬
# 그 정렬 배열을 돌면서 힙에 추가
# 근데 추가할 때 추가할 애의 시작시간보다 들어있는 애 끝나는 시간이 작으면 강의실 추가 필요 없으
# 그러므로 힙에서 내보냄
# 끝날때까지 힙에 얼마나 많이 있었나가 얼마나 많은 강의실이 필요한가 ㅇㅇ


import sys
input = sys.stdin.readline
import heapq

n = int(input())
lecture = [list(map(int, input().split())) for _ in range(n)]

lecture.sort(key= lambda x:(x[1]))

q = []
cnt = 0
for l, s, e in lecture:
    while q and q[0] <= s:
        heapq.heappop(q)
    heapq.heappush(q, e)
    cnt = max(cnt, len(q))

print(cnt)
