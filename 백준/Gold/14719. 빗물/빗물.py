# 14719 빗물
# gold 5
# 구현, 시뮬레이션

# 현 위치를 기준으로 양쪽에 현 블록보다 높은 블록들이 있으면 물이 고인다
# 첫칸, 막칸은 물이 고일 수 없다
import sys
input = sys.stdin.readline

def solution(h, w, wall):
    answer = 0
    for i in range(1, w-1):
        # 물이 고이는 높이는 양옆 가장 높은 벽들 중 작은 값
        able = min (max(wall[:i]), max(wall[i+1:]))

        # 현재 벽 높이가 able보다 작으면 물이 고일 수 있다.
        # 물이 고이는 양은 물의 높이 - 현재 블럭 높이
        if wall[i] < able:
            answer += able - wall[i]

    return answer

h, w = map(int, input().split())
wall = list(map(int, input().split()))
print(solution(h,w,wall))