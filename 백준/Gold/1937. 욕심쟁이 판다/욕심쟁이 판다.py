# 1937 욕심쟁이 판다 gold 3
# 순서대로 탐색, 첫방문이라면 dfs
# dfs: 재귀로 해당 칸에서 얼마나 진행할 수 있는지, 방문했던 칸이면 그 값 이용
# 결과적으로 갱신이 된 값(현재값이 더 크면 갱신 안됨) 리턴해서 해당 칸에서 얼만큼 갈 수 있는지 알아본다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dir = [[0,1], [0,-1], [1,0], [-1,0]]
def dfs(i, j):
    if dp[i][j]:
        return dp[i][j]
    
    dp[i][j] = 1
    for di, dj in dir:
        ni, nj = i + di, j + dj
        if 0<=ni<n and 0<=nj<n and board[i][j] < board[ni][nj]:
            dp[i][j] = max(dp[i][j], dfs(ni, nj)+1)
            
    return dp[i][j]


n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        dfs(i, j)

answer = 0
for i in dp:
    answer = max(max(i), answer)

print(answer)