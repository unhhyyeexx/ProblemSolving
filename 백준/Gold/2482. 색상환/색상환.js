const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
const k = +input[1];

function solution() {
  const dp = Array.from({ length: n + 1 }, () => Array(k + 1).fill(0));

  for (let i = 0; i < n + 1; i++) {
    dp[i][0] = 1; // i개 중에서 아무것도 안뽑는 경우
    dp[i][1] = i; // i개중에서 1개 뽑는 경우
  }

  for (let i = 2; i < n + 1; i++) {
    for (let j = 2; j < k + 1; j++) {
      // i번 포함 안할 때 dp[i-1][j]
      dp[i][j] += dp[i - 1][j];

      // i번째 색 포함하고 j개 선택 :dp[i-2][j-1] (i-1번 선택 못하니까 i-2, i선택했으므로 j-1개)
      if (i !== n) {
        dp[i][j] += dp[i - 2][j - 1];
      } else {
        // n번을 선택하면 1번도 못씀 그러므로 i-3개 중에서 j-1개 선택
        dp[i][j] += dp[i - 3][j - 1];
      }

      dp[i][j] %= 1000000003;
    }
  }
  console.log(dp[n][k]);
}

solution();