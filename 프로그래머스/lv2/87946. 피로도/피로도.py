
answer = 0

def dfs(k, dungeons, visit, cnt):
    global answer
    if cnt > answer:
        answer =cnt
        
    for idx, d in enumerate(dungeons):
        if not visit[idx] and k >= d[0]:
            visit[idx] = 1
            dfs(k-d[1], dungeons, visit, cnt+1)
            visit[idx] = 0

def solution(k, dungeons):
    global answer
    
    visit = [0 for _ in range(len(dungeons))]
    dfs(k, dungeons, visit, 0)
        
    return answer