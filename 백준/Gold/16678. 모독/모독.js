const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
const score = [];
for (let i = 1; i <= n; i++) {
  score.push(+input[i]);
}

let maxScore = 1;
let answer = 0;

score.sort((a, b) => a - b);
for (const s of score) {
  if (s >= maxScore) {
    answer += s - maxScore;
    maxScore += 1;
  }
}

console.log(answer);