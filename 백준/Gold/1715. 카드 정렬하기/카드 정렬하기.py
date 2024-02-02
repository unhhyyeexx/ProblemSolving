import sys
input = sys.stdin.readline
import heapq

# 차이가 적은 것끼리 먼저 더하는게 유리
n = int(input())
nums = []
for i in range(n):
    heapq.heappush(nums, int(input()))

answer = 0
while True:
    if n == 1 or len(nums) <= 1:
        break
    tmp = heapq.heappop(nums) + heapq.heappop(nums)
    answer += tmp
    heapq.heappush(nums, tmp)

print(answer)