from collections import deque
import sys
input = sys.stdin.readline


def solution(a, b):
    visit = [False] * 10000
    q = deque()
    q.append([a, ''])

    while q:
        now, path = q.popleft()
        visit[now] = True
        if now == b:
            print(path)
            break
        # D
        nd = (now*2)%10000
        if not visit[nd]:
            visit[nd] = True
            q.append([nd, path+'D'])
        # S
        ns = (now-1)%10000
        if not visit[ns]:
            visit[ns] = True
            q.append([ns, path+'S'])
        # L
        nl = (10*now + (now//1000)) % 10000
        if not visit[nl]:
            visit[nl] = True
            q.append([nl, path+'L'])
        # R
        nr = (now//10 + (now%10) * 1000 ) % 10000
        if not visit[nr]:
            visit[nr] = True
            q.append([nr,  path+'R'])


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    answer = solution(a, b)