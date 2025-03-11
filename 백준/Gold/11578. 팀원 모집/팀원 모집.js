const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);
const cap = [];
for (let i = 1; i < m + 1; i++) {
  let student = 0;
  for (const j of input[i].trim().split(" ").splice(1)) {
    student |= 1 << (j - 1);
  }
  cap.push(student);
}

let win = 0;
for (let i = 0; i < n; i++) {
  win |= 1 << i;
}

function combination(arr, n) {
  if (n === 1) return arr.map((el) => [el]);
  const result = [];
  arr.forEach((fixed, idx, origin) => {
    const rest = origin.slice(idx + 1);
    const combis = combination(rest, n - 1);
    const attached = combis.map((combi) => [fixed, ...combi]);
    result.push(...attached);
  });

  return result;
}

for (let i = 1; i < m + 1; i++) {
  for (const students of combination(cap, i)) {
    let tmp = 0;
    for (const st of students) {
      tmp |= st;
    }
    if (tmp === win) {
      console.log(i);
      process.exit();
    }
  }
}

console.log(-1);