def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)):
        tmp = discount[i:i+10]
        cnt = 0
        for idx, w in enumerate(want):
            if tmp.count(w) != number[idx]:
                break
            else:
                cnt += 1
        if cnt == len(want):
            answer += 1
    return answer