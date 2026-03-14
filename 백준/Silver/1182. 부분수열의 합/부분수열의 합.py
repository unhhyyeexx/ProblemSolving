
import sys
input = sys.stdin.readline

def solution(idx, sum, n, s, nums):
    global answer
    if idx >= n:
        return
    
    sum += nums[idx]

    if sum == s:
        answer += 1

    #현재수를 선택
    solution(idx+1, sum, n, s, nums)
    #현재 수 선택 안함
    solution(idx+1, sum-nums[idx], n, s, nums)


n, s = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
solution(0, 0, n, s, nums)

print(answer)