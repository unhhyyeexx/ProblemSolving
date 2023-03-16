function solution(maps) {
    var n = maps.length, m = maps[0].length;
    var visit = maps;
    visit[0][0] = 0;
    var q = [];
    q.push([0,0,1]);
    
    var dir = [[0,1], [0,-1], [1,0], [-1,0]];
    while (q.length > 0){
        var now = q.shift();
        var i = now[0], j = now[1], cnt = now[2];
        for (d of dir) {
            var ni = i+d[0], nj = j+d[1]
            if (0<=ni && ni<n && 0<=nj && nj<m && visit[ni][nj] === 1) {        
                if (ni === n-1 && nj === m-1) {
                    return cnt+1;
            }
                q.push([ni, nj, cnt+1]);
                visit[ni][nj] = 0
            }
        }
    }
    
    return -1;
}