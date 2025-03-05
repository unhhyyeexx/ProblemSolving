const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 문자.charCodeAt() - 64 = 1~26
// String.fromCharCode(숫자+64) = 문자

let answer = [];
const star = [];
let idx = 0;
const visit = new Array(13).fill(false);
for (let i = 0; i < 5; i++) {
  for (let j = 0; j < 9; j++) {
    if (input[i][j] !== ".") {
      star.push(input[i][j]);
      idx += 1;
      if (input[i][j] != "x") {
        visit[input[i][j].charCodeAt() - 64] = true;
      }
    }
  }
}

const lines = [
  [0, 2, 5, 7],
  [1, 2, 3, 4],
  [0, 3, 6, 10],
  [7, 8, 9, 10],
  [1, 5, 8, 11],
  [4, 6, 9, 11],
];

function check() {
  for (const line of lines) {
    let lineSum = 0;
    for (const l of line) {
      lineSum += star[l].charCodeAt() - 64;
    }
    if (lineSum !== 26) return false;
  }
  return true;
}

let flag = false;

function magic(cur, mstar) {
  if (flag) return;
  if (cur === 12) {
    if (check()) {
      flag = true;
      answer = [...mstar];
    }
    return;
  }

  if (mstar[cur] !== "x") {
    magic(cur + 1, mstar);
  } else {
    for (let i = 1; i < 13; i++) {
      if (!visit[i]) {
        mstar[cur] = String.fromCharCode(i + 64);
        visit[i] = true;
        magic(cur + 1, mstar);
        visit[i] = false;
        mstar[cur] = "x";
        if (flag) return;
      }
    }
  }
}

magic(0, star);

idx = 0;
const result = [];
for (let i = 0; i < 5; i++) {
  let tmp = "";
  for (let j = 0; j < 9; j++) {
    if (input[i][j] !== ".") {
      tmp += answer[idx];
      idx += 1;
    } else {
      tmp += ".";
    }
  }
  result.push(tmp);
}

for (let i = 0; i < 5; i++) {
  console.log(result[i]);
}