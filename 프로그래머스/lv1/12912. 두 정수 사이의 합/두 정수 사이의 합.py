def solution(a, b):
    answer = 0
    term = abs(b - a) + 1
    if term%2 == 0:
        answer = (a+b) * (term//2)
    else:
        answer = (a+b) * (term//2) + (a+b)//2
    
    return answer