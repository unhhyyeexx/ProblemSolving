def solution(sequence):
    answer = 0
    n = len(sequence)
    sum1, sum2 = 0, 0
    min1, min2 = 0, 0
    
    pulse = 1
    for i in range(n):
        sum1 += sequence[i] * pulse
        sum2 += sequence[i] * (pulse*(-1))
         
        answer = max(answer, (sum1-min1), (sum2-min2))
        
        min1 = min(sum1, min1)
        min2 = min(sum2, min2)
        pulse *= -1
    
    return answer