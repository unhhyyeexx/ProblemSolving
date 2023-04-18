def solution(cards):
    answer = []
    visit = [0]*(len(cards) + 1)
    for c in cards:
        if not visit[c]:
            tmp = []
            while c not in tmp:
                tmp.append(c)
                c = cards[c-1]
                visit[c] = 1
            answer.append(len(tmp))
    if answer[0] == len(cards):
        return 0
    answer.sort(reverse=True)
    return answer[0] * answer[1]