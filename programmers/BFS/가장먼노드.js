class Deque {
  constructor() {
    this.data = {};
    this.front = 0;
    this.rear = 0;
  }
  push(value) {
    this.data[this.rear] = value;
    this.rear++;
  }
  shift() {
    if (this.front == this.rear) return null;
    const value = this.data[this.front];
    delete this.data[this.front];
    this.front++;
    return value;
  }
  size() {
    return this.rear - this.front;
  }
}

function solution(n, edge) {
  var answer = 0;
  const matrix = Array.from({ length: n + 1 }, () => []);
  const visited = Array(n + 1).fill(false);
  const deque = new Deque();

  for (const [a, b] of edge) {
    matrix[a].push(b);
    matrix[b].push(a);
  }

  deque.push([1, 0]);
  max_length = 0;

  while (deque.size() > 0) {
    const [now, length] = deque.shift();
    if (!visited[now]) {
      visited[now] = true;
      if (length > max_length) {
        max_length = length;
        answer = 0;
      }
      answer++;
      for (const next of matrix[now]) {
        if (!visited[next]) {
          deque.push([next, length + 1]);
        }
      }
    }
  }

  return answer;
}

console.log(
  solution(6, [
    [3, 6],
    [4, 3],
    [3, 2],
    [1, 3],
    [1, 2],
    [2, 4],
    [5, 2],
  ])
);
