def solution(grid):
    answer = []
    dir = [[1,0], [0,-1], [-1,0], [0,1]]
    
    n, m = len(grid), len(grid[0])
    visit = [[[0]*4 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            for idx in range(4):
                # 해당 좌표-방향이 기존에 탐색된 경우
                if visit[i][j][idx]:
                    continue
                
                cnt = 0
                ni, nj = i, j
                while not visit[ni][nj][idx]:
                    visit[ni][nj][idx] = 1
                    cnt += 1
                    if grid[ni][nj] == "S":
                        pass
                    elif grid[ni][nj] == "L":
                        idx = (idx-1) % 4
                    elif grid[ni][nj] == "R":
                        idx = (idx+1) % 4
                    
                    ni = (ni + dir[idx][0]) % n
                    nj = (nj + dir[idx][1]) % m
                    
                answer.append(cnt)
    return sorted(answer)