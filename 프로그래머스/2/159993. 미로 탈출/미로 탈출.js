function bfs(start, end, maps, n, m) {
    const q = []
    q.push(start)
    let head = 0
    const visit = Array.from({ length: n }, () => Array(m).fill(-1));
    visit[start[0]][start[1]] = 0
    const dirs = [[0,1], [1,0], [0,-1], [-1,0]]
    while (q.length > head) {
        const [ci, cj] = q[head]
        const cv = visit[ci][cj]
        for (const [di, dj] of dirs) {
            const ni = ci+di, nj = cj+dj
            if (0<=ni && ni<n && 0<=nj && nj<m) {
                if (ni === end[0] && nj === end[1]) {
                    return cv + 1
                } else if (maps[ni][nj] === "X") {
                    continue
                } else if (visit[ni][nj] === -1) {
                    visit[ni][nj] = cv + 1
                    q.push([ni, nj])
                }
            }
        }
        head++
    }
    
}

function solution(maps) {
    const n = maps.length
    const m = maps[0].length
    let start = [], end = [], lever = []
    for (let i=0; i<n; i++) {
        for (let j=0; j<m; j++) {
            if (maps[i][j] ==='S') {
                start = [i, j]
            } else if (maps[i][j] === 'L') {
                lever = [i, j]
            } else if (maps[i][j] === 'E') {
                end = [i, j]
            }    
            if (start.length>0 && end.length>0 && lever.length>0) break
        }
        if (start.length>0 && end.length>0 && lever.length>0) break
    }
    const stol = bfs(start, lever, maps, n, m)
    const ltoe = bfs(lever, end, maps, n, m)
    
    if (!stol || !ltoe) {
        return -1
    } else {
        return stol + ltoe
    }

}