const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, k] = input[0].trim().split(" ").map(Number);
const airport = [[0, 0]];
for (let i = 1; i < n + 1; i++) {
  airport.push(input[i].trim().split(" ").map(Number));
}
airport.push([10000, 10000]);

const calc = (c1, c2) => (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2;
const dist = Array.from({ length: n + 2 }, () => Array(n + 2).fill(0));

for (let i = 0; i < n + 1; i++) {
  for (let j = i; j < n + 2; j++) {
    if (i === j) {
      dist[i][j] = Infinity;
    } else {
      dist[i][j] = calc(airport[i], airport[j]);
      dist[j][i] = calc(airport[i], airport[j]);
    }
  }
}

function bfs(cur, cnt, cost) {
  const q = [[cur, cnt]];
  const visit = Array(n + 2).fill(0);
  visit[0] = 1;

  while (q.length > 0) {
    const [idx, cntt] = q.shift();
    if (idx === n + 1) {
      return true;
    }
    if (cntt > k) continue;
    for (let i = 1; i < n + 2; i++) {
      if (cntt <= k && visit[i] === 0) {
        if (dist[idx][i] <= cost) {
          visit[i] = true;
          q.push([i, cntt + 1]);
        }
      }
    }
  }
  return false;
}

let answer = 0;
let l = 1;
let r = 1415;

while (l <= r) {
  const mid = Math.floor((l + r) / 2);
  const cost = mid ** 2 * 100;
  if (bfs(0, 0, cost)) {
    r = mid - 1;
    answer = mid;
  } else {
    l = mid + 1;
  }
}

console.log(answer);
