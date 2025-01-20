const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
const graph = Array.from({ length: n + 1 }, () => []);
for (let i = 1; i < n; i++) {
  const [a, b] = input[i].trim().split(" ").map(Number);
  graph[a].push(b);
  graph[b].push(a);
}

const m = +input[n];
const arr = [];
for (let i = n + 1; i < n + 1 + m; i++) {
  arr.push(input[i].trim().split(" ").map(Number));
}

const parent = Array(n + 1).fill(0);
const visit = Array(n + 1).fill(0);
const d = Array(n + 1).fill(0);
function dfs(x, depth) {
  visit[x] = true;
  d[x] = depth;

  for (const node of graph[x]) {
    if (visit[node]) continue;

    parent[node] = x;
    dfs(node, depth + 1);
  }
}

function lca(a, b) {
  while (d[a] !== d[b]) {
    if (d[a] > d[b]) {
      a = parent[a];
    } else {
      b = parent[b];
    }
  }

  while (a !== b) {
    a = parent[a];
    b = parent[b];
  }

  return a;
}

function solution() {
  dfs(1, 0);
  for (const [a, b] of arr) {
    console.log(lca(a, b));
  }
}

solution();
