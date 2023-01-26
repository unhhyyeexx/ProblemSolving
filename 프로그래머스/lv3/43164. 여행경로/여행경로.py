from collections import deque

def solution(tickets):
    answer = []
    q = deque()
    q.append(("ICN", ["ICN"], []))
    
    while q:
        airport, path, visit = q.popleft()
        if len(visit) == len(tickets):
            answer.append(path)
        for idx, ticket in enumerate(tickets):
            if ticket[0] == airport and not idx in visit:
                q.append((ticket[1], path+[ticket[1]], visit+[idx]))
    
    answer.sort()
    return answer[0]