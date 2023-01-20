import sys
input = sys.stdin.readline

def check(num):
    l = len(num)
    for i in range(1, l//2 + 1):
        if num[-i:] == num[-(i*2):-i]:
            return False
    else:
        return True

def solution(num, n):
    if len(num) == n:
        print(num)
        exit()
    for i in '123':
        if check(num + str(i)):
            solution(num + str(i), n)
    return

n = int(input())
solution('1', n)