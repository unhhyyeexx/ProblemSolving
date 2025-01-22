const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m, k] = input[0].trim().split(" ").map(Number);
const board = [];
for (let i = 1; i <= n; i++) {
  board.push(input[i].trim());
}

function minimal(color) {
  const prefix = Array.from({ length: n + 1 }, () => Array(m + 1).fill(0));

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      const value =
        (i + j) % 2 === 0 ? board[i][j] !== color : board[i][j] === color;
      prefix[i + 1][j + 1] =
        prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + (value ? 1 : 0);
    }
  }

  let count = Infinity;
  for (let i = 1; i <= n - k + 1; i++) {
    for (let j = 1; j <= m - k + 1; j++) {
      count = Math.min(
        count,
        prefix[i + k - 1][j + k - 1] -
          prefix[i + k - 1][j - 1] -
          prefix[i - 1][j + k - 1] +
          prefix[i - 1][j - 1]
      );
    }
  }

  return count;
}

console.log(Math.min(minimal("B"), minimal("W")));