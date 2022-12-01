def solution(k, score):
    answer = []
    
    for i in range(len(score)):
        tmp = sorted(score[:i+1])
        if i < k:
            answer.append(tmp[0])
        else:
            answer.append(tmp[-k])
    return answer