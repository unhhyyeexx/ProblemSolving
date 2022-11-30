# 2800 괄호 제거
# gold 5
# 자료구조, 문자열, 스택, 재귀

# 반복문으로 괄호의 시작점과 끝점을 순서대로 저장
# 저장된 괄호의 시작점과 끝점을 제거하기 위해 모든 경우의 수를 확인.
# 이때, 괄호의 개수를 늘리면서 확인
# 반복문을 통해 모든 경우의 수의 괄호를 제거하고 저장
# 중복없이 저장된 것을 오름차순으로 정렬하여 출력


import sys
from itertools import combinations
input = sys.stdin.readline

def solution(a):
    # 중복없이 
    answer = set()

    stack = []
    out = []

    # 반복문으로 괄호의 시작점과 끝점을 순서대로 저장
    for i, word in enumerate(a):
        if word == "(":
            stack.append(i)
        elif word == ")":
            out.append((stack.pop(), i))

    for i in range(1, len(out) + 1):
        # 모든 경우의 수
        combis = combinations(out, i)
        # 반복문으로 경우의 수 확인
        for combi in combis:
            tmp = list(a)
            #괄호 제거
            for c in combi:
                tmp[c[0]] = ""
                tmp[c[1]] = ""
            answer.add(''.join(tmp))    

    return sorted(answer)


a = list(input().strip())
for i in solution(a):
    print(i)