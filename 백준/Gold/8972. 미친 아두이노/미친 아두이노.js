const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [r, c] = input[0].split(" ").map(Number);
const board = [];
let jongsu = [];
let crazy = [];
for (let i = 1; i < input.length - 1; i++) {
  const tmp = input[i].toString().trim().split("");
  board.push(tmp);
  // 초기 종수 위치, 미친 아두이노 위치
  for (let j = 0; j < c; j++) {
    if (tmp[j] === "I") {
      jongsu = [i - 1, j];
    } else if (tmp[j] === "R") {
      crazy.push([i - 1, j]);
    }
  }
}
const move = input[input.length - 1].split("");

const dir = [
  [1, -1],
  [1, 0],
  [1, 1],
  [0, -1],
  [0, 0],
  [0, 1],
  [-1, -1],
  [-1, 0],
  [-1, 1],
];

// 미친 아누이노 위치인지 확인
function isCrazy(r, c) {
  return board[r][c] === "R";
}

function move_jongsu(direction) {
  let [jr, jc] = jongsu;
  const ni = jr + dir[direction - 1][0];
  const nj = jc + dir[direction - 1][1];

  if (isCrazy(ni, nj)) return false;
  else {
    jongsu = [ni, nj];
    board[jr][jc] = ".";
    board[ni][nj] = "I";
    return true;
  }
}

function move_crazy() {
  let [jr, jc] = jongsu;
  const newCrazy = [];
  const crazyCnt = {};

  for ([i, j] of crazy) {
    board[i][j] = ".";
    minDist = 201;
    minLoc = [0, 0];

    // 거리 절대값 작은 곳 찾고, 그 위치 minLoc에 저장
    for ([di, dj] of dir) {
      if (di === 0 && dj === 0) continue;
      const ni = i + di;
      const nj = j + dj;
      if (ni < 0 || nj < 0 || ni >= r || nj >= c) continue;
      if (Math.abs(ni - jr) + Math.abs(nj - jc) < minDist) {
        minDist = Math.abs(ni - jr) + Math.abs(nj - jc);
        minLoc = [ni, nj];
      }
    }

    // 이동한 위치에 종수가 있으면,
    if (minLoc[0] === jr && minLoc[1] === jc) return false;

    // newCrazy.push(minLoc);

    // {아두이노 위치 : 개수}
    crazyCnt[minLoc] = crazyCnt[minLoc] ? 1 + crazyCnt[minLoc] : 1;
  }

  // 한 위치에 아두이노 여러대 -> 폭파 -> new list에 추가 안함
  for (key of Object.keys(crazyCnt)) {
    if (crazyCnt[key] === 1) {
      newCrazy.push(key.split(",").map(Number));
    }
  }

  crazy = newCrazy;
  for ([ci, cj] of crazy) {
    board[ci][cj] = "R";
  }
  return true;
}

function solution() {
  move.forEach((d, idx) => {
    if (!move_jongsu(d)) {
      console.log(`kraj ${idx + 1}`);
      process.exit(0);
    }
    if (!move_crazy()) {
      console.log(`kraj ${idx + 1}`);
      process.exit(0);
    }
  });

  for (b of board) {
    console.log(b.join(""));
  }
}
solution();
