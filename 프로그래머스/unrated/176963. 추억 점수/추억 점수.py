def solution(name, yearning, photo):
    answer = []
    scores = dict()
    for n, y in zip(name, yearning):
        scores[n] = y
    for i in photo:
        score  = 0
        for j in i:
            if j in scores:
                score += scores[j]
        answer.append(score)                
    return answer