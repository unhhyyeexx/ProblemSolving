from itertools import combinations, permutations, product

def solution(n, q, ans):
    answer = 0
    q = [set(i) for i in q]
    candidates = [set(i) for i in combinations([i for i in range(1, n+1)], 5)]
    for candidate in candidates:
        for j in range(len(q)):
            target, r = q[j], ans[j]
            if len(target & candidate) != r:
                break
        else:
            answer += 1
            
    return answer