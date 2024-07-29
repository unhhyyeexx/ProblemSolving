def solution(numbers):
    answer = ''
    tmp = []
    for n in numbers:
        tmp.append(str(n))
    tmp.sort(key=lambda x:x*3, reverse=True)
    
    for t in tmp:
        answer += t
    return str(int(answer))