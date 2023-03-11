from collections import Counter, defaultdict

def solution(topping):
    answer = 0
    a = Counter(topping)
    b = defaultdict(int)
    
    for t in topping:
        b[t] += 1
        a[t] -= 1

        if a[t] == 0:
            del a[t]
        if len(b) == len(a):
            answer += 1
    return answer