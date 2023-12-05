def solution(board, h, w):
    answer = 0
    n, m = len(board), len(board[0])
    
    dir = [(0,1), (0,-1), (1,0), (-1,0)]
    now = board[h][w]
    
    for dx, dy in dir:
        if 0<=h+dx<n and 0<=w+dy<m and board[h+dx][w+dy] == now:
            answer += 1
            
    return answer