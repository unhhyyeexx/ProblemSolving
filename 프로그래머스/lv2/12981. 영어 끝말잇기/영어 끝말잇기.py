def solution(n, words):
    answer = []

    used = []
    for idx, w in enumerate(words):
        if used and (w in used or used[-1][-1] != w[0]):
            answer = [(idx%n) + 1, (idx//n) + 1]
            return answer
        else:
            used.append(w)
    return [0,0]