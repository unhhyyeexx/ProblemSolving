const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [r, c, t] = input[0].trim().split(" ").map(Number);
const board = [];
let gi = 0,
  gj = 0;
for (let i = 1; i < r + 1; i++) {
  let tmp = input[i].trim().split("");
  for (let j = 0; j < c; j++) {
    if (tmp[j] === "G") {
      gi = i - 1;
      gj = j;
    }
  }
  board.push(tmp);
}

const dir = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];

function solution() {
  let answer = 0;

  function dfs(i, j, time, cnt) {
    // [i,j] 현재위치 time 지금까지 걸린시간 cnt 먹은 고구마 개수
    if (time === t) {
      answer = Math.max(answer, cnt);
      return;
    }

    for ([di, dj] of dir) {
      let ni = i + di;
      let nj = j + dj;
      if (0 <= ni && ni < r && 0 <= nj && nj < c && board[ni][nj] !== "#") {
        if (board[ni][nj] === "S") {
          // 이동한 곳에 고구마 있으면 먹은 표시로 .으로 바꾸고 진행
          board[ni][nj] = ".";
          dfs(ni, nj, time + 1, cnt + 1);
          board[ni][nj] = "S"; // 돌아와서 다시 S로 되돌려 놓음 (백트래킹)
        } else {
          dfs(ni, nj, time + 1, cnt);
        }
      }
    }

    return;
  }

  dfs(gi, gj, 0, 0);

  return answer;
}

console.log(solution());
