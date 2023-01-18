from collections import deque

def bfs(n, computers, i, visit):
    visit[i] = 1
    q = deque([i])
    while q:
        now = q.popleft()
        visit[now] = 1
        for j in range(n):
            if j != now and computers[now][j] == 1:
                if visit[j] == 0:
                    q.append(j)
                

def solution(n, computers):
    answer = 0
    visit = [0]*n
    for i in range(n):
        if visit[i] == 0:
            bfs(n, computers, i, visit)
            answer += 1
    return answer