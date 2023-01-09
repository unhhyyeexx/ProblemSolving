def solution(s):
    answer = []
    arr = list((s[2:-2]).split("},{"))
    arr.sort(key=len)
    tmp = -1
    for a in arr:
        nums = list(a.split(','))
        for n in nums:
            if int(n) not in answer:
                answer.append(int(n))
    return answer