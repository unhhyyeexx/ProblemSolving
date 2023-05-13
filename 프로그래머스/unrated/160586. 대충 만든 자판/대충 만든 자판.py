def solution(keymap, targets):
    answer = []
    dic = dict()
    for k in keymap:
        for i in range(len(k)):
            if k[i] in dic:
                dic[k[i]] = min(dic[k[i]], i+1)
            else:
                dic[k[i]] = i+1
    
    for target in targets:
        res = 0
        for t in target:
            if t not in dic:
                res = -1
                break
            else:
                res += dic[t]
        answer.append(res)
    
    return answer