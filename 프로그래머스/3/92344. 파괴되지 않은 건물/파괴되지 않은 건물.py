def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    maps = [[0]*(m+1) for _ in range(n+1)]
    for t, r1, c1, r2, c2, d in skill:
        maps[r1][c1] += d * (-1 if t == 1 else 1)
        maps[r1][c2 + 1] += d * (1 if t == 1 else -1)
        maps[r2 + 1][c1] += d * (1 if t == 1 else -1)
        maps[r2 + 1][c2 + 1] += d * (-1 if t == 1 else 1)
    
    for i in range(n):
        for j in range(m):
            maps[i][j+1] += maps[i][j]
    for j in range(m):
        for i in range(n):
            maps[i+1][j] += maps[i][j]
            
    for i in range(n):
        for j in range(m):
            if board[i][j] + maps[i][j] > 0:
                answer += 1
    return answer