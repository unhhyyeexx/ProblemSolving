import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split(" "))
belt = list(map(int, input().split(" ")))
robots = [False] * (n)
step = 0

while True:
    step += 1

    # 1. 회전
    belt = [belt[-1]] + belt[:-1]
    robots = [False] + robots[:-1]
    robots[-1] = False # 내리기

    # 2. 로봇 이동
    for i in range(n-2, -1, -1):
        if robots[i] and not robots[i+1] and belt[i+1] > 0:
            robots[i] = False
            robots[i+1] = True
            belt[i+1] -= 1
    
    robots[-1] = False # 내리기

    # 3. 로봇 올리기
    if belt[0] > 0:
        robots[0] = True
        belt[0] -= 1
    
    # 4. 종료
    if belt.count(0) >= k:
        break

print(step)