def solution(k, ranges):
    answer = []
    
    n = len(ranges)
    h = [k]
    while k != 1:
        if k % 2 == 0:
            k = k//2
        else:
            k = k*3 + 1
        h.append(k)
    
    for s, e in ranges:
        area = 0
        tmp = h[s:len(h) + e]
        if s >= e + len(h):
            answer.append(-1)
            continue
        for i in range(len(tmp)-1):
            area += (tmp[i] + tmp[i+1]) / 2
        answer.append(area)
        
    return answer