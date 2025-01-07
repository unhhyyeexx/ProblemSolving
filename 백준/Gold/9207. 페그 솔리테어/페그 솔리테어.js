const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
const dir = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];

for (let k = 0; k < n; k++) {
  const board = [];
  for (let i = 0; i < 5; i++) {
    board.push(input[k * 5 + k + 1 + i].trim().split(""));
  }

  let minMove = 8; // 최소로 움직였을 때 움직인 횟수
  let minPin = 8; // 최소 핀의 개수

  function dfs(board, pinCnt, move) {
    if (pinCnt < minPin || (pinCnt === minPin && move < minMove)) {
      minMove = move;
      minPin = pinCnt;
    }

    for (let i = 0; i < 5; i++) {
      for (let j = 0; j < 9; j++) {
        if (board[i][j] === "o") {
          for (const [di, dj] of dir) {
            const ni = i + di;
            const nj = j + dj;
            const nni = ni + di;
            const nnj = nj + dj;

            if (nni < 0 || nnj < 0 || nni >= 5 || nnj >= 9) continue;
            if (board[ni][nj] === "o" && board[nni][nnj] === ".") {
              // 상태 변경
              board[i][j] = ".";
              board[ni][nj] = ".";
              board[nni][nnj] = "o";

              dfs(board, pinCnt - 1, move + 1);

              // 상태 복원
              board[i][j] = "o";
              board[ni][nj] = "o";
              board[nni][nnj] = ".";
            }
          }
        }
      }
    }
  }

  let initPin = 0;
  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 9; j++) {
      if (board[i][j] === "o") {
        initPin++;
      }
    }
  }

  dfs(board, initPin, 0);
  console.log(minPin, minMove);
}
