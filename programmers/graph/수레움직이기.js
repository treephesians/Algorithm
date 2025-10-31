function solution(maze) {
  const n = maze.length, m = maze[0].length;
  const dirs = [[1,0], [-1,0], [0,1], [0,-1]];

  let redStart, blueStart, redEnd, blueEnd;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (maze[i][j] === 1) redStart = [i, j];
      if (maze[i][j] === 2) blueStart = [i, j];
      if (maze[i][j] === 3) redEnd = [i, j];
      if (maze[i][j] === 4) blueEnd = [i, j];
    }
  }

  const bit = (r, c) => 1 << (r * m + c);
  const inRange = (r, c) => r >= 0 && c >= 0 && r < n && c < m;

  const start = {
    r1: redStart[0], c1: redStart[1],
    r2: blueStart[0], c2: blueStart[1],
    redMask: bit(redStart[0], redStart[1]),
    blueMask: bit(blueStart[0], blueStart[1]),
    turn: 0,
  };

  const visited = new Set();
  const q = [start];

  while (q.length) {
    const { r1, c1, r2, c2, redMask, blueMask, turn } = q.shift();

    if (r1 === redEnd[0] && c1 === redEnd[1] &&
        r2 === blueEnd[0] && c2 === blueEnd[1]) {
      return turn;
    }

    const key = `${r1},${c1},${r2},${c2},${redMask},${blueMask}`;
    if (visited.has(key)) continue;
    visited.add(key);

    for (const [dr1, dc1] of dirs) {
      for (const [dr2, dc2] of dirs) {
        let nr1 = r1 + dr1, nc1 = c1 + dc1;
        let nr2 = r2 + dr2, nc2 = c2 + dc2;

        const redFixed = (r1 === redEnd[0] && c1 === redEnd[1]);
        const blueFixed = (r2 === blueEnd[0] && c2 === blueEnd[1]);

        // 도착한 수레는 고정(제자리)
        if (redFixed) [nr1, nc1] = [r1, c1];
        if (blueFixed) [nr2, nc2] = [r2, c2];

        // 범위 & 벽
        if (!inRange(nr1, nc1) || !inRange(nr2, nc2)) continue;
        if (maze[nr1][nc1] === 5 || maze[nr2][nc2] === 5) continue;

        // 재방문 금지: '실제로 움직였을 때'만 금지
        if (!redFixed && (redMask & bit(nr1, nc1))) continue;
        if (!blueFixed && (blueMask & bit(nr2, nc2))) continue;

        // 같은 칸 금지
        if (nr1 === nr2 && nc1 === nc2) continue;

        // 자리 교환 금지
        if (nr1 === r2 && nc1 === c2 && nr2 === r1 && nc2 === c1) continue;

        q.push({
          r1: nr1, c1: nc1,
          r2: nr2, c2: nc2,
          redMask: redFixed ? redMask : (redMask | bit(nr1, nc1)),
          blueMask: blueFixed ? blueMask : (blueMask | bit(nr2, nc2)),
          turn: turn + 1,
        });
      }
    }
  }
  return 0;
}