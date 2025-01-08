const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);
const before = [];
const after = [];
for (let i = 1; i <= n; i++) {
  before.push(input[i].trim().split(" ").map(Number));
}
for (let i = 1 + n; i <= n + n; i++) {
  after.push(input[i].trim().split(" ").map(Number));
}

const dir = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];

const visit = Array.from({ length: n }, () => Array(m).fill(0));

function bfs(si, sj) {
  const beforeData = before[si][sj];
  const afterData = after[si][sj];

  const q = [];
  q.push([si, sj]);
  visit[si][sj] = true;
  before[si][sj] = afterData;

  while (q.length > 0) {
    const [i, j] = q.shift();
    for ([di, dj] of dir) {
      const ni = i + di;
      const nj = j + dj;
      // 못가는 칸, 이미 갔던칸이면 넘어가기
      if (
        ni < 0 ||
        nj < 0 ||
        ni >= n ||
        nj >= m ||
        before[ni][nj] !== beforeData ||
        visit[ni][nj]
      )
        continue;

      if (after[ni][nj] !== afterData) {
        return false;
      }

      q.push([ni, nj]);
      visit[ni][nj] = true;
      before[ni][nj] = afterData;
    }
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (before[i][j] !== after[i][j]) return false;
    }
  }

  return true;
}

function solution() {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (before[i][j] !== after[i][j]) {
        if (bfs(i, j)) {
          console.log("YES");
          return;
        } else {
          console.log("NO");
          return;
        }
      }
    }
  }
  console.log("YES");
}

solution();