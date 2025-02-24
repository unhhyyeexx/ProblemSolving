const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
const scores = input[1].trim().split(" ").map(Number);
const [p, q, r, S] = input[2].trim().split(" ").map(Number);

scores.sort((a, b) => a - b);

let left = 1;
let right = 110000;

while (left < right) {
  const mid = Math.floor((left + right) / 2);
  let total = 0;
  for (const s of scores) {
    if (s > mid + r) {
      total += s - p;
    } else if (s < mid) {
      total += s + q;
    } else {
      total += s;
    }
  }
  if (total < S) {
    left = mid + 1;
  } else {
    right = mid;
  }
}

if (right === 110000) {
  console.log(-1);
} else {
  console.log(right);
}