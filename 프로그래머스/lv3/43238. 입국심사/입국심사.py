def solution(n, times):
    left, right = min(times), max(times)*n
    answer = max(times)*n
    
    while left <= right:
        total = 0
        mid = (left + right) // 2
        for time in times:
            total += (mid // time)
        if total < n:
            left = mid + 1
        else:
            right = mid - 1
            answer = min(answer, mid)
            
    return answer