const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

class Heap {
  constructor() {
    this.heap = [];
  }

  isEmpty() {
    return this.heap.length === 0;
  }

  swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }

  push(value) {
    this.heap.push(value);
    let currentIdx = this.heap.length - 1;
    let parentIdx = Math.floor((currentIdx - 1) / 2);

    while (
      this.heap[parentIdx] &&
      this.heap[parentIdx][0] > this.heap[currentIdx][0]
    ) {
      this.swap(currentIdx, parentIdx);
      currentIdx = parentIdx;
      parentIdx = Math.floor((currentIdx - 1) / 2);
    }
  }

  pop() {
    if (this.heap.length === 1) {
      return this.heap.pop();
    }

    const returnValue = this.heap[0];
    this.heap[0] = this.heap.pop();

    let currentIdx = 0;
    let leftIdx = currentIdx * 2 + 1;
    let rightIdx = currentIdx * 2 + 2;

    while (
      (this.heap[leftIdx] &&
        this.heap[leftIdx][0] < this.heap[currentIdx][0]) ||
      (this.heap[rightIdx] && this.heap[rightIdx][0] < this.heap[currentIdx][0])
    ) {
      let smallerIdx = leftIdx;
      if (
        this.heap[rightIdx] &&
        this.heap[rightIdx][0] < this.heap[smallerIdx][0]
      ) {
        smallerIdx = rightIdx;
      }

      this.swap(currentIdx, smallerIdx);
      currentIdx = smallerIdx;
      leftIdx = currentIdx * 2 + 1;
      rightIdx = currentIdx * 2 + 2;
    }
    return returnValue;
  }
}

const [v, e, p] = input[0].trim().split(" ").map(Number);
const graph = Array.from({ length: v + 1 }, () => []);
for (let i = 1; i < e + 1; i++) {
  const [a, b, c] = input[i].trim().split(" ").map(Number);
  graph[a].push([b, c]);
  graph[b].push([a, c]);
}

function dijkstra(start) {
  const heap = new Heap();
  heap.push([0, start]);
  const distance = Array(v + 1).fill(100000000);
  distance[start] = 0;
  while (!heap.isEmpty()) {
    const [cost, node] = heap.pop();
    for ([nextN, nextC] of graph[node]) {
      const total = cost + nextC;
      if (distance[nextN] > total) {
        distance[nextN] = total;
        heap.push([total, nextN]);
      }
    }
  }
  return distance;
}

if (dijkstra(1)[v] === dijkstra(1)[p] + dijkstra(p)[v]) {
  console.log("SAVE HIM");
} else {
  console.log("GOOD BYE");
}
