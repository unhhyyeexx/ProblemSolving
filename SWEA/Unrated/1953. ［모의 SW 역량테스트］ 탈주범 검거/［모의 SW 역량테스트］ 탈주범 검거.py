from collections import deque

def solution(n, m, r, c, l, maps):
    visit = [[0]*m for _ in range(n)]
    visit[r][c] = 1
    q = deque([])
    q.append((r,c))
    cnt = 1

    while q:
        i, j = q.popleft()
        if visit[i][j] < l:
            for d in types[maps[i][j]]:
                ni, nj = i+dirs[d][0], j+dirs[d][1]
                if 0<=ni<n and 0<=nj<m and not visit[ni][nj] and ((d+2)%4 in types[maps[ni][nj]]):
                    cnt += 1
                    visit[ni][nj] = visit[i][j] + 1
                    q.append((ni, nj))
    
    return cnt

for tc in range(1, int(input())+1):
    n, m, r, c, l = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    dirs = [[-1,0], [0,1], [1,0], [0,-1]]
    types = [[], [0,1,2,3], [0,2], [1,3], [0,1], [1,2], [2,3], [3,0]]
    print(f'#{tc} {solution(n,m,r,c,l,maps)}')