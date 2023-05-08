def solution(d, budget):
    answer = 0
    d.sort(reverse = True)
    while d and d[-1] <= budget:
        budget -= d.pop()
        answer += 1

    return answer