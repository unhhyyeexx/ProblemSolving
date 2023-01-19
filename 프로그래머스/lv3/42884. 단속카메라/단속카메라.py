def solution(routes):
    answer = 0
    routes.sort(key = lambda x: x[1])
    now = -30001
    
    for route in routes:
        if route[0] > now:
            answer += 1
            now = route[1]
    return answer