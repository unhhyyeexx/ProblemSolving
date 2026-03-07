import sys
input = sys.stdin.readline

r, c = map(int, input().split(" "))
board = []
for _ in range(r):
    board.append(list(map(str, input().rstrip())))

def dfs(i, j, visited, r, c, board):
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]

    result = 1

    for di, dj in dirs:
        ni, nj = i+di, j+dj

        if not (0<=ni<r and 0<=nj<c):
            continue

        alpha = ord(board[ni][nj]) - ord('A')
        if visited & (1 << alpha):
            continue
        
        result = max(
            result,
            1+ dfs(ni, nj, visited | (1<<alpha), r, c, board)
        )

    return result


def solution(r, c, board) :
   start = ord(board[0][0]) - ord('A')
   visited = 1<<start
   return dfs(0, 0, visited, r, c, board)

print(solution(r, c, board))
