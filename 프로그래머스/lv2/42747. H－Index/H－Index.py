def solution(citations):
    answer = len(citations)
    citations.sort(reverse=True)
    for idx, c in enumerate(citations):
        if c <= idx:
            answer = idx
            return answer
    return answer