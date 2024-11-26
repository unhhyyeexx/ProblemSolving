const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
let room = input[1].trim().split(" ").map(BigInt);

function solution() {
  let flag = 0;
  for (let i = 0; i < n; i++) {
    if (room[i] > 0n) {
      flag = i;
      break;
    }
  }
  room = [...room.slice(flag), ...room.slice(0, flag)];
  if (room[0] === 0n && room.at(-1) === 0n) {
    room.pop();
  }

  const newN = room.length;
  let answer = 0n;
  for (let i = 0; i < newN; i++) {
    if (room[i] === 0n) {
      answer++;
      if (room[i + 1] === 0n) i++;
    } else {
      answer += room[i];
    }
  }

  return answer.toString();
}

console.log(solution());