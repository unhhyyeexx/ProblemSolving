const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);
const farm = [];
for (let i = 1; i < n + 1; i++) {
  farm.push(input[i].trim().split(" ").map(Number));
}

function solution() {
  const dir = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
    [1, 1],
    [-1, 1],
    [1, -1],
    [-1, -1],
  ];
  const visit = Array.from({ length: n }, () => Array(m).fill(0));

  let answer = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (visit[i][j] === 1) continue;

      const q = [[i, j]];
      let flag = true;

      while (q.length > 0) {
        const [r, c] = q.shift();
        visit[r][c] = 1;

        for ([di, dj] of dir) {
          const ni = r + di;
          const nj = c + dj;

          if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;

          if (farm[r][c] === farm[ni][nj] && visit[ni][nj] === 0) {
            q.push([ni, nj]);
          } else if (farm[r][c] < farm[ni][nj]) {
            flag = false;
          }
        }
      }
      if (flag) {
        answer += 1;
      }
    }
  }
  console.log(answer);
}

solution();