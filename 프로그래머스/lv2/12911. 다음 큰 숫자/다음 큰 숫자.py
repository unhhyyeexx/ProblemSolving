def solution(n):
    answer = 0
    onecnt = bin(n).count('1')
    c = n + 1
    while True:
        if bin(c).count('1') == onecnt:
            return c
        c += 1
    return answer