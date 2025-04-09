const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let i = 0;
for (let t = 0; t < 3; t++) {
  const n = +input[i++];
  let total = 0;
  const coins = {};
  for (let j = 0; j < n; j++) {
    const [coin, cnt] = input[i++].trim().split(" ").map(Number);
    total += coin * cnt;
    coins[coin] = cnt;
  }

  if (total % 2 === 1) {
    console.log(0);
    continue;
  }

  total /= 2;
  const dp = Array(total + 1).fill(0);
  dp[0] = 1;

  for (let coin of Object.keys(coins)) {
    for (let money = total; money > coin - 1; money--) {
      if (dp[money - coin] === 1) {
        for (let j = 0; j < coins[coin]; j++) {
          if (money + coin * j <= total) {
            dp[money + coin * j] = 1;
          }
        }
      }
    }
  }
  console.log(dp[total]);
}