def solution(stones, k):
    answer = 0
    # 최소로 건너는 횟수는 1회, 최대는 돌 숫자의 최대값
    left, right = 1, max(stones)
    # stones의 원소에 mid를 뺐을 때 0이 나오는 횟수
    cnt = 0
    while left <= right:
        cnt = 0
        # mid : 건너는 친구들의 수
        mid = (left + right) // 2
        for s in stones:
            # 0이 나오면 cnt 증가해서 0의 개수 파악
            if (s - mid) <= 0:
                cnt += 1
            # 0이 연속적으로 나오지 않으면 초기화
            else:
                cnt = 0
            if cnt >= k:
                answer = mid
                right = mid - 1
                break
        # 연속된 0의 개수가 주어진 k보다 적다면 현재 친구 수보다 많은 수의 친구들이 건널 수 있음
        if cnt < k:
            left = mid + 1
    return answer