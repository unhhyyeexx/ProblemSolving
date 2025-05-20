from collections import defaultdict, Counter

def solution(points, routes):
    answer = 0
    dic = defaultdict(list)
    
    for route in routes:
        idx = 0
        for i in range(1, len(route)):
            r, c = points[route[i-1]-1][0], points[route[i-1]-1][1]
            tr, tc = points[route[i]-1][0], points[route[i]-1][1]
            
            if i == 1:
                dic[idx].append((r, c))
                
            while r != tr:
                if r < tr:
                    r += 1
                else:
                    r -= 1
                idx += 1
                dic[idx].append((r, c))
                
            while c != tc:
                if c < tc :
                    c += 1
                else :
                    c -= 1
                idx += 1
                dic[idx].append((r, c))
                
    for key in dic:
        cnt = Counter(dic[key])
        for key in cnt :
            if cnt[key] > 1:
                answer += 1
    
    return answer