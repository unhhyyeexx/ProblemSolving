const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const check1 = Array(1000001).fill(1);
const check2 = Array(1000001).fill(0);
check1[0] = 0;
check1[1] = 0;
for (let i = 2; i < 1500; i++) {
  if (check1[i] !== 0) {
    for (let j = 2 * i; j < 1000001; j += i) {
      check1[j] = 0;
    }
  }
}
check2[2] = 1;
for (let i = 3; i < 1000001; i++) {
  if (check1[i] !== 0 && i % 4 === 1) {
    check2[i] = 1;
  }
}

for (let i = 1; i < 1000001; i++) {
  check1[i] += check1[i - 1];
  check2[i] += check2[i - 1];
}

let index = 0;
while (true) {
  const [l, u] = input[index++].trim().split(" ").map(Number);
  if (l === -1 && u === -1) break;

  let x, y;
  if (l >= 1) {
    x = check1[u] - check1[l - 1];
    y = check2[u] - check2[l - 1];
  } else if (l < 1 && u >= 0) {
    x = check1[u];
    y = check2[u];
  } else if (l < 1 && u < 1) {
    x = 0;
    y = 0;
  }
  console.log(l, u, x, y);
}