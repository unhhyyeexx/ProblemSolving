const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [s, n, k, r1, r2, c1, c2] = input[0].trim().split(" ").map(Number);

const size = n ** s;

function recur(now, x, y) {
  // now: 현재 정사각형 변 길이, xy: 현재 좌표
  if (now === 1) return 0;

  const next = now / n; // 다음단계 변 길이
  const lower = next * Math.floor((n - k) / 2);
  const upper = next * Math.floor((n + k) / 2);

  if (x >= lower && x < upper && y >= lower && y < upper) {
    // 현재 좌표 중심영역이면 바로 검정
    return 1;
  }

  return recur(next, x % next, y % next);
}

let answer = "";
for (let i = r1; i <= r2; i++) {
  for (let j = c1; j <= c2; j++) {
    answer += recur(size, i, j);
  }
  answer += "\n";
}

console.log(answer);
