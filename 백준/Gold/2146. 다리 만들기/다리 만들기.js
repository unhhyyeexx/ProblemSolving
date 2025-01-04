const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
const board = [];
for (let i = 1; i <= n; i++) {
  const tmp = input[i].trim().split(" ").map(Number);
  board.push(tmp);
}

function solution() {
  const dir = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  const visit = Array.from({ length: n }, () => Array(n).fill(0));
  let island = 1;

  function bfs(si, sj) {
    const q = [[si, sj]];
    board[si][sj] = island;
    visit[si][sj] = 1;
    while (q.length > 0) {
      const [i, j] = q.shift();
      for ([di, dj] of dir) {
        const ni = i + di;
        const nj = j + dj;
        if (ni < 0 || nj < 0 || ni >= n || nj >= n || visit[ni][nj] != 0)
          continue;

        if (board[ni][nj] === 1) {
          board[ni][nj] = island;
          visit[ni][nj] = 1;
          q.push([ni, nj]);
        }
      }
    }
    island++;
  }

  for (let k = 0; k < n; k++) {
    for (let l = 0; l < n; l++) {
      if (board[k][l] === 1 && visit[k][l] === 0) {
        bfs(k, l);
      }
    }
  }
  let answer = Infinity;

  function connect(now) {
    const q = [];
    const visit2 = Array.from({ length: n }, () => Array(n).fill(-1));

    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (board[i][j] === now) {
          q.push([i, j]);
          visit2[i][j] = 0;
        }
      }
    }

    while (q.length > 0) {
      const [i, j] = q.shift();
      for (const [di, dj] of dir) {
        const ni = i + di;
        const nj = j + dj;
        if (ni < 0 || nj < 0 || ni >= n || nj >= n) continue;

        if (board[ni][nj] > 0 && board[ni][nj] !== now) {
          answer = Math.min(answer, visit2[i][j]);
          return;
        }

        if (board[ni][nj] === 0 && visit2[ni][nj] === -1) {
          visit2[ni][nj] = visit2[i][j] + 1;
          q.push([ni, nj]);
        }
      }
    }
  }

  for (let i = 1; i < island; i++) {
    connect(i);
  }

  console.log(answer);
}

solution();
