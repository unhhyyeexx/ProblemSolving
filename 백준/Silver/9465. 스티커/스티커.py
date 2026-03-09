import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(2)]
    
    dp = [[0]*(n+1) for _ in range(2)]

    dp[0][1] = board[0][0]
    dp[1][1] = board[1][0]

    for i in range(2, n+1):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + board[0][i-1]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + board[1][i-1]
    
    print(max(dp[0][n], dp[1][n]))