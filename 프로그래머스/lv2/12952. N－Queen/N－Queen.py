def dfs(queen, r, n):
    count = 0
    if n == r:
        return 1
    
    for c in range(n):
        queen[r] = c
        for i in range(r):
            # 세로
            if queen[i] == queen[r]:
                break
            # 대각선
            if abs(queen[i] - queen[r]) == (r-i):
                break
        else:
            count += dfs(queen, r+1, n)
    return count

def solution(n):
    queen = [0] * n
    
    return dfs(queen, 0, n)