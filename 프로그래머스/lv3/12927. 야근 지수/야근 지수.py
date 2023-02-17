import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        i = heapq.heappop(works)
        i += 1
        heapq.heappush(works, i)
    return sum([w*w for w in works])