from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    visit = [0] * y
    q = deque([])
    q.append((x, 0))
    while True:
        now, cnt = q.popleft()
        a, b, c = now+n, now*2, now*3
        if a > y and b > y and c > y:
            return -1
        if y in [a,b,c]:
            return cnt + 1
        for i in [a, b, c]:
            if i<=y and visit[i] == 0:
                visit[i] = 1
                q.append((i, cnt+1))
            else:
                continue
    
    return answer