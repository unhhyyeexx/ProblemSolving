const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m, k] = input[0].trim().split(" ").map(Number);
const order = [[0, 0]];
for (let i = 1; i < n + 1; i++) {
  order.push(input[i].trim().split(" ").map(Number));
}

function solution() {
  const dp = Array.from({ length: n + 1 }, () =>
    Array.from({ length: m + 1 }, () => Array(k + 1).fill(0))
  );

  for (let o = 1; o < order.length; o++) {
    const [nb, nf] = order[o];
    for (let b = 1; b < m + 1; b++) {
      for (let f = 1; f < k + 1; f++) {
        if (nb <= b && nf <= f) {
          dp[o][b][f] = Math.max(
            1+ dp[o - 1][b - nb][f - nf],
            dp[o - 1][b][f]
          );
        } else {
          dp[o][b][f] = dp[o - 1][b][f];
        }
      }
    }
  }
  console.log(dp[n][m][k]);
}

solution();
