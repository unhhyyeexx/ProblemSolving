const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, r, q] = input[0].trim().split(" ").map(Number);
const graph = Array.from({ length: n + 1 }, () => Array());
for (let i = 1; i < n; i++) {
  const [u, v] = input[i].trim().split(" ").map(Number);
  graph[u].push(v);
  graph[v].push(u);
}

const child = Array(n + 1).fill(1);
const visit = Array(n + 1).fill(0);

function dfs(node) {
  visit[node] = 1;

  for (const next of graph[node]) {
    if (visit[next] === 1) continue;

    child[node] += dfs(next);
  }

  return child[node];
}

dfs(r);

for (let i = n; i < n + q; i++) {
  console.log(child[+input[i]]);
}
