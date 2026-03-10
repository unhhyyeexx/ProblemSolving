import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]

array.sort()

answer = float("inf")
start = 0
end = 1

while start<=end<n:
    if start == end:
        end += 1
    elif array[end] - array[start] >= m:
        answer = min(array[end]-array[start], answer)
        if answer == m:
            break
        start += 1
    else:
        end += 1

print(answer)