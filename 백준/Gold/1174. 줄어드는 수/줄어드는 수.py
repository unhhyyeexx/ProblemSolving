from itertools import combinations

def solution(n):
    if n >= 1024:
        return -1
    decrease = []
    for i in range(1, 11):
        for c in combinations(range(0, 10), i):
            c = list(c)
            c.sort(reverse=True)
            decrease.append(int("".join(map(str, c))))
    decrease.sort()
    return decrease[n-1]

N = int(input())
print(solution(N))