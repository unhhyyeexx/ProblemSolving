const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);
const board = [];
for (let i = 1; i < n + 1; i++) {
  board.push(input[i].trim().split(""));
}
let [pr, pc] = input[n + 1].trim().split(" ").map(Number);
pr -= 1;
pc -= 1;

function solution() {
  const dir = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
  ];
  const dir2 = ["U", "R", "D", "L"];
  const sl = [1, 0, 3, 2];
  const bsl = [3, 2, 1, 0];

  let answer = 0; //time
  let ansDir = 0;

  for (let dd = 0; dd < 4; dd++) {
    let i = pr,
      j = pc,
      d = dd,
      t = 1;
    while (true) {
      const ni = i + dir[d][0];
      const nj = j + dir[d][1];
      if (ni < 0 || ni >= n || nj < 0 || nj >= m || board[ni][nj] === "C") {
        break;
      }

      if (board[ni][nj] === "/") {
        d = sl[d];
      } else if (board[ni][nj] === "\\") {
        d = bsl[d];
      }
      t += 1;

      if (ni === pr && nj === pc && d === dd) {
        console.log(dir2[dd]);
        console.log("Voyager");
        return;
      }

      i = ni;
      j = nj;
    }

    if (answer < t) {
      answer = t;
      ansDir = dd;
    }
  }
  console.log(dir2[ansDir]);
  console.log(answer);
}

solution();
