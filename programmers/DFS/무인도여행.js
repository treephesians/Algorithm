function find_max_days(matrix, visited, stack, row, col){
    let max_days = 0;
    while (stack.length > 0) {
        const [r, c] = stack.pop();
        if (visited[r][c]) continue;
        max_days += parseInt(matrix[r][c], 10);
        visited[r][c] = true;
        dr = [0, 0, 1, -1];
        dc = [1, -1, 0, 0];
        for (let i = 0; i < 4; i++){
            nr = r + dr[i];
            nc = c + dc[i];
            if (0 <= nr && nr < row && 0 <= nc && nc < col && matrix[nr][nc] != 'X' && !visited[nr][nc])
                stack.push([nr, nc]);
        }
    }
    return max_days;
}

function solution(maps) {
    var answer = [];

    const row = maps.length;
    const col = maps[0].length;
    const matrix = [];

    for (let i = 0; i < row; i++) matrix.push(maps[i].split(""));
    const visited = Array.from(Array(row), () => Array(col).fill(false));

    for (let r = 0; r < row; r++){
        for (let c = 0; c < col; c++){
            if (matrix[r][c] == 'X') continue;
            if (visited[r][c] == false) {
                const stack = [[r, c]];
                const max_days = find_max_days(matrix, visited, stack, row, col);
                answer.push(max_days);
            }
        }
    }
    answer.sort((a, b) => a - b);
    if (answer.length == 0) answer = [-1];
    return answer;
}

const maps = ["XXX","XXX","XXX"];
console.log(solution(maps));