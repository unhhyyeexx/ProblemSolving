def solution(n, stations, w):
    answer = 0
    leng = 2*w +1
    dist = []
    dist.append(stations[0]-w-1)
    dist.append(n-(stations[-1]+w))
    
    for i in range(1, len(stations)):
        dist.append((stations[i]-w-1)-(stations[i-1]+w))
        
    for d in dist:
        if d <= 0:
            continue
        else:
            if d % leng:
                answer += (d//leng) + 1
            else:
                answer += (d//leng)
    return answer