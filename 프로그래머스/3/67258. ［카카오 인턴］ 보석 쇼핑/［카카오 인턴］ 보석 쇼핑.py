def solution(gems):
    n = len(gems)
    answer = [0, n-1]
    kind = set(gems)
    dic = {gems[0]: 1}
    start, end = 0, 0
    while start < n and end < n:
        if len(dic) < len(kind):
            end += 1
            if end == n:
                break
            dic[gems[end]] = dic.get(gems[end], 0) +1
        else:
            if end-start < answer[1]-answer[0]:
                answer = [start, end]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
            
    answer[0] += 1
    answer[1] += 1
    return answer
