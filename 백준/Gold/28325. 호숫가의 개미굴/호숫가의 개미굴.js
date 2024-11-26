const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
let room = input[1].trim().split(" ").map(Number);

function solution() {
  let total = 0;
  room.forEach((n) => (total += n));
  if (total === 0) return parseInt(n / 2);

  let flag = 0;
  for (let i = 0; i < n; i++) {
    if (room[i] > 0) {
      flag = 0;
      break;
    }
  }
  room = [...room.slice(flag, n), ...room.slice(0, flag)];

  let zeroCnt = 0;
  for (let i = 0; i < n; i++) {
    if (room[i] === 0) {
      zeroCnt += 1;
    } else {
      total += parseInt((zeroCnt + 1) / 2);
      zeroCnt = 0;
    }
  }

  if (zeroCnt > 0) {
    total += parseInt((zeroCnt + 1) / 2);
  }

  return total;
}

console.log(solution());

