def dfs(i, n, computers, visit):
    visit[i] = 1
    for j in range(n):
        if visit[j] == 0 and computers[i][j] == 1:
            dfs(j, n, computers, visit)


def solution(n, computers):
    answer = 0
                
    visit = [0] * n
    for i in range(n):
        if visit[i] == 0:
            dfs(i, n, computers, visit)
            answer += 1
        
    return answer