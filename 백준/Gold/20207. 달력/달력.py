import sys
input = sys.stdin.readline

scd = []
days = [0] *366

n = int(input())
for _ in range(n):
    s, e = map(int, input().split())
    scd.append([s, e])
    for i in range(s, e+1):
        days[i] += 1

w, h = 0, 0
answer = 0

for day in days:
    if day:
        w += 1
        h = max(h, day)
    else:
        answer += w*h
        w, h = 0, 0
answer += w*h

print(answer)