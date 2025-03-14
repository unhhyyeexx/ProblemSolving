const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);
const hi = input[1].trim().split(" ").map(Number);
const arc = input[2].trim().split(" ").map(Number);
hi.sort((a, b) => a - b);
arc.sort((a, b) => a - b);

function bs(now, enemy) {
  let left = 0,
    right = m - 1;
  let tie_start = -1,
    tie_end = -1;

  // 가장 왼족 동점 시작 위치 찾기
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (enemy[mid] >= now) {
      if (enemy[mid] === now) {
        tie_start = mid;
      }
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  if (tie_start === -1) {
    return [left, m - left, 0];
  }

  // 가장 오른쪽 동점 끝 위치 찾기기
  (left = 0), (right = m - 1);
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (enemy[mid] <= now) {
      if (enemy[mid] === now) tie_end = mid;
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  const tie_cnt = tie_end - tie_start + 1; // 동점 개수수
  return [tie_start, m - tie_end - 1, tie_cnt];
}

// left가 동점인지 봐야됨 동점이면 이긴거 +left -1, 동점 + 1, 진거 length - left
const answer = [0, 0, 0];
for (let i = 0; i < n; i++) {
  const [win, lose, tie] = bs(hi[i], arc);
  answer[0] += win;
  answer[1] += lose;
  answer[2] += tie;
}

console.log(answer.join(" "));