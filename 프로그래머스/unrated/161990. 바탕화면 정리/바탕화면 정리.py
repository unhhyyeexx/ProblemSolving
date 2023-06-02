def solution(wallpaper):
    lux, luy, rdx, rdy = 1e9, 1e9, 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                lux = min(lux, i)
                rdx = max(rdx, i+1)
                luy = min(luy, j)
                rdy = max(rdy, j+1)
                
    return [lux, luy, rdx, rdy]