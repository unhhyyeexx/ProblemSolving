const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

function find(a, arr) {
  if (a !== arr[a]) {
    arr[a] = find(arr[a], arr);
  }

  return arr[a];
}

function union(a, b, arr) {
  a = find(a, arr);
  b = find(b, arr);

  if (a < b) {
    arr[b] = a;
  } else {
    arr[a] = b;
  }
}

function solution(n, graph) {
  const parent = [...Array(n)].map((x, i) => i);
  for (let i = 0; i < n; i++) {
    const [x1, y1, r1] = graph[i];
    for (let j = i + 1; j < n; j++) {
      const [x2, y2, r2] = graph[j];
      if (Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) <= r1 + r2) {
        union(i, j, parent);
      }
    }
  }
  const result = new Set();
  for (let i = 0; i < n; i++) {
    const num = find(i, parent);
    if (!result.has(num)) {
      result.add(num);
    }
  }

  console.log(result.size);
}

const t = +input[0];
let idx = 1;
while (idx < input.length) {
  const n = +input[idx];
  const graph = [];
  for (let i = idx + 1; i < idx + n + 1; i++) {
    graph.push(input[i].trim().split(" ").map(Number));
  }
  solution(n, graph);

  idx += n + 1;
}
