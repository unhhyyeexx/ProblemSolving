from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        now = q.popleft()
        state = 0
        for i in q:
            state += 1
            if now > i:
                break
        answer.append(state)
    
    return answer