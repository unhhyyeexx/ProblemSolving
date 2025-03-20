const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
const costs = [];
for (let i = 1; i < n + 1; i++) {
  costs.push(input[i].trim().split(" ").map(Number));
}

let answer = Infinity;
for (let i = 0; i < 3; i++) {
  const dp = Array.from({ length: n }, () => Array(3).fill(Infinity));
  dp[0][i] = costs[0][i];

  for (let j = 1; j < n; j++) {
    dp[j][0] = costs[j][0] + Math.min(dp[j - 1][1], dp[j - 1][2]);
    dp[j][1] = costs[j][1] + Math.min(dp[j - 1][2], dp[j - 1][0]);
    dp[j][2] = costs[j][2] + Math.min(dp[j - 1][0], dp[j - 1][1]);
  }

  for (let j = 0; j < 3; j++) {
    if (i != j) {
      answer = Math.min(answer, dp[n - 1][j]);
    }
  }
}

console.log(answer);