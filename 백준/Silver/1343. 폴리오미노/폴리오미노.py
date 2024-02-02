import sys
input = sys.stdin.readline

def solution(board):
    answer = ''
    n = len(board)

    cnt = 0
    for i in range(n):
        if board[i] == '.':
            if cnt > 0 and cnt%2 == 0:
                answer += 'AAAA' * (cnt//4)
                cnt %= 4
                answer += 'BB' * (cnt//2)
                cnt = 0
            elif cnt > 0 and cnt%2 != 0:
                return -1
            
            answer += '.'
            
        else:
            cnt += 1
    if cnt > 0:
        if cnt % 2 != 0:
                return -1
        answer += 'AAAA' * (cnt//4)
        cnt %= 4
        answer += 'BB' * (cnt//2)
        cnt = 0
    return answer

board = list(input().strip())
print(solution(board))