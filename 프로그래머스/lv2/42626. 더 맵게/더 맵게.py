# heap을 사용하는 이유 : 일반적인 리스트와 달리 push, pop이후 자동 정렬

import heapq
def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
        
    cnt = 0
    while heap[0] < K:
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        cnt += 1
        
        if len(heap) == 1 and heap[0] < K:
            return -1
    return cnt