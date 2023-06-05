def solution(n, lost, reserve):
    answer = 0
    just_lost = set(lost) - set(reserve)
    just_reserve = set(reserve) - set(lost)
    
    for i in just_reserve:
        if i-1 in just_lost:
            just_lost.remove(i-1)
            
        elif i+1 in just_lost:
            just_lost.remove(i+1)
    
    answer = n - len(just_lost)
    return answer