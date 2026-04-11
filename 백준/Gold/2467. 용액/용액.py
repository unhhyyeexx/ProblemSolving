import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(" ")))
arr.sort()

left = 0
right = n-1
total = 2000000001
answer = [arr[left], arr[right]]

while left < right :
    tmp = arr[left]+arr[right]
    if abs(tmp) < abs(total):
        total = abs(tmp)
        answer = [arr[left], arr[right]]
        if total == 0:
            break
    
    if tmp < 0:
        left += 1
    else:
        right -= 1

print(*answer)