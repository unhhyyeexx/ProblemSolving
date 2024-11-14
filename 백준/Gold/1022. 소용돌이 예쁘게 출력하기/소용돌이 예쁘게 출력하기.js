const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [r1, c1, r2, c2] = input[0].split(" ").map(Number);
const r = r2 - r1 + 1,
  c = c2 - c1 + 1;
const board = Array.from({ length: r }, () => Array(c).fill(0));
let maxLength = 0;

function make_board() {
  let n = r * c;
  const dir = [
    [0, 1],
    [-1, 0],
    [0, -1],
    [1, 0],
  ];
  let d = 0;
  let i = 0,
    j = 0;
  let value = 1,
    cnt = 1;
  while (n > 0) {
    for (let a = 0; a < 2; a++) {
      for (let b = 0; b < cnt; b++) {
        if (i >= r1 && i <= r2 && j >= c1 && j <= c2) {
          board[i - r1][j - c1] = value;
          n -= 1;
          maxLength = value;
        }
        i += dir[d][0];
        j += dir[d][1];
        value += 1;
      }
      d = (d + 1) % 4;
    }
    cnt += 1;
  }
  maxLength = maxLength.toString().length;
}

function solution() {
  make_board();

  for (let i = 0; i < r; i++) {
    let tmp = [];
    for (let j = 0; j < c; j++) {
      tmp.push(board[i][j].toString().padStart(maxLength, " "));
    }
    console.log(tmp.join(" "));
  }
}

solution();