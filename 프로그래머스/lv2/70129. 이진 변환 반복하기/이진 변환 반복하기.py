def solution(s):
    cnt, zero = 0, 0
    while s != '1':
        cnt += 1
        zero += s.count('0')
        s = s.count('1')
        s = bin(s)[2:]
    return [cnt, zero]