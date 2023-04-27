from collections import defaultdict
def solution(clothes):
    answer = 1
    kind = defaultdict(int)
    for cloth in clothes:
        kind[cloth[1]] += 1
    for value in kind.values():
        answer *= (value +1)
    return answer - 1