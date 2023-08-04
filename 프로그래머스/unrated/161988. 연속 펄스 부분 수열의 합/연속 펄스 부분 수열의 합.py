def solution(sequence):
    answer = 0
    n = len(sequence)
    s1 = s2 = 0
    s1_min = s2_min = 0
    
    pulse = 1
    for idx in range(n):
        s1 += sequence[idx] * pulse
        s2 += sequence[idx] * (-pulse)
        
        answer = max(answer, s1-s1_min, s2-s2_min)
        
        s1_min = min(s1, s1_min)
        s2_min = min(s2, s2_min)
        pulse *= -1
    
    return answer