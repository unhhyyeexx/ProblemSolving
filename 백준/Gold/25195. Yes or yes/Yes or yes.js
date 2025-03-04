const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);
graph = Array.from({ length: n + 1 }, () => []);
for (let i = 1; i < m + 1; i++) {
  const [u, v] = input[i].trim().split(" ").map(Number);
  graph[u].push(v);
}
const S = +input[m + 1];
const ss = input[m + 2].trim().split(" ").map(Number);

if (ss.includes(1)) {
  console.log("Yes");
  process.exit();
}

const q = [];
q.push(1);
while (q.length > 0) {
  const now = q.shift();
  if (graph[now].length === 0) {
    console.log("yes");
    process.exit();
  }

  for (const next of graph[now]) {
    if (ss.includes(next)) continue;
    q.push(next);
  }
}

console.log("Yes");