const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

class MaxHeap {
    constructor(){
        this.heap = [];
    }
    getParent(n){
        return Math.floor((n - 1) / 2);
    }
    getLeftChild(n){
        return 2 * n + 1;
    }
    getRightChild(n){
        return 2 * n + 2;
    }
    swap(a, b){
        [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
    }
    push(value){
        this.heap.push(value);
        this.heapifyUp();
    }
    heapifyUp(){
        let index = this.heap.length - 1;
        while (index > 0 && this.heap[this.getParent(index)] < this.heap[index]){
            const parentIndex = this.getParent(index);
            this.swap(index, parentIndex);
            index = parentIndex;
        }
    }
    pop(){
        const size = this.heap.length;
        if (size == 0) return 0;
        if (size == 1) return this.heap.pop();
        const root = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.heapifyDown();
        return root;
    }
    heapifyDown() {
        let index = 0;
        while (this.getLeftChild(index) < this.heap.length) {
            let biggerIndex = this.getLeftChild(index);

            if (this.getRightChild(index) < this.heap.length &&
                this.heap[this.getRightChild(index)] > this.heap[this.getLeftChild(index)]) {
                biggerIndex = this.getRightChild(index);
            }

            if (this.heap[biggerIndex] <= this.heap[index]) break;
            this.swap(index, biggerIndex);
            index = biggerIndex; // 🔥 여기서 바로 갱신하여 추가적인 비교 방지
        }
    }
}

let index = 0;
const N = parseInt(input[index++]);
const MH = new MaxHeap();
const result = [];

for (let i = 0; i < N; i++){
    const n = parseInt(input[index++]);
    if (n == 0) 
        result.push(MH.pop());
    else
        MH.push(n);
}

console.log(result.join("\n"));
