const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, x] = input[0].trim().split(" ").map(Number);
const menu = [];
for (let i = 1; i < n + 1; i++) {
  menu.push(input[i].trim().split(" ").map(Number));
}

function solution() {
  menu.sort((a, b) => b[0] - b[1] - (a[0] - a[1]));
  let xx = x - 1000 * n;
  let answer = 0;
  for (let i = 0; i < n; i++) {
    let [a, b] = menu[i];
    if (xx >= 4000 && a > b) {
      xx -= 4000;
      b = a;
    }
    answer += b;
  }

  console.log(answer);
}

solution();