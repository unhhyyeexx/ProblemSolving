import sys
input = sys.stdin.readline

r, c = map(int, input().split())

board = []
for _ in range(r):
    board.append(list(input().rstrip()))

# 알파벳 -> 인덱스 map
map_dict = {}
for i in range(26):
    map_dict[chr(65 + i)] = i

# 방문 배열
visited = [False] * 26


def dfs(i, j):
    dirs = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]

    result = 1

    for di, dj in dirs:
        ni = i + di
        nj = j + dj

        if ni < 0 or ni >= r or nj < 0 or nj >= c:
            continue

        idx = map_dict[board[ni][nj]]

        if visited[idx]:
            continue

        visited[idx] = True
        result = max(result, dfs(ni, nj) + 1)
        visited[idx] = False  # 백트래킹

    return result


def solution():
    start_idx = map_dict[board[0][0]]
    visited[start_idx] = True

    return dfs(0, 0)


print(solution())