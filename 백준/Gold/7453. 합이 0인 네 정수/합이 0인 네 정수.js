const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
const aa = [],
  bb = [],
  cc = [],
  dd = [];
for (let i = 1; i <= n; i++) {
  const [a, b, c, d] = input[i].trim().split(" ").map(Number);
  aa.push(a);
  bb.push(b);
  cc.push(c);
  dd.push(d);
}

const ab = new Map();
// A와 B의 모든 합을 저장장
for (const a of aa) {
  for (const b of bb) {
    const sumV = a + b;
    ab.set(sumV, (ab.get(sumV) || 0) + 1);
  }
}

let answer = 0;
// C와 D의 합의 음수를 찾아 AB에 있는지 확인
for (const c of cc) {
  for (const d of dd) {
    let target = -(c + d);
    if (ab.has(target)) {
      answer += ab.get(target);
    }
  }
}

console.log(answer);