from collections import deque

def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    q = deque([])
    
    for idx, n in enumerate(numbers):
        if len(q):
            while len(q) and q[-1][0] < n:
                answer[q[-1][1]] = n
                q.pop()
        q.append((n, idx))
    return answer