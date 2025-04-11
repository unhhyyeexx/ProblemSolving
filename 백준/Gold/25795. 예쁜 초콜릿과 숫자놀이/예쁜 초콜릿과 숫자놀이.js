const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, a, b, c] = input[0].trim().split(" ").map(Number);

const mod = 100000;
let answer = 0;
const visit = new Set();

function solution(white, dark, value) {
  const key = `${white}, ${dark}, ${value}`;
  if (visit.has(key)) return;

  visit.add(key);

  if (dark === n) {
    answer = Math.max(answer, value);
    return;
  }

  if (white < n) {
    solution(white + 1, dark, (value + b) % mod);
  }
  if (white > dark) {
    solution(white, dark + 1, (value * c) % mod);
  }
}

solution(0, 0, a);
console.log(answer);