const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const dir = [
  [1, 0, 0],
  [-1, 0, 0],
  [0, 1, 0],
  [0, -1, 0],
  [0, 0, 1],
  [0, 0, -1],
];

while (input.length) {
  const [l, r, c] = input.shift().trim().split(" ").map(Number);
  if (l === 0) break;

  const board = [];
  let floor = [];

  while (board.length < l) {
    const tmp = input.shift().trim().split("");
    if (tmp.length) {
      floor.push(tmp);
    } else {
      board.push(floor);
      floor = [];
    }
  }

  solution(l, r, c, board);
}

function findStart(l, r, c, board) {
  // 시작점 v위치찾기
  for (let i = 0; i < l; i++) {
    for (let j = 0; j < r; j++) {
      for (let k = 0; k < c; k++) {
        if (board[i][j][k] === "S") {
          return [i, j, k, 0];
        }
      }
    }
  }
}

function bfs(L, R, C, board, start) {
  let q = [start];
  board[q[0][0]][q[0][1]][q[0][2]] = "#"; //방문표시

  while (q.length) {
    let [l, r, c, cnt] = q.shift();
    for ([dl, dr, dc] of dir) {
      let nl = l + dl;
      let nr = r + dr;
      let nc = c + dc;

      if (nl < 0 || nl >= L || nr < 0 || nr >= R || nc < 0 || nc >= C) continue;

      if (board[nl][nr][nc] !== "#") {
        if (board[nl][nr][nc] === "E") {
          // 탈출 시
          return `Escaped in ${cnt + 1} minute(s).`;
        }

        board[nl][nr][nc] = "#"; //방문표시
        q.push([nl, nr, nc, cnt + 1]);
      }
    }
  }

  return "Trapped!";
}

function solution(l, r, c, board) {
  console.log(bfs(l, r, c, board, findStart(l, r, c, board)));
}
