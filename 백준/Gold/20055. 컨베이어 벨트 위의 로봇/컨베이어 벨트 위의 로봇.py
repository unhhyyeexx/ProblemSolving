import sys
from collections import deque
input = sys.stdin.readline

def solution(n, k, arr):
    answer = 0
    robot = deque([0]*n)

    while True:
        answer += 1
        arr.rotate(1)
        robot[-1] = 0
        robot.rotate(1)
        robot[-1] = 0 # 내리는 위치

        for i in range(n-2, -1, -1):
            # 이동하려는 칸 내구도 1 이상, 로봇 없음, 현재 칸은 로봇 있으면 이동
            if arr[i+1] >= 1 and robot[i+1] == 0 and robot[i] == 1:
                robot[i+1] = 1
                robot[i] = 0
                arr[i+1] -= 1
        robot[-1] = 0

        if arr[0] != 0 and robot[0] == 0:
            robot[0] = 1
            arr[0] -= 1
        
        if arr.count(0) >= k:
            break
    
    return answer

n, k = map(int, input().split())
arr = deque(map(int, input().split()))
print(solution(n, k, arr))