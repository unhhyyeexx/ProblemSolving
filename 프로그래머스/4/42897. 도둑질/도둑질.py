def solution(money):
    answer = 0
    n = len(money)
    dp1 = [0] * n
    dp2 = [0] * n
    
    dp1[0] = 0
    dp1[1] = money[1]
    for i in range(2, n):
        dp1[i] = max(dp1[i-1], (dp1[i-2] + money[i]))
    
    dp2[0] = money[0]
    dp2[1] = max(dp2[0], money[1])
    for i in range(2, n-1):
        dp2[i] = max(dp2[i-1], (dp2[i-2] + money[i]))
    
    
    answer = max(dp1[n-1], dp2[n-2])
    
    return answer