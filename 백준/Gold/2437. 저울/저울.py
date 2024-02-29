
import sys
input = sys.stdin.readline

def solution(weights):
    now = 1
    weights.sort()
    for i in range(n):
        if now< weights[i]:
            break
        now += weights[i]

    return now

n = int(input())
weights = list(map(int, input().split()))
print(solution(weights))