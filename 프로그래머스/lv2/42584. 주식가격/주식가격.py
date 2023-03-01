from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    
    while q:
        now = q.popleft()
        sec = 0
        for i in q:
            sec += 1
            if now > i:
                break
        answer.append(sec)
    
    return answer