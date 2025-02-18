const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let [n, k] = input[0].trim().split(" ").map(Number);

let ans = 0;
let digit = 1;
let nine = 9;

while (k > digit * nine) {
  k -= digit * nine;
  ans += nine;
  digit += 1;
  nine *= 10;
}

ans += Math.floor((k - 1) / digit) + 1;

if (ans > n) {
  console.log(-1);
} else {
  console.log((ans + "")[(k - 1) % digit]);
}