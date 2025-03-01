const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m, q] = input[0].trim().split(" ").map(Number);
const water = [0, ...input[1].trim().split(" ").map(Number)];
for (let i = 1; i < n + 1; i++) {
  if (water[i] === 0) {
    water[i] -= 1;
  }
}

const parent = Array(n + 1).fill(0);
for (let i = 1; i < n + 1; i++) {
  parent[i] = i;
}

function find(x) {
  if (parent[x] !== x) {
    parent[x] = find(parent[x]);
  }
  return parent[x];
}

function union(a, b) {
  a = find(a);
  b = find(b);
  if (a < b) {
    water[a] += water[b];
    parent[b] = a;
  } else if (a>b) {
    water[b] += water[a];
    parent[a] = b;
  }
}

for (let i = 2; i < m + 2; i++) {
  const [u, v] = input[i].trim().split(" ").map(Number);
  union(u, v);
}

for (let i = m + 2; i < m + q + 2; i++) {
  const k = +input[i];
  if (water[find(k)] > 0) {
    console.log(1);
  } else {
    console.log(0);
  }
}