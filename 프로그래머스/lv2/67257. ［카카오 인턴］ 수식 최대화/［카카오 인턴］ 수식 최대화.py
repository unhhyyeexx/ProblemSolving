from itertools import permutations as permu

def solution(expression):
    answer = 0
    lis = []
    oper = set()
    tmp = ''
    for e in expression:
        if e in ['+', '-', '*']:
            lis.append(tmp)
            tmp = ''
            lis.append(e)
            oper.add(e)
        else:
            tmp += e
    if tmp:
        lis.append(tmp)
    opers = list(permu(list(oper), len(oper)))
    
    for o in opers:
        copy_lis = lis[:]
        for i in o:
            while i in copy_lis:
                idx = copy_lis.index(i)
                copy_lis[idx-1:idx+2] = [str(eval("".join(copy_lis[idx-1:idx+2])))]
        answer = max(abs(int(copy_lis[0])), answer)
    
    return answer