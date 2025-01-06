const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
const time = Array.from({ length: n + 1 }, () => 0);
const graph = Array.from({ length: n + 1 }, () => []);
const indegree = Array.from({ length: n + 1 }, () => 0);
const dp = Array.from({ length: n + 1 }, () => 0);

for (let i = 1; i <= n; i++) {
  const tmp = input[i].trim().split(" ").map(Number);
  time[i] = tmp[0];
  if (tmp.length > 2) {
    for (let j = 1; j < tmp.length - 1; j++) {
      // 간선 연결, 진입차수 설정
      graph[tmp[j]].push(i);
      indegree[i] += 1;
    }
  }
}

const q = [];
for (let i = 1; i < n + 1; i++) {
  if (indegree[i] === 0) {
    q.push(i);
    dp[i] = time[i];
  }
}

while (q.length > 0) {
  const now = q.shift();
  for (idx of graph[now]) {
    indegree[idx] -= 1;
    dp[idx] = Math.max(dp[idx], dp[now] + time[idx]);
    if (indegree[idx] === 0) {
      q.push(idx);
    }
  }
}

for (el of dp) {
  if (el !== 0) {
    console.log(el);
  }
}