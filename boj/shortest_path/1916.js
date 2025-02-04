class MinHeap {
  constructor() {
    this.heap = [];
  }
  parentIndex(i) {
    return Math.floor((i - 1) / 2);
  }
  leftChildIndex(i) {
    return i * 2 + 1;
  }
  rightChildIndex(i) {
    return i * 2 + 2;
  }
  swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }
  push(value) {
    this.heap.push(value);
    this.heapifyUp();
  }
  heapifyUp() {
    let index = this.heap.length - 1;
    const parent = this.parentIndex(index);
    while (index > 0 && this.heap[parent].cost > this.heap[index].cost) {
      this.swap(index, parent);
      index = parent;
    }
  }
  pop() {
    const length = this.heap.length;
    if (length == 0) return null;
    if (length == 1) return this.heap.pop();
    const root = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.heapifyDown();
    return root;
  }
  heapifyDown() {
    let index = 0;
    while (this.leftChildIndex(index) < this.heap.length) {
      let smallerIndex = this.leftChildIndex(index);
      if (
        this.rightChildIndex(index) < this.heap.length &&
        this.heap[this.rightChildIndex(index)].cost <
          this.heap[this.leftChildIndex(index).cost]
      ) {
        smallerIndex = this.rightChildIndex(index);
      }
      if (this.heap[smallerIndex].cost >= this.heap[index]) {
        break;
      } else {
        this.swap(index, smallerIndex);
      }
      index = smallerIndex;
    }
  }
  isEmpty() {
    return this.heap.length === 0;
  }
}

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
//const input = fs.readFileSync("../input.txt").toString().trim().split("\n");

const n = parseInt(input[0]); // 도시의 개수
const m = parseInt(input[1]); // 버스의 개수

// 그래프 초기화 (인접 리스트)
const graph = Array.from({ length: n + 1 }, () => []);

// 버스 정보 입력
for (let i = 2; i < m + 2; i++) {
  const [start, end, cost] = input[i].split(" ").map(Number);
  graph[start].push({ node: end, cost: cost });
}

// 출발점과 도착점
const [startCity, endCity] = input[m + 2].split(" ").map(Number);

function dijkstra(startCity) {
  const distances = Array(n + 1).fill(Infinity);
  distances[startCity] = 0;

  const heap = new MinHeap();
  heap.push({ node: startCity, cost: 0 });

  while (!heap.isEmpty()) {
    const { node: current, cost: currentCost } = heap.pop();

    if (currentCost > distances[current]) continue;

    for (const { node: nextNode, cost: nextCost } of graph[current]) {
      const newCost = currentCost + nextCost;

      if (newCost < distances[nextNode]) {
        distances[nextNode] = newCost;
        heap.push({ node: nextNode, cost: newCost });
      }
    }
  }

  return distances;
}

console.log(dijkstra(startCity)[endCity]);
