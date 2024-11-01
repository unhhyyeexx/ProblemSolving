function solution(rectangle, characterX, characterY, itemX, itemY) {
    var answer = 0;
    let board = Array.from(Array(102), ()=>Array(102).fill(-1));
    rectangle.forEach((el, i)=> {
        el.forEach((e, j)=> rectangle[i][j] = e*2);
    });
    
    rectangle.forEach((el) => {
        let x1 = el[0], y1 = el[1], x2 = el[2], y2 = el[3];
        for(let x=x1; x<=x2; x++){
            for(let y=y1; y<=y2; y++){
                if (x1<x&&x<x2 && y1<y&&y<y2) board[x][y] = 0;
                else if (board[x][y] === -1) board[x][y] = 1;
            }
        }
    });
    
    let q = [[characterX*2, characterY*2]];
    let visit = Array.from(Array(102), ()=>Array(102).fill(0));
    visit[characterX*2][characterY*2] = 1;
    let dir = [[0,1], [0,-1], [1,0], [-1,0]];
    while (q.length > 0) {
        let now = q.shift();
        let x = now[0], y = now[1];
        if (x === itemX*2 && y === itemY*2){
            answer = (visit[x][y] - 1) / 2;
            break;
        }
        for (d of dir){
            let nx = x+d[0], ny = y+d[1];
            if (visit[nx][ny] === 0 && board[nx][ny] === 1) {
                q.push([nx, ny]);
                visit[nx][ny] = visit[x][y] + 1;
            }
        }
    }
    
    
    return answer;
}