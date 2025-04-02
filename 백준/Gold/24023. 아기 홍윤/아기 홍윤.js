const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, k] = input[0].trim().split(" ").map(Number);
const arr = input[1].trim().split(" ").map(Number);

function solution() {
  let result = [-1, -1];
  let prevOr = new Map();

  for (let i = 0; i < n; i++) {
    let currentOr = new Map();
    currentOr.set(arr[i], i);
    for (const [orVal, startIdx] of prevOr.entries()) {
      const newOr = orVal | arr[i];
      if (!currentOr.has(newOr) || currentOr.get(newOr) > startIdx) {
        currentOr.set(newOr, startIdx);
      }
    }

    if (currentOr.has(k)) {
      result = [currentOr.get(k) + 1, i + 1];
      break;
    }

    prevOr.clear();
    for (const [key, val] of currentOr.entries()) {
      prevOr.set(key, val);
    }
  }

  return result[0] === -1 ? [-1] : result;
}

const answer = solution();
console.log(answer.join(" "));
