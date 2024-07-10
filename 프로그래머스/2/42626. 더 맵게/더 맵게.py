# # heap을 사용하는 이유 : 일반적인 리스트와 달리 push, pop이후 자동 정렬

import heapq
def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < k:
        if len(scoville) <= 1 and scoville[0] < k:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        answer += 1
    
    return answer