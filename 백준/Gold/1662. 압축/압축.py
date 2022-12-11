# gold 5 1662 압축
# 자료구조 스택 재귀

import sys
input = sys.stdin.readline

def solution(s):
    stack  = []

    cnt = 0
    tmp = 0
    for i in s:
        if i == '(':
            stack.append([cnt-1, tmp])
            cnt = 0
        elif i == ')':
            info = stack.pop()
            cnt = cnt*info[1] + info[0]
        else:
            cnt += 1
            tmp = int(i)

    return cnt
 
s = input().strip()
print(solution(s))