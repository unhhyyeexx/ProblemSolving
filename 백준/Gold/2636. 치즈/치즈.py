from collections import deque

#한번 바깥쪽 치즈 삭제될 때 마다 삭제되는 치즈개수
cheesecnt = []

def bfs(N, M, path):
    queue = deque()
    queue.append([0,0])
    visit[0][0] = 1
    dir = [[0,1], [0,-1], [1,0], [-1,0]]
    cnt = 0
    while queue:
        now = queue.popleft()
        for d in dir:
            # 빈칸(치즈없는 칸) 탐색
            nx, ny = now[0] + d[0], now[1] + d[1]
            if 0<=nx<M and 0<=ny<N and visit[ny][nx]==0:
                #치즈가 없으면 queue에 추가해서 탐색할 준비
                if path[ny][nx] == 0:
                    visit[ny][nx] = 1
                    queue.append([nx, ny])
                #치즈가 있으면 치즈있던 칸 0으로 바꿔서 치즈 삭제
                #queue에 추가하지는 않는다. 추가하면 안쪽치즈(?)도 녹는다.
                elif path[ny][nx] == 1:
                    path[ny][nx] = 0
                    visit[ny][nx] = 1
                    cnt += 1
    cheesecnt.append(cnt)
    return cnt

height, width = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(height)]

time = -1
while True:
    visit = [[0] * width for _ in range(height)]
    time += 1
    num  = bfs(height, width, maps)
    if num == 0:
        break

print(time)
print(cheesecnt[-2])