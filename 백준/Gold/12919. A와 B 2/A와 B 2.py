import sys
input = sys.stdin.readline

def solution(string):
    global answer

    if string == s:
        return 1
    if len(string) <= len(s):
        return 0

    if string[-1] == 'A':
        answer = solution(string[:-1])

    if answer == 1:
        return 1

    if string[0] == 'B':
        answer = solution((string[::-1])[:-1])

    return answer

s = input().rstrip()
t = input().rstrip()
answer = 0

print(solution(t))