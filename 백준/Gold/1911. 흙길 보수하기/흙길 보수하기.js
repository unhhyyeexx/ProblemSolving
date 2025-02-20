const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, l] = input[0].trim().split(" ").map(Number);
const puddles = [];
for (let i = 1; i < n + 1; i++) {
  puddles.push(input[i].trim().split(" ").map(Number));
}
puddles.sort((a, b) => a[0] - b[0]);

let answer = 0;
let now = 0;
for (const [s, e] of puddles) {
  let tmp = 0;
  if (now < s) {
    tmp += Math.floor((e - s) / l);
    if ((e - s) % l > 0) {
      tmp += 1;
    }

    now = s + l * tmp;
  } else if (e > now) {
    tmp += Math.floor((e - now) / l);
    if ((e - now) % l > 0) {
      tmp += 1;
    }

    now += l * tmp;
  } else {
    continue;
  }

  answer += tmp;
}

console.log(answer);