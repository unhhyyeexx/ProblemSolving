def solution(n, stations, w):
    answer = 0
    i = 0
    now = 1

    while(now <= n) :
        if(i < len(stations) and now >= stations[i]-w) :
            now = stations[i]+w+1
            i += 1
        else :
            now += 2*w+1
            answer += 1
    return answer