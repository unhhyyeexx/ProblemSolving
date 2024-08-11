import heapq

def solution(n, k, enemy):
    answer = 0
    able = 0
    heap = []
    
    for e in enemy:
        heapq.heappush(heap, -e)
        able += e
        if able > n:
            if k == 0:
                break
            able += heapq.heappop(heap)
            k -= 1
            
        answer += 1
    return answer