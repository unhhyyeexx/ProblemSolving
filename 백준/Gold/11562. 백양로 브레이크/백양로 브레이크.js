const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].split(" ").map(Number);
const graph = Array.from({ length: n + 1 }, () => Array(n + 1).fill(Infinity));

for (let i = 1; i < m + 1; i++) {
  [u, v, b] = input[i].trim().split(" ").map(Number);

  if (b === 1) {
    graph[v][u] = 0;
    graph[u][v] = 0;
  } else {
    graph[v][u] = 1;
    graph[u][v] = 0;
  }
}

function floyd() {
  for (let k = 1; k < n + 1; k++) {
    for (let i = 1; i < n + 1; i++) {
      for (let j = 1; j < n + 1; j++) {
        if (graph[i][j] > graph[i][k] + graph[k][j]) {
          graph[i][j] = graph[i][k] + graph[k][j];
        }
      }
    }
  }

  for (let i = 0; i < n + 1; i++) {
    graph[i][i] = 0;
  }
}

function solution() {
  floyd();
  const k = +input[m + 1];
  for (let i = m + 2; i < m + k + 2; i++) {
    const [s, e] = input[i].split(" ").map(Number);
    console.log(graph[s][e]);
  }
}

solution();
