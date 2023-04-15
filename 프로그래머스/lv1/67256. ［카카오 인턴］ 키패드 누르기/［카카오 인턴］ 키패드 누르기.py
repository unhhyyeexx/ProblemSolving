def solution(numbers, hand):
    answer = ''
    r, l = 12, 10
    for n in numbers:
        if n in [1,4,7]:
            answer += 'L'
            l = n
        elif n in [3,6,9]:
            answer += 'R'
            r = n
        else:
            # 몇번째줄?
            if n == 0:
                n = 11
            rr = (r-1)//3 + 1
            ll = (l-1)//3 + 1
            nn = (n-1)//3 + 1

            rn = abs(rr-nn) + abs(((n-1)%3 + 1) - ((r-1)%3 + 1))
            ln = abs(ll-nn) + abs(((n-1)%3 + 1) - ((l-1)%3 + 1))
            
            if rn < ln or (rn==ln and hand=='right'):
                answer += 'R'
                r = n
            elif ln < rn or (rn==ln and hand=='left'):
                answer += 'L'
                l = n

    return answer