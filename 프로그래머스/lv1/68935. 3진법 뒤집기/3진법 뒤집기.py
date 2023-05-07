def solution(n):
    answer = 0
    tmp = ''
    while n > 0:
        n, mod = divmod(n, 3)
        tmp += str(mod)
    
    answer = int(tmp, 3)
    return answer