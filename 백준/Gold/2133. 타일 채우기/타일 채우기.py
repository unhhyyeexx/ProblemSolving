import sys
input = sys.stdin.readline

def solution(n):
    # n이 홀수일 경우 경우의 수는 0
    dp = [0] * (31)
    # n=2인 경우 경우의 수는 3
    # n=4인 경우 경우의 수는 11 (3*3 + 2)
    # n=6인 경우 경우의 수는 41 (3*3*3 + 2*6 + 2)

    # i-2이면 2칸 비죠 그럼 n=2인 경우를 추가해야됨 !!! 
    # 그러므로 dp[i-2]는 *3을 해줘야 되고,,
    # i-4이면 4칸이 비죠 그럼 n=4인 경우 추가해야되면 2가지 방법 잇음 => *2

    dp[2] = 3
    for i in range(4, 31, 2):
        dp[i] = dp[2] * dp[i-2] 
        # 위에 즉 = 3* dp[i-2]
        for j in range(4, i, 2):
            dp[i] += dp[i-j] * 2
        dp[i] += 2
    return dp[n]

n = int(input())
print(solution(n))