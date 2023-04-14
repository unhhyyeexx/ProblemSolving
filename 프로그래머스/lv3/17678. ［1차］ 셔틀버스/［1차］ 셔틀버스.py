def solution(n, t, m, timetable):
    answer = 0
    bus = [9*60 + t*i for i in range(n)]
    crew = [int(time[:2])*60 + int(time[3:5]) for time in timetable]
    crew.sort()

    # 버스에 오를 크루의 idx
    i = 0
    for time in bus:
        cnt = 0 # 현 버스에 탄 크루 수
        # 1.수용인원m명까지 타고, 2.크루수만큼 3.버스시간보다 빨리 온 크루만 탄다
        while cnt<m and i<len(crew) and crew[i]<=time:
            i += 1
            cnt += 1
        # 버스에 자리가 남았으면
        if cnt < m :
            answer = time
        else:
            answer = crew[i-1] - 1
    
    return ("0"+str(answer//60))[-2:] + ":" + ("0"+str(answer%60))[-2:]