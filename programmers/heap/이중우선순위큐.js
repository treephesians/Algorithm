class MinHeap {
    constructor() {
        this.heap = [];
    }
    getParentIndex(n) {
        return Math.floor((n - 1) / 2);
    }
    getLeftIndex(n) {
        return 2 * n + 1;
    }
    getRightIndex(n) {
        return 2 * n + 2;
    }
    swap(a, b) {
        [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
    }
    push(n) {
        this.heap.push(n);
        this.heapifyUp();
    }
    heapifyUp() {
        let index = this.heap.length - 1;
        while (index > 0 && this.heap[this.getParentIndex(index)] > this.heap[index]) {
            const parentIndex = this.getParentIndex(index);
            this.swap(index, parentIndex);
            index = parentIndex;
        }
    }
    pop() {
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop();
        const root = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.heapifyDown();
        return root;
    }
    heapifyDown() {
        let index = 0;
        while (this.getLeftIndex(index) < this.heap.length) {
            let smallerIndex = this.getLeftIndex(index);
            if (
                this.getRightIndex(index) < this.heap.length &&
                this.heap[this.getRightIndex(index)] < this.heap[smallerIndex]
            ) {
                smallerIndex = this.getRightIndex(index);
            }
            if (this.heap[smallerIndex] >= this.heap[index]) break;
            this.swap(index, smallerIndex);
            index = smallerIndex;
        }
    }
    isEmpty() {
        return this.heap.length === 0;
    }
    peek() {
        return this.heap.length > 0 ? this.heap[0] : null;
    }
}

function solution(operations) {
    const minHeap = new MinHeap();
    const maxHeap = new MinHeap(); // 최대 힙을 만들기 위해 음수 값으로 저장
    const entryMap = new Map(); // 실제 삽입된 값의 개수 관리

    for (const operation of operations) {
        const [action, value] = operation.split(" ");
        const number = parseInt(value, 10);

        if (action === "I") {
            minHeap.push(number);
            maxHeap.push(-number); // 최대 힙을 위한 음수 값 저장
            entryMap.set(number, (entryMap.get(number) || 0) + 1);
        } else {
            if (entryMap.size === 0) continue; // 큐가 비어있으면 무시

            if (number === 1) {
                // 최댓값 삭제
                while (!maxHeap.isEmpty()) {
                    const maxVal = -maxHeap.pop();
                    if (entryMap.has(maxVal)) {
                        if (entryMap.get(maxVal) === 1) entryMap.delete(maxVal);
                        else entryMap.set(maxVal, entryMap.get(maxVal) - 1);
                        break;
                    }
                }
            } else {
                // 최솟값 삭제
                while (!minHeap.isEmpty()) {
                    const minVal = minHeap.pop();
                    if (entryMap.has(minVal)) {
                        if (entryMap.get(minVal) === 1) entryMap.delete(minVal);
                        else entryMap.set(minVal, entryMap.get(minVal) - 1);
                        break;
                    }
                }
            }
        }
    }

    if (entryMap.size === 0) return [0, 0];

    let maxVal, minVal;
    while (!maxHeap.isEmpty()) {
        maxVal = -maxHeap.pop();
        if (entryMap.has(maxVal)) break;
    }
    while (!minHeap.isEmpty()) {
        minVal = minHeap.pop();
        if (entryMap.has(minVal)) break;
    }

    return [maxVal, minVal];
}