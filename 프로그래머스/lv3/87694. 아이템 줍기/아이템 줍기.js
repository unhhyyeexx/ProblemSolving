function solution(rectangle, characterX, characterY, itemX, itemY) {
    var answer = 0;
    var max = 102;
    var maps = Array.from(Array(max), ()=> new Array(max).fill(-1));
    
    for (rec of rectangle) {
        var x1 = rec[0]*2, y1 = rec[1]*2, x2 = rec[2]*2, y2 = rec[3]*2;
        for (let i=x1; i<=x2; i++) {
            for (let j=y1; j<=y2; j++){
                if (i>x1 && i<x2 && j>y1 && j<y2) { // 내부일 때
                    maps[i][j] = 0;
                } else if (maps[i][j] !== 0) { // 내부가 아닐 때 (테두리일때)
                    maps[i][j] = 1;
                }
            }
        }
    }
    
    var q = [];
    q.push([characterX*2, characterY*2]);
    var visit = Array.from(Array(max), ()=> new Array(max).fill(0));
    visit[characterX*2][characterY*2] = true;
    
    var dir = [[0,1], [0,-1], [1,0], [-1,0]];
    while (q.length > 0) {
        var now = q.shift();
        var x = now[0], y = now[1];
        if (x === itemX*2 && y == itemY*2) {
            answer = (visit[x][y] - 1) / 2;
            break;
        }
        for (d of dir) {
            var nx = x + d[0], ny = y + d[1];
            if (visit[nx][ny] === 0 && maps[nx][ny] === 1){
                q.push([nx, ny]);
                visit[nx][ny] = visit[x][y] + 1;
            }
        }    
    }     
    return answer;
}