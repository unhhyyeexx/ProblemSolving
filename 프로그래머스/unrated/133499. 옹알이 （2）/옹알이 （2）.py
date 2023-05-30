def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    for ba in babbling:
        for word in words:
            if word*2 not in ba:
                ba = ba.replace(word, ' ')
        if ba.isspace():
            answer += 1

    return answer