import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split(" ")))

dp1 = [1]*n
dp2 = [1]*n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if nums[i] > nums[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

answer = 1
for i in range(n):
    answer = max(answer, dp1[i]+dp2[i])

print(answer-1)