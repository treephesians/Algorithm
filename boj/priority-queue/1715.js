const fs = require("fs")
const input = fs.readFileSync("boj/input.txt").toString().trim().split("\n");

class MinHeap {
    constructor(){
        this.heap = [];
    }
    getParent(index){
        return Math.floor((index - 1) / 2);
    }
    getLeftChild(index){
        return index * 2 + 1;
    }
    getRightChild(index){
        return index * 2 + 2;
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
        while(index > 0 && this.heap[this.getParent(index)] > this.heap[index]){
            const parent = this.getParent(index);
            this.swap(index, parent);
            index = parent;
        }
    }
    pop(){
        const length = this.heap.length;
        if (length == 0) return null;
        if (length == 1) return this.heap.pop();
        const root = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.heapifyDown();
        return root;
    }
    heapifyDown(){
        let index = 0;
        while (this.getLeftChild(index) < this.heap.length){
            let smallerIndex = this.getLeftChild(index);
            if (this.getRightChild(index) < this.heap.length && this.heap[this.getRightChild(index)] < this.heap[this.getLeftChild(index)]){
                smallerIndex = this.getRightChild(index);
            }
            if (this.heap[smallerIndex] > this.heap[index]) break;
            else this.swap(index, smallerIndex);
            index = smallerIndex;
        }
    }
}

let index = 0;
const N = parseInt(input[index++]);
const arr = new MinHeap();

for (let i = 0; i < N; i++){
    const size = parseInt(input[index++]);
    arr.push(size);
}

let answer = 0;

while(arr.heap.length > 1){
    const first = arr.pop();
    const second = arr.pop();
    arr.push(first + second);
    answer += (first + second);
}

console.log(answer);