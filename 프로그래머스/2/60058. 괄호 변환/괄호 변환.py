def sep(s):
    a, b = 0, 0
    for i in range(len(s)):
        if s[i] == '(':
            a += 1
        else:
            b += 1 
        if a == b:
            return s[:i+1], s[i+1:]

def isCollect(s):
    q = []
    for i in s:
        if i == '(':
            q.append(i)
        else:
            if len(q) == 0:
                return False
            q.pop()
    return True

def solution(p):
    if not p: return ''
    if isCollect(p): return p

    u, v = sep(p)
    if isCollect(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        for s in u[1:len(u)-1]:
            if s == '(':
                answer += ')'
            else:
                answer += '('
        
    return answer