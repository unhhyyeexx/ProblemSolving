const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);
const board = [];
for (let i = 1; i < n + 1; i++) {
  board.push(input[i].trim().split(" ").map(Number));
}

const blank = [];
for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (board[i][j] === 0) {
      blank.push([i, j]);
    }
  }
}

const dir = [
  [0, 1],
  [0, -1],
  [-1, 0],
  [1, 0],
];

function cnt_ckeck(si, sj) {
  const q = [[si, sj]];
  visit[si][sj] = 1;
  let flag = 1;
  let enemy = 1;

  while (q.length > 0) {
    const [i, j] = q.shift();
    for (const [di, dj] of dir) {
      const ni = i + di;
      const nj = j + dj;
      if (ni < 0 || nj < 0 || ni >= n || nj >= m || visit[ni][nj] === 1)
        continue;

      if (board[ni][nj] === 0) {
        flag = 0;
        continue;
      } else if (board[ni][nj] === 1) {
        continue;
      } else {
        q.push([ni, nj]);
        visit[ni][nj] = 1;
        enemy += 1;
      }
    }
  }
  if (flag === 1) {
    return enemy;
  } else {
    return 0;
  }
}

function getCombination(n, r) {
  const res = [];
  if (r === 1) return n.map((value) => [value]);

  n.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    const combinations = getCombination(rest, r - 1);
    const attached = combinations.map((combination) => [fixed, ...combination]);
    res.push(...attached);
  });

  return res;
}

let answer = 0;
for (const [b1, b2] of getCombination(blank, 2)) {
  let cnt = 0;
  visit = Array.from({ length: n }, () => Array(m).fill(0));
  board[b1[0]][b1[1]] = 1;
  board[b2[0]][b2[1]] = 1;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (board[i][j] === 2 && visit[i][j] === 0) {
        cnt += cnt_ckeck(i, j);
      }
    }
  }

  board[b1[0]][b1[1]] = 0;
  board[b2[0]][b2[1]] = 0;

  answer = Math.max(answer, cnt);
}

console.log(answer);