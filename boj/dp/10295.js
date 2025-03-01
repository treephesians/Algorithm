const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

class Queue {
    constructor(){
        this.start = 0;
        this.end = 0;
        this.arr = [];
    }
    size(){
        return this.end - this.start;
    }
    push(n){
        this.arr.push(n);
        this.end++;
    }
    pop(){
        const result = this.arr[this.start];
        this.start++;
        return result;
    }
}

function find_high_point(heightArr, row, col){
    let high_point;
    let high_height = -1;
    for (let r = 0; r < row; r++){
        for (let c = 0; c < col; c++){
            if (heightArr[r][c] > high_height){
                high_point = {row: r, col: c};
                high_height = heightArr[r][c];
            }
        }
    }
    return high_point;
}

function calculate_cost(heightArr, costArr, high_point, queue, row, col){
    while (queue.size() > 0) {
        const [r, c] = queue.pop();
        const current_cost = costArr[r][c];
        const dr = [0, 1, 0, -1, 1, 1, -1, -1];
        const dc = [1, 0, -1, 0, 1, -1, 1, -1];
        for (let i = 0; i < 8; i++){
            const [nr, nc] = [r + dr[i], c + dc[i]];
            if (0 <= nr && nr < row && 0 <= nc && nc < col){
                if (heightArr[nr][nc] != NaN){
                    const diff_height = Math.abs(heightArr[nr][nc] - heightArr[r][c]);
                    const cost = (diff_height + 1) * (diff_height + 1);
                    if (cost + current_cost < costArr[nr][nc]){
                        costArr[nr][nc] = cost + current_cost;
                        queue.push([nr, nc]);
                    }
                }
            }
        }
    }
    return costArr[high_point.row][high_point.col];
}

let index = 0;
const T = parseInt(input[index++]);

for (let t = 0; t < T; t++){
    const [row, col] = input[index++].split(" ").map(Number);
    const heightArr = Array.from(Array(row), ()=>[]);
    for (let r = 0; r < row; r++){
        heightArr[r] = input[index++].split("").map(Number);
    }
    const costArr = Array.from(Array(row), () => Array(col).fill(Infinity));
    const [sr, sc] = input[index++].split(" ").map(Number);
    costArr[sr][sc] = 0;
    const queue = new Queue();
    queue.push([sr, sc]);

    const high_point = find_high_point(heightArr, row, col);
    let answer = calculate_cost(heightArr, costArr, high_point, queue, row, col);
    if (answer == Infinity) answer = "NO";
    console.log(answer);
}
