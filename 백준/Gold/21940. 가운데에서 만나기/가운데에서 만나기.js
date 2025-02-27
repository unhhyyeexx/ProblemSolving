const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);
const graph = Array.from({ length: n + 1 }, () => Array(n + 1).fill(Infinity));
for (let i = 1; i < m + 1; i++) {
  const [a, b, t] = input[i].trim().split(" ").map(Number);
  graph[a][b] = t;
}
const K = +input[m + 1];
const C = input[m + 2].trim().split(" ").map(Number);

// 자기 자신에게로 가는 비용
for (let i = 1; i < n + 1; i++) {
  graph[i][i] = 0;
}

// 플로이드-워셜
for (let k = 1; k < n + 1; k++) {
  for (let j = 1; j < n + 1; j++) {
    for (let i = 1; i < n + 1; i++) {
      graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
    }
  }
}

// 최대 왕복시간
const cities = Array(n + 1).fill(0);
for (let D = 1; D < n + 1; D++) {
  let maxV = 0;
  for (const c of C) {
    if (c === D || graph[c][D] === Infinity || graph[D][c] === Infinity)
      continue;
    maxV = Math.max(maxV, graph[D][c] + graph[c][D]);
  }
  cities[D] = maxV;
}

// 최소 왕복시간
// 위에서 구한 최대 왕복시간 중에서 가장 작은 왕복시간을 가진 모든 도시 출력력
const answer = [];
let target = Math.min(...cities.slice(1));
for (let D = 1; D < n + 1; D++) {
  if (cities[D] === target) {
    answer.push(D);
  }
}

console.log(...answer);