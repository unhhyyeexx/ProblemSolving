def solution(s):
    answer = ''
    ss = list(s.split(' '))
    for i in ss:
        for j in range(len(i)):
            if j%2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    return answer[:-1]