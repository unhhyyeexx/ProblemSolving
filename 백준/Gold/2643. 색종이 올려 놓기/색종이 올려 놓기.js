const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
const arr = [];

for (let i = 1; i <= n; i++) {
  arr.push(
    input[i]
      .trim()
      .split(" ")
      .map(Number)
      .sort((a, b) => a - b)
  );
}

arr.sort((a, b) => a[0] - b[0] || a[1] - b[1]);

const dp = Array(n).fill(1);

for (let i = 1; i < n; i++) {
  for (let j = 0; j < i; j++) {
    if (arr[i][1] >= arr[j][1]) {
      dp[i] = Math.max(dp[i], dp[j] + 1);
    }
  }
}

console.log(Math.max(...dp));
