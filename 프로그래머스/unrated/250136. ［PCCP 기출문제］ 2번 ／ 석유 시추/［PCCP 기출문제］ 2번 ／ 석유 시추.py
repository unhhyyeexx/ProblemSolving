from collections import deque
from collections import defaultdict

def solution(land):
    n, m = len(land), len(land[0])
    answer = 0
    
    dir = [[1,0], [-1,0], [0,1], [0,-1]]
    
    dic = defaultdict(int)
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                land[i][j] = -1
                cnt = 1
                col = {j}
                q = deque([(i, j)])
                
                while q:
                    x, y = q.popleft()
                    
                    for di, dj in dir:
                        ni, nj = x+di, y+dj
                        if 0<=ni<n and 0<=nj<m and land[ni][nj] == 1:
                            q.append((ni, nj))
                            cnt += 1
                            land[ni][nj] = -1
                            col.add(nj)
                
                for c in list(col):
                    dic[c] += cnt
    
    answer = dic[max(dic, key=dic.get)]
                            
                
    return answer