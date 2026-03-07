const fs = require("fs");

const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split("\n");

const [r, c] = input[0].split(" ").map(Number);

const board = [];
for (let i = 1; i <= r; i++) {
  board.push(input[i].split(""));
}

// 알파벳 -> 인덱스 map
const map = {};
for (let i = 0; i < 26; i++) {
  map[String.fromCharCode(65 + i)] = i;
}

// 방문 배열
const visited = new Array(26).fill(false);

function dfs(i, j) {
  const dirs = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  let result = 1;

  for (const [di, dj] of dirs) {
    const ni = i + di;
    const nj = j + dj;

    if (ni < 0 || ni >= r || nj < 0 || nj >= c) continue;

    const idx = map[board[ni][nj]];

    if (visited[idx]) continue;

    visited[idx] = true;
    result = Math.max(result, dfs(ni, nj) + 1);
    visited[idx] = false; // 백트래킹
  }

  return result;
}

function solution() {
  const startIdx = map[board[0][0]];
  visited[startIdx] = true;

  return dfs(0, 0);
}

console.log(solution());