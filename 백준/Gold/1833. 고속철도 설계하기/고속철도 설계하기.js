const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n] = input[0].split(" ").map(Number);
const graph = [];
for (let i = 1; i < n + 1; i++) {
  graph.push(
    input[i]
      .trim()
      .split(/\s+/)
      .map((e) => Number(e))
  );
}

function find_parent(parent, x) {
  if (parent[x] !== x) parent[x] = find_parent(parent, parent[x]);

  return parent[x];
}

function union_parent(parent, a, b) {
  a = find_parent(parent, a);
  b = find_parent(parent, b);

  if (a < b) parent[b] = a;
  else parent[a] = b;
}

function solution() {
  const parent = Array.from({ length: n + 1 }, (el, i) => i);
  const costs = [];
  let totalCost = 0;

  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      if (graph[i][j] < 0) {
        totalCost -= graph[i][j];
        union_parent(parent, i + 1, j + 1);
      } else {
        costs.push([graph[i][j], i + 1, j + 1]);
      }
    }
  }

  costs.sort((a, b) => a[0] - b[0]);

  const newWay = [];
  for (const [cost, a, b] of costs) {
    if (find_parent(parent, a) !== find_parent(parent, b)) {
      union_parent(parent, a, b);
      totalCost += cost;
      newWay.push([a, b]);
    }
  }

  console.log(totalCost, newWay.length);
  for (nw of newWay) {
    console.log(nw.join(" "));
  }
}

solution();