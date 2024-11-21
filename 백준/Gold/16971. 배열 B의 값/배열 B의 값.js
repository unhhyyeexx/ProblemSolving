const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 1 2 2 2 1
// 2 4 4 4 2
// 2 4 4 4 2
// 1 2 2 2 1

const [n, m] = input[0].split(" ").map(Number);
const board = [];

for (let i = 1; i < n + 1; i++) {
  board.push(input[i].trim().split(" ").map(Number));
}

function solution() {
  const rowSum = Array.from({ length: n }, () => 0);
  const colSum = Array.from({ length: m }, () => 0);

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (i === 0 || i === n - 1) {
        colSum[j] += board[i][j];
      } else {
        colSum[j] += board[i][j] * 2;
      }
      if (j === 0 || j === m - 1) {
        rowSum[i] += board[i][j];
      } else {
        rowSum[i] += board[i][j] * 2;
      }
    }
  }

  let origin = 0;
  rowSum.forEach((el, i) => {
    if (i === 0 || i === n - 1) origin += el;
    else origin += el * 2;
  });
  let answer = origin;

  let minV = Math.min(...rowSum.slice(1, n - 1));
  let maxV = Math.max(rowSum[0], rowSum[n - 1]);
  if (answer < origin - minV + maxV) {
    answer = origin - minV + maxV;
  }

  minV = Math.min(...colSum.slice(1, m - 1));
  maxV = Math.max(colSum[0], colSum[m - 1]);
  if (answer < origin - minV + maxV) {
    answer = origin - minV + maxV;
  }

  console.log(answer);
}

solution();