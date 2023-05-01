def solution(targets):
    answer, defense = 0, 100000001
    for s, e in sorted(targets, reverse=True):
        if e <= defense:
            defense = s + 0.5
            answer += 1
    
    return answer