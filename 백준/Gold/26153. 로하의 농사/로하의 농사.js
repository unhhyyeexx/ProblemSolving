const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);
const board = [];

for (let i = 1; i < n + 1; i++) {
  board.push(input[i].trim().split(" ").map(Number));
}
const [rx, ry, p] = input[n + 1].trim().split(" ").map(Number);

const dir = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];
const visit = Array.from({ length: n }, () => Array(m).fill(0));
let answer = board[rx][ry];

function dfs(si, sj, sum, direction, pipes) {
  if (pipes > p) {
    return;
  }
  answer = Math.max(sum, answer);

  for (let i = 0; i < 4; i++) {
    const [di, dj] = dir[i];
    const ni = si + di;
    const nj = sj + dj;
    if (ni < 0 || nj < 0 || ni >= n || nj >= m || visit[ni][nj] === 1) continue;

    visit[ni][nj] = 1;
    if (direction != -1 && direction != i) {
      if (pipes >= 1) {
        dfs(ni, nj, sum + board[ni][nj], i, pipes + 2);
      }
    } else {
      dfs(ni, nj, sum + board[ni][nj], i, pipes + 1);
    }

    visit[ni][nj] = 0;
  }
}

if (p === 1) {
  console.log(board[rx][ry]);
  process.exit(0);
}

visit[rx][ry] = 1;
dfs(rx, ry, board[rx][ry], -1, 0);
console.log(answer);