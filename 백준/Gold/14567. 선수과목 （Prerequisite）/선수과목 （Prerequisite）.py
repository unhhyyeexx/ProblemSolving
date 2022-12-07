# 14567 선수과목 (Prerequisite)
# gold 5
# dp, 그래프 이론, 위상 정렬

import sys
input = sys.stdin.readline

from collections import deque, defaultdict

# # dp
# # 과목들을 번호가 낮은 순서대로 정렬해준 후 선수과목이 있으면 +1
# def solution(pres):
#     dp = [1] * (n+1)
#     sub = sorted(pres)
#     for a, b in sub:
#         if dp[b] <= dp[a]:
#             dp[b] = dp[a] + 1
#     return dp[1:]

# n, m = map(int, input().split())
# pres = []
# for i in range(m):
#     a, b = map(int, input().split())
#     pres.append((a, b))
# print(*solution(pres))


# 위상정렬
# : 앞에 진입하는 간선노드가 없는 경우 실행 하는 방식

n, m = map(int, input().split())
cur = [0 for i in range(n+1)]
res = [0 for i in range(n+1)]
pres = defaultdict(list)
q = deque()
for i in range(m):
    a, b = map(int, input().split())
    pres[a].append(b)
    res[b] += 1

for i in range(1, n+1):
    # 진입차수가 0이면
    if res[i] == 0:
        # 진입차수가 0인 것들 q에 삽입
        q.append((i, 1))
        # 1학기에 이수 가능
        cur[i] = 1

while q:
    a, cnt = q.popleft()
    for i in pres[a]:
        res[i] -= 1
        if res[i] == 0:
            q.append((i, cnt+1))
            cur[i] = cnt + 1
print(*cur[1:])