const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);

const trans = (c) => c.charCodeAt() - 97;

const words = [];
for (let i = 1; i < n + 1; i++) {
  const tmp = input[i].trim().split("");
  let bit = Array(26).fill(0);
  for (const ch of tmp) {
    const idx = trans(ch);
    bit[idx] = 1;
  }
  words.push(parseInt(bit.join(""), 2));
}

let alpha = Array(26).fill(0);
const answer = []

for (let i = n + 1; i < n + m + 1; i++) {
  const [o, x] = input[i].trim().split(" ");
  let alphaIdx = trans(x);

  if (o === "1") {
    alpha[alphaIdx] = 1;
  } else {
    alpha[alphaIdx] = 0;
  }

  let cnt = 0;
  const unknown = parseInt(alpha.join(""), 2);
  for (const word of words) {
    if ((unknown & word) > 0) {
      cnt += 1;
    }
  }

  answer.push(n-cnt)
}

console.log(answer.join('\n'));