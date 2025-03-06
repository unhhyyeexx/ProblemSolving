const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = input.length;
const dp = Array.from({ length: 16 }, () => Array(16).fill(0));

for (let i = 0; i < n; i++) {
  const [white, black] = input[i].trim().split(" ").map(Number);
  for (let w = 15; w > -1; w--) {
    for (let b = 15; b > -1; b--) {
      if (w !== 0) {
        // 백 선수 영입 x VS 영입 o
        dp[w][b] = Math.max(dp[w][b], dp[w - 1][b] + white);
      }
      if (b !== 0) {
        // 흑흑 선수 영입 x VS 영입 o
        dp[w][b] = Math.max(dp[w][b], dp[w][b - 1] + black);
      }
    }
  }
}

console.log(dp[15][15]);