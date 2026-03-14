import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

def dfs(end, idx, sum, sumList):
    
    if idx == end:
        sumList.append(sum)
        return
    
    dfs(end, idx+1, sum, sumList)
    dfs(end, idx+1, sum+nums[idx], sumList)


n, s = map(int, input().split())
nums = list(map(int, input().split()))

sumA = []
sumB = []

dfs(n//2, 0, 0, sumA)
dfs(n, n//2, 0, sumB)

sumB.sort()

answer = 0

for a in sumA:
    target = s - a
    left = bisect_left(sumB, target)
    right = bisect_right(sumB, target)
    answer += (right - left)

if s == 0:
    answer -= 1
    
print(answer)