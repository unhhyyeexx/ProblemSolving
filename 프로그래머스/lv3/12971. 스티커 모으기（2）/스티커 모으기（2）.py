def solution(sticker):
    n = len(sticker)
    if n == 1: return sticker[0]

    dp = [[0]*n for _ in range(2)]
    # 0 행은 첫번째 스티커 선택 시
    # 1 행은 첫번째 스티커 미 선택 시
    dp[0][0] = sticker[0]
    dp[0][1] = sticker[0]
    dp[1][1] = sticker[1]
    
    for i in range(2, n-1):
        dp[0][i] = max(dp[0][i-2] + sticker[i], dp[0][i-1])
    for i in range(2, n):
        dp[1][i] = max(dp[1][i-2] + sticker[i], dp[1][i-1])

    return max(dp[0][n-2], dp[1][n-1])