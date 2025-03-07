const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const s = input[0].trim().split("");
const t = input[1].trim().split("");

const cntList = Array.from({ length: t.length }, () => 0);
const idx = {};
for (let i = 0; i < t.length; i++) {
  idx[t[i]] = i;
}

for (const el of s) {
  if (!t.includes(el)) continue;
  const nowIdx = idx[el];
  if (nowIdx === 0 || cntList[nowIdx] < cntList[nowIdx - 1]) {
    cntList[nowIdx] += 1;
  }
}

console.log(cntList[t.length - 1]);
