import sys
input = sys.stdin.readline

def solution(n, board):
    visit = [[0]*n for _ in range(n)]
    visit[0][0] = 1
    for i in range(n):
        for j in range(n):
            if i == n-1 and j == n-1:
                return visit[n-1][n-1]
            if visit[i][j] > 0:
                dist = board[i][j]
                if 0 <= i+dist < n: 
                    visit[i+dist][j] += visit[i][j]
                if 0 <= j+dist < n:
                    visit[i][j+dist] += visit[i][j]
    return visit[n-1][n-1]

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

print(solution(n, board))