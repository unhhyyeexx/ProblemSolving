from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque((v, idx) for idx,v in enumerate(priorities))
    while q:
        now = q.popleft()
        if q and now[0] < max(q)[0]:
            q.append(now)
        else:
            answer += 1
            if now[1] == location:
                break
    return answer