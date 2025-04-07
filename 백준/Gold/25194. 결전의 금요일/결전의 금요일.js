const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
const arr = input[1].trim().split(" ").map(Number);

let dp = Array(7).fill(0);
dp[0] = 1;

for (const a of arr) {
  const tmp = Array(7).fill(0);
  for (let i = 0; i < 7; i++) {
    if (dp[i] != 0) {
      tmp[(a + i) % 7] = 1;
      tmp[i] = 1;
    }
  }
  dp = [...tmp];
}

if (dp[4] != 0) {
  console.log("YES");
} else {
  console.log("NO");
}
