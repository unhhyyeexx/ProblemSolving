from collections import defaultdict
from itertools import combinations as combi

def solution(orders, course):
    answer = []

    for c in course:
        dic = defaultdict(int)
        for order in orders:
            if len(order) >= c:
                tmplist = combi(list(order), c)
                for t in tmplist:
                    t = list(t)
                    t.sort()
                    dic[''.join(t)] += 1
        sortdic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        if not sortdic:
            break
        nows, nown = sortdic[0][0], sortdic[0][1]
        if nown <= 1:
            break
        answer.append(''.join(nows))
        for ss, sn in sortdic[1:]:
            if sn == nown:
                answer.append(''.join(ss))
            else:
                break
    answer.sort()
    return answer