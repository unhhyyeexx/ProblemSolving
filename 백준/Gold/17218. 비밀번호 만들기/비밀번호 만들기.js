const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const a = input[0].trim().split("");
const b = input[1].trim().split("");

let alen = a.length;
let blen = b.length;

const dp = Array.from({ length: alen + 1 }, () => Array(blen + 1).fill(0));

for (let i = 1; i <= alen; i++) {
  for (let j = 1; j <= blen; j++) {
    if (a[i - 1] === b[j - 1]) {
      dp[i][j] = dp[i - 1][j - 1] + 1;
    } else {
      dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
    }
  }
}

let answer = [];
while (dp[alen][blen] !== 0) {
  if (dp[alen][blen] === dp[alen - 1][blen]) {
    alen -= 1;
  } else if (dp[alen][blen] === dp[alen][blen - 1]) {
    blen -= 1;
  } else {
    answer.push(a[alen - 1]);
    alen -= 1;
    blen -= 1;
  }
}

console.log(answer.reverse().join(""));