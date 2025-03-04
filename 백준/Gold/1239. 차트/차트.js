const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
const arr = input[1].trim().split(" ").map(Number);

let ans = 0;
let visit = [];
let op = [];

function solution(k) {
  if (k === n) {
    let cnt = 0;
    for (let i = 0; i < n; i++) {
      let sumV = 0;
      let idx = i;
      while (true) {
        sumV += op[idx];
        idx++;
        idx = idx % n;
        if (sumV === 50) {
          cnt += 1;
          break;
        } else if (sumV > 50) {
          break;
        }
      }
    }
    ans = Math.max(ans, cnt);
    return;
  }

  // 순열 생성
  for (let i = 0; i < n; i++) {
    if (!visit[i]) {
      visit[i] = true;
      op[k] = arr[i];
      solution(k + 1);
      visit[i] = false;
    }
  }
}

op = new Array(n);
visit = new Array(n).fill(false);

solution(0);

console.log(Math.floor(ans / 2));
