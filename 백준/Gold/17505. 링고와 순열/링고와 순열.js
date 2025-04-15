const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let [n, k] = input[0].trim().split(" ").map(Number);
let s = 1;
let e = n;

let answer = Array(n + 1);
for (let i = 1; i <= n; i++) {
  if (k >= n - i) {
    k -= n - i;
    answer[i] = e--;
  } else {
    answer[i] = s++;
  }
}

if (k !== 0 || s <= e) {
  console.log(-1);
} else {
  console.log(answer.splice(1).join(" "));
}