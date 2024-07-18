def solution(enroll, referral, seller, amount):
    answer = [0]*len(enroll)
    num = dict()
    for i, e in enumerate(enroll):
        num[e] = i

    for i, now in enumerate(seller):
        n = num[now]
        a = amount[i]*100
        new = ''
        while True:
            if referral[n] == "-":
                if a//10 >= 1:
                    answer[n] += (a - a//10)
                else:
                    answer[n] += a
                break
            
            if a//10 >= 1:
                answer[n] += (a - a//10)
            else:
                answer[n] += a
                break
            new = referral[n]
            n = num[new]
            a = (a//10)

    return answer