import string

tmp = "0123456789ABCDEF"
def change(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return change(q, base) + tmp[r]

def solution(n, t, m, p):
    answer = ''
    total = ''
    for i in range(m*t):
        total += str(change(i, n))
    
    while len(answer) < t:
        answer += total[p-1]
        p += m
        
    return answer