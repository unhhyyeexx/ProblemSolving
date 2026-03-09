import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

dp = [1] * (n+1)

for i in range(n):
    for j in range(i):
        if array[i] > array[j]: # 만약 해당 원소가 전 원소보다 크다면
            dp[i] = max(dp[i], dp[j] + 1)
            # 전 원소에 저장되어 있는 최장수열길이에서 +1 값과 저장되어 있는 수열길이값을 비교해서 큰 값 대입
print(max(dp))

subsequence = [] # 정답 수열
order = max(dp)
for i in range(n-1, -1, -1):
    if dp[i] == order:
        subsequence.append(array[i])
        order -= 1
    
subsequence.reverse()
print(*subsequence)