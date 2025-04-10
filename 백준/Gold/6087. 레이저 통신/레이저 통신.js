const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [w, h] = input[0].trim().split(" ").map(Number);
const board = input.slice(1, h + 1).map((row) => row.split(""));

const dirs = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];

let points = [];
for (let y = 0; y < h; y++) {
  for (let x = 0; x < w; x++) {
    if (board[y][x] === "C") {
      points.push([y, x]);
    }
  }
}

const [sy, sx] = points[0];
const [ey, ex] = points[1];

// visit[y][x][dir] = 최소 거울 수
const visit = Array.from({ length: h }, () =>
  Array.from({ length: w }, () => Array(4).fill(Infinity))
);

const deque = [];
for (let d = 0; d < 4; d++) {
  const [dy, dx] = dirs[d];
  const ny = sy + dy;
  const nx = sx + dx;
  if (ny >= 0 && ny < h && nx >= 0 && nx < w && board[ny][nx] !== "*") {
    deque.push([ny, nx, d, 0]); // y, x, dir, mirrors
    visit[ny][nx][d] = 0;
  }
}

while (deque.length) {
  const [y, x, dir, mirrors] = deque.shift();

  for (let nd = 0; nd < 4; nd++) {
    const [dy, dx] = dirs[nd];
    const ny = y + dy;
    const nx = x + dx;
    if (ny < 0 || ny >= h || nx < 0 || nx >= w) continue;
    if (board[ny][nx] === "*") continue;

    const newMirrors = dir === nd ? mirrors : mirrors + 1;

    if (visit[ny][nx][nd] > newMirrors) {
      visit[ny][nx][nd] = newMirrors;
      if (dir === nd) {
        deque.unshift([ny, nx, nd, newMirrors]); // 거울 안 씀
      } else {
        deque.push([ny, nx, nd, newMirrors]); // 거울 씀
      }
    }
  }
}

const answer = Math.min(...visit[ey][ex]);
console.log(answer);
