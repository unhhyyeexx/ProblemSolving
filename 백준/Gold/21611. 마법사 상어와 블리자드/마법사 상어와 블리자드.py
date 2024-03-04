# boj 21611 마법사 상어와 블리자드 gold1 implementation

def magic(d, s):
    global board
    result = {1:0, 2:0, 3:0}

    # 얼음파편 던지기
    for i in range(1, s+1):
        ni, nj = int(si + dir[d-1][0]*i), int(sj + dir[d-1][1]*i)
        board[ni][nj] = -1
    
    # 파괴된 빈칸 채우기
    nboard = [[0]*n for _ in range(n)]
    live = []
    for ri, rj in road:
        if board[ri][rj] > 0:
            live.append(board[ri][rj])
        elif board[ri][rj] == 0:
            break
    
    # 채우기 전에 한줄정렬 되어있으니 폭발도 시키자,,!
    flag = 1
    while flag:
        now = 0
        ncnt = 0
        nlive = []
        flag = 0
        for l in live:
            if l == now:
                ncnt += 1
            else:
                if ncnt >= 4: # 폭발
                    result[now] += ncnt
                    flag = 1
                else:
                    for _ in range(ncnt):
                        nlive.append(now)
                ncnt = 1
                now = l
        if ncnt >= 4:
            result[now] += ncnt
        else:
            for _ in range(ncnt):
                nlive.append(now)       
        if flag:
            live = nlive
    
    # 구슬 변화
    nlive = []
    now, ncnt = 0, 0
    for l in live:
        if l == now:
            ncnt += 1
        else:
            nlive.append(ncnt)
            nlive.append(now)
            ncnt, now = 1, l
    nlive.append(ncnt)
    nlive.append(now)

    live = nlive[2 : 2+n*n-1]

    for li in range(len(live)):
        nboard[road[li][0]][road[li][1]] = live[li] 
    board = nboard

    return result


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
magic_ds = [list(map(int, input().split())) for _ in range(m)]
si, sj = [int((n+1)/2 -1), int((n+1)/2 -1)]
dir = [[-1,0], [1,0], [0,-1], [0,1]]
map_dir = [[0,-1], [1,0], [0,1], [-1,0]]

# 구슬 이동 좌표
# 상어에서 바깥쪽으로
road = []
cnt, end, d = 0, 1, 0
i, j = si, sj
while end:
    cnt += 1
    for _ in range(2):
        if not end:
            break
        for _ in range(cnt):
            i, j = i+map_dir[d][0], j+map_dir[d][1]
            if 0<=i<n and 0<=j<n:
                road.append([i, j])
            else:
                end = 0
                break
        d  = (d+1)%4

answer = {1:0, 2:0, 3:0}
for d, s in magic_ds:
    tmp = magic(d, s)
    answer[1] += tmp[1]
    answer[2] += tmp[2]
    answer[3] += tmp[3]

print(answer[1] + answer[2]*2 + answer[3]*3)