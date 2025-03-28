const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, v, e] = input[0].trim().split(" ").map(Number);
const [A, B] = input[1].trim().split(" ").map(Number);
const home = input[2].trim().split(" ").map(Number);
const graph = Array.from({ length: v + 1 }, () => []);
for (let i = 3; i < 3 + e; i++) {
  const [a, b, l] = input[i].trim().split(" ").map(Number);
  graph[a].push([b, l]);
  graph[b].push([a, l]);
}

const distance = Array.from({ length: v + 1 }, () => [Infinity, Infinity]);

function dijkstra(start, idx, distance) {
  distance[start][idx] = 0;
  const heap = [];
  heap.push([0, start]);
  while (heap.length > 0) {
    const [dist, now] = heap.shift();
    if (distance[now][idx] < dist) continue;
    for (const x of graph[now]) {
      const cost = x[1] + dist;
      if (distance[x[0]][idx] > cost) {
        distance[x[0]][idx] = cost;
        heap.push([cost, x[0]]);
      }
    }
  }
}

dijkstra(A, 0, distance);
dijkstra(B, 1, distance);

let answer = 0;
for (const i of home) {
  if (distance[i][0] === Infinity) {
    distance[i][0] = -1;
  }
  if (distance[i][1] === Infinity) {
    distance[i][1] = -1;
  }
  answer += distance[i][0] + distance[i][1];
}

console.log(answer);
