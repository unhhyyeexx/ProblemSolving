const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);
const board = [];
for (let i = 1; i <= n; i++) {
  board.push(input[i].trim().split(" ").map(Number));
}

const dir = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
];

const visit = Array.from({ length: n }, () => Array(m).fill(0));
const q = [];

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (board[i][j] === 9) {
      visit[i][j] = 1;
      q.push([i, j]);
    }
  }
}

while (q.length > 0) {
  const [i, j] = q.shift();
  for (const [di, dj] of dir) {
    let [dx, dy] = [di, dj];
    let [ni, nj] = [i + di, j + dj];

    while (0 <= ni && n > ni && 0 <= nj && m > nj) {
      visit[ni][nj] = 1;
      if (board[ni][nj] === 9) break;

      if (board[ni][nj] === 3) {
        [dx, dy] = [-dy, -dx];
      } else if (board[ni][nj] === 4) {
        [dx, dy] = [dy, dx];
      } else if (
        (board[ni][nj] === 1 && dx === 0) ||
        (board[ni][nj] === 2 && dy === 0)
      ) {
        break;
      }

      ni += dx;
      nj += dy;
    }
  }
}

let answer = 0;

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (visit[i][j] === 1) {
      answer++;
    }
  }
}

console.log(answer);
