const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
const board = [];
for (let i = 1; i < n + 1; i++) {
  board.push(input[i].trim().split(" "));
}

function solution() {
  let maxV = -(5 ** 20);
  let minV = 5 ** 20;

  const dir = [
    [0, 1],
    [1, 0],
  ];

  function dfs(i, j, v) {
    if (i === n - 1 && j === n - 1) {
      // 끝까지 왔으면 정답 갱신
      maxV = Math.max(maxV, v);
      minV = Math.min(minV, v);
    }

    for ([di, dj] of dir) {
      const ni = i + di;
      const nj = j + dj;

      if (ni >= n || nj >= n) {
        continue;
      }

      if (!isNaN(board[i][j])) {
        // 숫자이면
        dfs(ni, nj, v);
      } else {
        dfs(ni, nj, eval(v + board[i][j] + board[ni][nj]).toString());
      }
    }
  }

  dfs(0, 0, board[0][0]);

  console.log(maxV, minV);
}

solution();