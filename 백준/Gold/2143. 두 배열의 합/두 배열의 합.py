# boj 2143 두 배열의 합 gold3

import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

answer = 0
dic = defaultdict(int)
for i in range(n):
    for j in range(i, n):
        dic[sum(a[i:j+1])] += 1
for i in range(m):
    for j in range(i, m):
        answer += dic[t - sum(b[i:j+1])]

print(answer)