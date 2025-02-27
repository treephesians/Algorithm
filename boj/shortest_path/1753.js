const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

// 5 6
// 1
// 5 1 1
// 1 2 2
// 1 3 3
// 2 3 4
// 2 4 5
// 3 4 6

class MinHeap {
    constructor(){
        this.heap = [];
    }
    getParent(n){
        return Math.floor((n - 1) / 2);
    }
    getRightChild(n){
        return 2 * n + 1;
    }
    getLeftChild(n){
        return 2 * n + 2;
    }
    swap(a, b){
        [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
    }
    push(node){
        this.heap.push(node);
        this.heapifyUp();
    }
    heapifyUp(){
        let pos = this.heap.length - 1;
        while (pos > 0 && this.heap[pos].weight < this.heap[this.getParent(pos)].weight){
            const parent = this.getParent(pos);
            this.swap(pos, parent);
            pos = parent;
        }
    }
    pop(){
        if (this.heap.length == 0) return null;
        if (this.heap.length == 1) return this.heap.pop();
        const root = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.heapifyDown();
        return root;
    }
    heapifyDown(){
        let root = 0;
        const size = this.heap.length;
        while (this.getLeftChild(root) < size) {
            let minValue = this.getLeftChild(root);
            if (this.getRightChild(root) < size && this.heap[this.getLeftChild(root)].weight > this.heap[this.getRightChild(root)].weight){
                minValue = this.getRightChild(root);
            }
            if (this.heap[minValue].weight > this.heap[root].weight) break;
            else this.swap(root, minValue);
            root = minValue;
        }
    }
    isEmpty(){
        return this.heap.length === 0;
    }
}

let index = 0;
const [V, E] = input[index++].split(" ").map(Number);
const K = parseInt(input[index++]);
const matrix = Array.from(Array(V + 1), () => []);
const arr = Array(V + 1).fill(Infinity);
arr[K] = 0;
const heap = new MinHeap();
heap.push({vertex:K, weight:0});

for (let i = 0; i < E; i++){
    const [u, v, w] = input[index++].split(" ").map(Number);
    const node = {vertex:v, weight:w};
    matrix[u].push(node);
}

while(!heap.isEmpty()){
    const now = heap.pop();
    for (node of matrix[now.vertex]) {
        const w = now.weight + node.weight;
        if (arr[node.vertex] > w){
            arr[node.vertex] = w;
            heap.push({vertex:node.vertex, weight:w});
        }
    }
}

for (let i = 1; i < V + 1; i++){
    if (arr[i] == Infinity) console.log("INF");
    else console.log(arr[i]);
}
