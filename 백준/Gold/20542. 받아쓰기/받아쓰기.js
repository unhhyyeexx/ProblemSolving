const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].split(" ").map(Number);
const sy = input[1];
const answer = input[2];

const dp = Array.from({ length: n + 1 }, () => Array(m + 1).fill(Infinity));
for (let i = 0; i < n; i++) {
  dp[i][0] = i;
}
for (let i = 0; i < m; i++) {
  dp[0][i] = i;
}

for (let i = 1; i < n + 1; i++) {
  for (let j = 1; j < m + 1; j++) {
      
    if (sy[i - 1] === answer[j - 1]) {
      dp[i][j] = dp[i - 1][j - 1];
        
    } else if (sy[i - 1] === "i" && (answer[j - 1] === "j" || answer[j - 1] === "l")) { // 휘갈겨 쓴 i => j, l 정답처리
      dp[i][j] = dp[i - 1][j - 1];
        
    } else if (sy[i - 1] === "v" && answer[j - 1] === "w") { // 휘갈겨 쓴 v => w 정답처리
      dp[i][j] = dp[i - 1][j - 1];
        
    } else {
      dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1;
    }
  }
}

console.log(dp[n][m]);