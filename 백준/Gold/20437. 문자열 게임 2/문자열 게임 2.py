# boj 20437 문자열 게임2 gold5

import sys
input = sys.stdin.readline
from collections import defaultdict

def solution(w, k):
    dic = defaultdict(list)
    if k == 1:
        print(1,1)
        return

    else:
        for idx, s in enumerate(w):
            dic[s].append(idx)
        minv, maxv = 10001, -1
        for v in dic.values():
            if len(v) >= k:
                for i in range(len(v)-k+1):
                    if minv > v[i+k-1] - v[i] + 1:
                        minv = v[i+k-1] - v[i] + 1
                    if maxv < v[i+k-1] - v[i] + 1:
                        maxv = v[i+k-1] - v[i] + 1
        if minv == 10001 or maxv == -1:
            print(-1)
            return

        print(minv, maxv)
        return 


for _ in range(int(input())):
    w = list(input().strip())
    k = int(input())
    solution(w, k)