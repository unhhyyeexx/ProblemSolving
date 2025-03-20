const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const k = +input[0];
let binK = (k + 1).toString(2);

if (binK === "1") {
  console.log(4);
}
binK = binK.slice(1);
binK = binK.replace(/1/g, "7");
binK = binK.replace(/0/g, "4");
console.log(binK);

// 1 1 4 => 0
// 2 10 7 => 1
// 3 11 44 => 00
// 4 100 47 => 01
// 5 101 74 => 10
// 6 110 77
// 하나 큰거에서 맨 앞자리 1빼고 가져오기