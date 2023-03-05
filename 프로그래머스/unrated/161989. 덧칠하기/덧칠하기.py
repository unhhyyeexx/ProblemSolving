def solution(n, m, section):
    answer = 0
    dp = [0 for _ in range(n+m)]
    for s in section:
        if dp[s] == 1:
            continue
        else:
            dp[s:s+m] = [1]*m
            answer += 1
        
    return answer