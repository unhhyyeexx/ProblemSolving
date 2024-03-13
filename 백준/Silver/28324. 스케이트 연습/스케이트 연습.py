# 28324 스케이트 연습 silver 4

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.reverse()

v = 0
answer = 0
for i in range(n):
    if v == 0:
        v = 1
    elif v < arr[i]:
        v += 1
    elif v >= arr[i]:
        v = arr[i]

    answer+= v

print(answer)