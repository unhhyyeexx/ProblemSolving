const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, q] = input[0].trim().split(" ").map(Number);
const xCoord = input[1].trim().split(" ").map(Number);
const yCoord = input[2].trim().split(" ").map(Number);
const dist1 = [];
const dist2 = [];

for (let i = 1; i < n; i++) {
  const dist = Math.sqrt(
    (xCoord[i] - xCoord[i - 1]) ** 2 + (yCoord[i] - yCoord[i - 1]) ** 2
  );
  if (yCoord[i] > yCoord[i - 1]) {
    // 오르막
    dist1.push(dist * 3);
    dist2.push(dist);
  } else if (yCoord[i] === yCoord[i - 1]) {
    // 평지
    dist1.push(dist * 2);
    dist2.push(dist * 2);
  } else {
    // 내리막
    dist1.push(dist);
    dist2.push(dist * 3);
  }
}

const prefix = Array(n).fill(0);
const rvsprefix = Array(n).fill(0);
for (let i = 1; i < n; i++) {
  prefix[i] = prefix[i - 1] + dist1[i - 1];
  rvsprefix[n - 1 - i] = rvsprefix[n - i] + dist2[n - 1 - i];
}

const answer = [];
for (let i = 3; i < 3 + q; i++) {
  const [a, b] = input[i].trim().split(" ").map(Number);
  if (a < b) {
    answer.push(prefix[b - 1] - prefix[a - 1]);
  } else {
    answer.push(rvsprefix[b - 1] - rvsprefix[a - 1]);
  }
}

console.log(answer.join("\n"));