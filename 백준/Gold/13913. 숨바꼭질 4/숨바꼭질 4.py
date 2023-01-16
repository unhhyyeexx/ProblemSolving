from collections import deque

def solution(n, k):
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        if now == k:
            path = []
            tmp = now
            for _ in range(dist[now] + 1):
                path.append(tmp)
                tmp = move[tmp]
            print(dist[now])
            print(' '.join(map(str, path[::-1])))
            return
        dir = [now-1, now+1, now*2]
        for d in dir:
            if 0<=d<=100000 and dist[d] == 0:
                q.append(d)
                q.append(d)
                dist[d] = dist[now] + 1
                move[d] = now


    return

n, k = map(int, input().split())
dist = [0] * 100001
move = [0] * 100001
answer = solution(n, k)