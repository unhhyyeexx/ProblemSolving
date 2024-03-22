import heapq

def solution(jobs):
    answer = 0
    
    fin = 0 # 처리한 작업 개수
    time = 0 # 현재 시간
    start = -1 # 새로 시작할 시간(전 작업 완료시간)
    q = []
    while fin < len(jobs):
        for a, b in jobs:
            if start < a <= time:
                heapq.heappush(q, (b, a))
        if q:
            now = heapq.heappop(q)
            start = time
            time += now[0]
            answer += time - now[1]
            fin += 1
        else:
            time += 1

    return answer // len(jobs)