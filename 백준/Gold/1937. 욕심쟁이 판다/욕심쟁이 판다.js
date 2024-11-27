const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
const board = [];
for (let i = 1; i < n + 1; i++) {
  board.push(input[i].trim().split(" ").map(Number));
}

const dir = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];

function dfs(i, j, dp) {
  // 방문했던 칸이면 이전 연산값 이용
  if (dp[i][j] > 0) {
    return dp[i][j];
  }

  dp[i][j] = 1; // 방문처리
  for ([di, dj] of dir) {
    const ni = i + di,
      nj = j + dj;
    if (0 <= ni && ni < n && 0 <= nj && nj < n && board[i][j] < board[ni][nj]) {
      // 진행하려는 곳이 범위 안에 있고, 현재보다 대나무가 많으면 진행
      dp[i][j] = Math.max(dp[i][j], dfs(ni, nj, dp) + 1);
    }
  }

  return dp[i][j];
}

function solution() {
  const dp = Array.from({ length: n }, () => Array(n).fill(0));

  // 순서대로 탐색
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      dfs(i, j, dp);
    }
  }

  let answer = 0;
  dp.forEach((el) => {
    answer = Math.max(answer, ...el);
  });

  return answer;
}

console.log(solution());