def solution(n, s):
    answer = [-1]
    if n > s :
        return answer
    init = s // n
    answer = [init for _ in range(n)]
    idx = n - 1
    for _ in range(s % n):
        answer[idx] += 1
        idx -= 1
    return answer