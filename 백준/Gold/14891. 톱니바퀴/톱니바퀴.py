import sys
from collections import deque
input = sys.stdin.readline

def solution(w, d):
    r = []
    for i in range(4):
        r.append([wheels[i][6], wheels[i][2]])
    # 왼쪽
    if w != 0:
        for i in range(w, 0, -1):
            if r[i][0] != r[i-1][1]:
                if (w-(i-1))%2 == 0: #같은방향으로 돌리기
                    wheels[i-1].rotate(d)
                else:
                    wheels[i-1].rotate(-1*d)
            else:
                break
    # 오른쪽
    if w != 3:
        for i in range(w, 3):
            if r[i][1] != r[i+1][0]:
                if (w-(i+1))%2 == 0:
                    wheels[i+1].rotate(d)
                else:
                    wheels[i+1].rotate(-1*d)
            else:
                break
    
    wheels[w].rotate(d)

    return


wheels = [deque(list(map(int, input().rstrip()))) for _ in range(4)]
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    solution(a-1, b)
    
answer = 0
for i in range(4):
    if wheels[i][0] == 1:
        answer += 2**i

print(answer)