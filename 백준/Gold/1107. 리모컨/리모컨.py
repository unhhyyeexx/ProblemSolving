import sys
input = sys.stdin.readline

def solution(goal, now, broken):
    answer = abs(goal - now)

    # 1000000 => goal 전 후로 500000만큼 움직여봐야됨;;
    # 찐 어쩔완탐
    for nums in range(500000*2 + 1):
        nums = str(nums)
        for i in range(len(nums)):
            # for문 돌면서 고장난 버튼 있으면 쿨하게 넘김
            if nums[i] in broken:
                break
            # 현재 숫자 중에 고장난 버튼 없어서 다 누를 수 있으면
            # 그 숫자 개수 + (+)(-)버튼 몇개 눌러서 goal에 가는지 더해준다.
            elif i + 1 == len(nums):
                answer = min(answer, abs(int(nums) - goal) + len(nums))
    return answer

n = int(input())
m = int(input())
b = list(input().split())
now = 100

print(solution(n, now, b))