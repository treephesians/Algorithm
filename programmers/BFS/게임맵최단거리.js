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
    if (this.front === this.rear) return null;
    const value = this.data[this.front];
    delete this.data[this.front];
    this.front++;
    return value;
  }

  size() {
    return this.rear - this.front;
  }
}

function solution(maps) {
  const row = maps.length;
  const col = maps[0].length;

  const queue = new Deque();
  queue.push([0, 0, 1]);

  const visited = Array.from(Array(row), () => Array(col).fill(false));
  visited[0][0] = true; // ✅ 시작 위치 방문 처리

  const directions = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
  ];

  while (queue.size() > 0) {
    // ✅ 무한 루프 방지
    const node = queue.shift();

    const [r, c, length] = node;

    if (r === row - 1 && c === col - 1) {
      return length;
    }

    for (const [dr, dc] of directions) {
      const nr = r + dr;
      const nc = c + dc;

      if (
        nr >= 0 &&
        nr < row &&
        nc >= 0 &&
        nc < col &&
        maps[nr][nc] === 1 &&
        !visited[nr][nc]
      ) {
        visited[nr][nc] = true; // ✅ 큐에 넣을 때 방문 처리
        queue.push([nr, nc, length + 1]);
      }
    }
  }

  return -1;
}
