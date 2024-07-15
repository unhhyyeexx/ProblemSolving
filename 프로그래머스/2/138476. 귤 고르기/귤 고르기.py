

def solution(k, tangerine):
    answer = 0
    counts = []
    dic = dict()
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else: 
            dic[i] = 1
    dic = dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))
    for i in dic:
        if k <= 0:
            return answer
        k -= dic[i]
        answer += 1
    return answer