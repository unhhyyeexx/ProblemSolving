import sys
input = sys.stdin.readline
from collections import deque


def dfs(idx, sum):
    global answer

    if idx == n:
        if sum == s:
            answer += 1
        return
    
    dfs(idx+1, sum)
    dfs(idx+1, sum+nums[idx])
    

n, s = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
dfs(0,0)

if s == 0:
    answer -= 1
    
print(answer)