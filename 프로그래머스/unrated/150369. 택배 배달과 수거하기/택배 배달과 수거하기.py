def solution(cap, n, deliveries, pickups):
    answer = 0
    # 물류창고랑 먼 거리부터 탐색
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    
    d, p = 0, 0
    
    for i in range(n):
        d += deliveries[i]
        p += pickups[i]
        
        while d > 0 or p >0:
            d -= cap
            p -= cap
            answer += (n-i) * 2
    return answer