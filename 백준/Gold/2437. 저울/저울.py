# boj 2437 저울 gold2

import sys
input = sys.stdin.readline

def solution(ws):
    now = 1
    for i in range(n):
        if now < ws[i]:
            break
        now += ws[i]

    return now

n = int(input())
ws = list(map(int, input().split()))
print(solution(sorted(ws)))