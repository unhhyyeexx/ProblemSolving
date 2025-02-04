const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);
const memories = input[1].trim().split(" ").map(Number);
const costs = input[2].trim().split(" ").map(Number);

function solution() {
  const tmp = costs.reduce((a, b) => a + b, 0);
  const dp = Array(tmp + 1).fill(0);

  for (let i = 0; i < n; i++) {
    const memory = memories[i];
    const cost = costs[i];

    for (let j = tmp; j >= cost; j--) {
      dp[j] = Math.max(dp[j], dp[j - cost] + memory);
    }
  }

  for (let i = 0; i < tmp + 1; i++) {
    if (dp[i] >= m) {
      console.log(i);
      break;
    }
  }
}

solution();
