function solution(land) {
    let answer = 0;
    const max_row = land.length;
    const max_col = land[0].length;
    const visited = Array.from({length : max_row}, () => Array(max_col).fill(false));
    const new_land = Array.from({length : max_row}, () => Array(max_col).fill(0));
    const dirs = [[1,0], [0,1], [-1,0], [0,-1]];
    const inLand = (r, c) => 0 <= r && r < max_row && 0 <= c && c < max_col;
    let oil_id = 1;
    for (let r = 0; r < max_row; r++) {
        for (let c = 0; c < max_col; c++) {
            if (land[r][c] === 0 || visited[r][c]) continue;
            const stack = [[r, c]];
            while (stack.length) {
                const [cur_r, cur_c] = stack.pop();
                if (visited[cur_r][cur_c]) continue;
                visited[cur_r][cur_c] = true;
                new_land[cur_r][cur_c] = oil_id;
                for (const [dr, dc] of dirs) {
                    const next_r = cur_r + dr;
                    const next_c = cur_c + dc;
                    if (inLand(next_r, next_c) && !visited[next_r][next_c] && land[next_r][next_c] === 1) {
                        stack.push([next_r, next_c]);
                    }
                }
            }
            oil_id++;
        }
    }
    const oilArr = Array(oil_id).fill(0);
    
    for (let r = 0; r < max_row; r++) {
        for (let c = 0; c < max_col; c++) {
            if (new_land[r][c] === 0) continue;
            oilArr[new_land[r][c]]++;
        }
    }
    
    for (let c = 0; c < max_col; c++) {
        const set = new Set();
        for (let r = 0; r < max_row; r++) {
            if (new_land[r][c] === 0) continue;
            set.add(new_land[r][c]);
        }
        const arr = Array.from(set);
        let result = 0;
        for (const id of arr) {
            result += oilArr[id];
        }
        answer = Math.max(answer, result);
    }
    return answer;
}