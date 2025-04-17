const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);
const graph = [];
const parent = Array(n + 1).fill(-1);

let day = 1;

for (let i = 1; i <= m; i++) {
  const [u, v, t] = input[i].trim().split(" ").map(Number);
  graph.push([u, v, t]);
}
graph.sort((a, b) => a[2] - b[2]);

function find(x) {
  if (parent[x] < 0) return x;
  parent[x] = find(parent[x]);
  return parent[x];
}

function union(x, y) {
  x = find(x);
  y = find(y);
  if (x === y) return false;

  parent[y] += parent[x];
  parent[x] = y;
  return true;
}

for (const [u, v, t] of graph) {
  if (t !== day) break; // 오늘 디저트 못먹으면 끝
  if (!union(u, v)) break; // 이미 연결된 상태 : 사이클클
  day++;
}

console.log(day);
