import sys
input = sys.stdin.readline

from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split(" ")))

tails = []

for num in nums:
    pos = bisect_left(tails, num)

    if pos == len(tails):
        tails.append(num)
    else:
        tails[pos] = num

print(len(tails))