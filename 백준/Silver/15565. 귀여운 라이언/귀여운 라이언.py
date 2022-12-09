# 15565 귀여운 라이언
# silver 1
# 투포인터, 슬라이딩 윈도우

import sys
input = sys.stdin.readline

def solution(n, k, dolls):
    answer = n
    # 투 포인터의 위치
    left, right = 0, 0
    # 라이언 인형의 개수
    count = 0

    if dolls[left] == 1:
        count += 1
    
    # 두 개의 포인터 중 하나가 배열의 끝에 도달할 때 까지 반복
    while left < n and right < n :
        # 왼쪽 그대로, 라이언 개수가 부족할 때 오른쪽 포인터 이동
        if count < k :
            right += 1
            if right < n and dolls[right] == 1:
                count += 1
        # 라이언 개수 충분하면 왼쪽 포인터 옮겨서 가장 작은 집합을 찾는다.
        else:
            # 인형 개수가 딱 맞으면 답이랑 비교해서 최적의 답을 찾는다
            if count == k:
                answer = min(answer, right - left + 1)
            if left < n and dolls[left] == 1:
                count -= 1
            left += 1

    if answer == n :
        answer = -1

    return answer

n, k = map(int, input().split())
dolls = list(map(int, input().split()))
print(solution(n, k, dolls))