function solution(land) {
    const row_len = land.length;
    const col_len = land[0].length;
    const next = [[1,0], [-1,0], [0,1], [0,-1]];
    const visited = Array.from({length: row_len}, () => Array(col_len).fill(false));
    const col_sums = Array(col_len).fill(0);
    let block_id = 0;

    for (let row = 0; row < row_len; row++) {
        for (let col = 0; col < col_len; col++) {
            if (land[row][col] === 1 && !visited[row][col]) {
                let count = 0;
                const q = [[row, col]];
                const remember = [];
                const cols_in_block = new Set();
                visited[row][col] = true;

                while (q.length) {
                    const [r, c] = q.shift();
                    remember.push([r, c]);
                    count++;
                    cols_in_block.add(c);

                    for (const [dr, dc] of next) {
                        const nr = r + dr, nc = c + dc;
                        if (nr>=0 && nr<row_len && nc>=0 && nc<col_len && land[nr][nc]===1 && !visited[nr][nc]) {
                            visited[nr][nc] = true;
                            q.push([nr, nc]);
                        }
                    }
                }

                // 블록이 등장한 열에 count 더하기
                for (const c of cols_in_block) {
                    col_sums[c] += count;
                }

                block_id++;
            }
        }
    }

    // 이제 max_count는 col_sums에서 최대값
    return Math.max(...col_sums);
}