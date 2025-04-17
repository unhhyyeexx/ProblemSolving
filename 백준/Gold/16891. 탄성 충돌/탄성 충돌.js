const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];

// console.log(Math.floor(Math.PI * n));

const m1 = 1;
const m2 = n * n;
let v1 = 0;
let v2 = -1;
let count = 0;

while (true) {
  // 물체1과 물체2가 충돌
  if (v2 < v1) {
    const new_v1 = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2);
    const new_v2 = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2);
    v1 = new_v1;
    v2 = new_v2;
    count++;
  } else {
    // 물체1이 벽과 충돌할 경우
    if (v1 < 0) {
      v1 = -v1;
      count++;
    } else {
      break; // 더 이상 충돌 없음
    }
  }
}

console.log(count);
