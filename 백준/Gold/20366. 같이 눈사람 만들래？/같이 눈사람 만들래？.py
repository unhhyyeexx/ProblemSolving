# boj 20366 같이 눈사람 만들래? gold3

import sys
input = sys.stdin.readline

n = int(input())
dm = list(map(int, input().split()))
dm.sort()

answer = int(1e9)
for i in range(n-3):
    for j in range(i+3, n):
        anna = dm[i] + dm[j]
        left, right = i+1, j-1 # 엘사 눈사람 정하기
        
        while left < right:
            elsa = dm[left] + dm[right]
            if anna-elsa > 0:
                left += 1
            elif anna-elsa < 0 :
                right -= 1
            else:
                print(0)
                exit()

            answer = min(answer, abs(anna-elsa))

print(answer)