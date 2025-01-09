const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, k] = input[0].trim().split(" ").map(Number);
const arr = input[1].trim().split(" ").map(Number);

function solution() {
  let answer = 0;
  let left = 0; // 얻을 수 있는 점수 중 최저
  let right = 1e5 * 20 + 1; // 얻을 수 있는 점수 중 최대

  while (left <= right) {
    // 각 그룹의 합이 mid를 넘어야 한다. (mid가 각 그룹 합의 최소값)
    let mid = Math.floor((left + right) / 2);

    let group = 0;
    let score = 0;

    for (el of arr) {
      score += el;
      if (score >= mid) {
        group += 1;
        score = 0;
      }
    }

    if (group >= k) {
      answer = mid;
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return answer;
}

console.log(solution());