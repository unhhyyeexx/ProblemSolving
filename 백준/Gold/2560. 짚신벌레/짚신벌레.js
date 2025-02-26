const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [a, b, d, n] = input[0].trim().split(" ").map(Number);

const dp = Array(n + 1).fill(0);
for (let i = 0; i < a; i++) {
  dp[i] = 1;
}

for (let i = a; i < n + 1; i++) {
  dp[i] = (dp[i - 1] + dp[i - a] + 1000) % 1000;
  if (i >= b) {
    dp[i] = (dp[i] - dp[i - b] + 1000) % 1000;
  }
}

if (n >= d) {
  console.log((dp[n] - dp[n - d] + 1000) % 1000);
} else {
  console.log((dp[n] + 1000) % 1000);
}