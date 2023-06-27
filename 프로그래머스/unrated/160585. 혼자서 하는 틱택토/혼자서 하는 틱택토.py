def solution(board):
    # O와 X의 개수가 같거나 O가 선공이므로 하나 더 많은 경우만 유효하다.
    joinBoard = ''.join(board)
    subVal = joinBoard.count('O') - joinBoard.count('X')
    if subVal not in [0, 1]:
        return 0
    
    # 가로 세로 
    transBoard = list(zip(*board))
    cntO, cntX = 0, 0
    for i in range(3):
        if transBoard[i].count('O') == 3 or board[i].count('O') == 3:
            cntO += 1
        if transBoard[i].count('X') == 3 or board[i].count('X') == 3:
            cntX += 1
    
    # 대각선
    for i in range(0,3,2):
        if (board[0][i] == board[1][1] == board[2][2-i] == 'O'):
            cntO += 1
        if (board[0][i] == board[1][1] == board[2][2-i] == 'X'):
            cntX += 1
            
    if cntO and cntX:
        return 0
    if cntO == 1 and subVal == 0:
        return 0
    if cntX == 1 and subVal >= 1:
        return 0
    
    return 1