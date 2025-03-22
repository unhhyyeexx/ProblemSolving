const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m, k] = input[0].trim().split(" ").map(Number);
const scores = [];
for (let i = 1; i < n + 1; i++) {
  const [x, y] = input[i].trim().split(" ").map(Number);
  scores.push([x, y, false]);
}

// 심판 점수 내림차순, 주최자 점수 내림차순 순
scores.sort((a, b) => b[1] - a[1] || b[0] - a[0]);

// 상위 k개 선택
for (let i = 0; i < k; i++) {
  scores[i][2] = true;
}

// 주최자 점수 기준 내림차순, 심판점수 기준 내림차순
scores.sort((a, b) => b[0] - a[0] || b[1] - a[1]);

// m개 선택
let remainCnt = m;
for (let i = 0; remainCnt > 0; i++) {
  if (!scores[i][2]) {
    scores[i][2] = true;
    remainCnt--;
  }
}

let answer = 0;
for (const sc of scores) {
  if (sc[2]) {
    answer += sc[0];
  }
}

console.log(answer);