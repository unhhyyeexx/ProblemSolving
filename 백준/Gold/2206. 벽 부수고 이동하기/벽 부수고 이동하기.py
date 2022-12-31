from collections import deque

dir = [[0,1],[0,-1],[1,0],[-1,0]]
def solution(i, j, state):
    visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visit[0][0][0] = 1

    q = deque([[i, j, state]])

    while q:
        i, j, state = q.popleft()
        if i == n-1 and j == m-1:
            return visit[i][j][state]
        for d in dir:
            ni, nj = i+d[0], j+d[1]
            if ni<0 or nj<0 or ni>=n or nj>=m:
                continue
            if maps[ni][nj] == 1 and state == 0:
                visit[ni][nj][1] = visit[i][j][state] + 1
                q.append([ni, nj, 1])
            elif maps[ni][nj] == 0 and visit[ni][nj][state] == 0:
                visit[ni][nj][state] = visit[i][j][state] + 1
                q.append([ni,nj,state])
    return -1


n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]
print(solution(0,0,0))