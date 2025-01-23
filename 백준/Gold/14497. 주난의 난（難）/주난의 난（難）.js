const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);
const [x1, y1, x2, y2] = input[1]
  .trim()
  .split(" ")
  .map(Number)
  .map((el) => el - 1);
const board = [];
for (let i = 2; i < 2 + n; i++) {
  board.push(input[i].trim().split(""));
}

const dir = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];

const visit = Array.from({ length: n }, () => Array(m).fill(Infinity));
visit[x1][y1] = 0;

q = [];
q.push([0, x1, y1]);
while (q.length > 0) {
  const [now, x, y] = q.shift();
  if (visit[x][y] < now) continue;

  for (const [di, dj] of dir) {
    const nx = x + di;
    const ny = y + dj;
    if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;

    const next = now + (board[nx][ny] != "0" ? 1 : 0);
    if (next < visit[nx][ny]) {
      q.push([next, nx, ny]);
      visit[nx][ny] = next;
    }
  }
}

console.log(visit[x2][y2]);