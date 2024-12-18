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

const [n, m, a, b, c] = input[0].trim().split(" ").map(Number);
const graph = Array.from({ length: n + 1 }, () => []);
const costs = [];
for (let i = 1; i < m + 1; i++) {
  const [x, y, z] = input[i].trim().split(" ").map(Number);
  costs.push(z);
  graph[x].push([y, z]);
  graph[y].push([x, z]);
}

function dijkstra(start) {
  const heap = new Heap();
  heap.push([0, a]);
  const distance = Array(n + 1).fill(Infinity);
  distance[a] = 0;
  while (!heap.isEmpty()) {
    const [cost, node] = heap.pop();
    // 최단경로를 확인. 이미 이번 노드로 가는 비용이 누적 비용보다 적다면 갱신하지 않음.
    if (distance[node] < cost) {
      continue;
    }
    for ([nextN, nextC] of graph[node]) {
      const total = cost + nextC;
      if (distance[nextN] > total && nextC <= start) {
        distance[nextN] = total;
        heap.push([total, nextN]);
      }
    }
  }
  return distance[b] <= c;
}

function solution() {
  costs.sort((a, b) => a - b);

  let totalMin = Infinity;
  let left = 0;
  let right = costs.length - 1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);

    if (dijkstra(costs[mid])) {
      right = mid - 1;
      totalMin = Math.min(totalMin, costs[mid]);
    } else {
      left = mid + 1;
    }
  }

  console.log(totalMin === Infinity ? -1 : totalMin);
}

solution();
