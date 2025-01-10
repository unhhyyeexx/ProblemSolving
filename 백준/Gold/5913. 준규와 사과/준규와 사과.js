const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const k = +input[0];
const board = Array.from({ length: 5 }, () => Array(5).fill(false));
for (let i = 1; i < k + 1; i++) {
  const [x, y] = input[i].trim().split(" ").map(Number);
  board[x - 1][y - 1] = true;
}

function solution() {
  // 준규와 해빈의 루트를 하나로 본다
  // -> (0,0)에서 (4,4)까지 가는 경우의 수가 답
  let answer = 0;

  const dir = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];
  const able = 25 - k; // 돌 없는 칸

  function findRoute(i, j, visited) {
    if (i === 4 && j === 4) {
      if (visited === able) answer += 1;

      return;
    }

    for (const [di, dj] of dir) {
      const ni = i + di;
      const nj = j + dj;
      if (ni < 0 || nj < 0 || ni >= 5 || nj >= 5) continue;

      if (!board[ni][nj]) {
        board[ni][nj] = true;
        findRoute(ni, nj, visited + 1);
        board[ni][nj] = false;
      }
    }
  }

  board[0][0] = true;
  findRoute(0, 0, 1);

  return answer;
}

console.log(solution());