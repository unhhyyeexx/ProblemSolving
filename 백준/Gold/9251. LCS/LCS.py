import sys
input = sys.stdin.readline

def solution(first, second) :
    f, s = len(first), len(second)
    dp = [0] * s

    for i in range(f):
        cnt = 0
        for j in range(s):
            if cnt < dp[j]:
                cnt = dp[j]
            elif first[i] == second[j]:
                dp[j] = cnt + 1
    return max(dp)


first = input().rstrip()
second = input().rstrip()
print(solution(first, second))