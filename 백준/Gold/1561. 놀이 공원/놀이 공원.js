const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);
const times = input[1].trim().split(" ").map(Number);

function solution() {
  if (n <= m) {
    return n;
  }

  let left = 0;
  let right = 30 * n;
  let t = 0;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    let cnt = m; // mid안에 놀이기구를 탄 아이들 수, 0분에서 모든 놀이기구 탑승하므로 기본값 m
    for (const time of times) {
      cnt += Math.floor(mid / time);
    }
    if (cnt >= n) {
      t = mid;
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  let cnt = m;
  // t-1초까지 탄 아이들 수를 구해서
  // t초에 새롭게 탄 수만 확인해 n번째 아이를 찾는다.
  for (const time of times) {
    cnt += Math.floor((t - 1) / time);
  }

  for (let i = 0; i < m; i++) {
    if (t % times[i] === 0) {
      cnt += 1;
    }
    if (cnt === n) {
      return i + 1;
    }
  }
}

console.log(solution());