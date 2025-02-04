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
    parent = this.parentIndex(index);
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
