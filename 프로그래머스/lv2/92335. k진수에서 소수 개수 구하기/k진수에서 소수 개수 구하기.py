import math
def checkprime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def changenum(x, k):
    result = ''
    while x > 0:
        x, mod = divmod(x, k)
        result += str(mod)
    return result[::-1]

def solution(n, k):
    answer = 0
    new = changenum(n, k)
    tmp = ''
    for s in new:
        if s != '0':
            tmp += s
        else:
            if len(tmp)>0 and checkprime(int(tmp)):
                answer += 1
            tmp = ''
    if len(tmp)>0 and checkprime(int(tmp)):
        answer += 1
    return answer