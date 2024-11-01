function solution(maps) {
    let n = maps.length, m = maps[0].length;
    let visit = Array.from(Array(n), ()=>Array(m).fill(0));
    let q = [[0, 0]];
    visit[0][0] = 1;
    let dir = [[0,1], [0,-1], [1,0], [-1,0]];
    
    while (q.length > 0){
        let [x, y] = q.shift();
        for (d of dir) {
            let nx = x+d[0], ny = y+d[1];
            if (0<=nx&&nx<n && 0<=ny&&ny<m && maps[nx][ny] === 1 && visit[nx][ny] === 0){
                if (nx === n-1 && ny === m-1) return visit[x][y] +1;
                visit[nx][ny] = visit[x][y] + 1;
                q.push([nx, ny]);
            }
        }
    }
    return -1;
}