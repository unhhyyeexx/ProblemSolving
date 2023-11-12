# greedy
# ex2) 1 1 1 1 1 1 1 1 1 1 1 1 1 / n=13 / k=2
# 2,2,2,2,2,2,1 => 4,4,4,1 => 8,4,1
# +1 => 8,4,1,1 => 8,4,2
# +1 => 8,4,2,1
# +1 => 8,4,2,1,1 => 8,4,2,2 => 8,4,4 => 8,8 => 16 < 2
# 2의 제곱승 숫자만 합칠 수 있음(2진수에서 1의 개수)
# 2진수로 바꿔서 1의 개수가 k보다 크거나 같을 때까지 상점에서 물 사면 됨
import sys
input = sys.stdin.readline

def solution(n, k):
    cnt = 0
    while bin(n).count('1') > k:
        n += 1
        cnt += 1
    return cnt

n, k = map(int, input().split())
print(solution(n, k))