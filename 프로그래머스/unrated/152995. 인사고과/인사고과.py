def solution(scores):
    answer =1
    
    wanho = scores[0]
    wanho_sum = sum(scores[0])
    scores.sort(key = lambda x: (-x[0], x[1]))
    
    limit = 0
    for score in scores:
        if wanho[0] < score[0] and wanho[1] < score[1]:
            return -1
        if limit <= score[1]:
            if wanho_sum < score[0] + score[1]:
                answer += 1
            limit = score[1]
    return answer