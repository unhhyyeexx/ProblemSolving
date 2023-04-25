import heapq

def solution(n, k, enemy):
    answer = 0
    sum_en = 0
    heap = []
    
    for e in enemy:
        heapq.heappush(heap, -e)
        sum_en += e
        if sum_en > n:
            if k == 0:
                break
            sum_en += heapq.heappop(heap)
            k -= 1
        answer += 1
    return answer