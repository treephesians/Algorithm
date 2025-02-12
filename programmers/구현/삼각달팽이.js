function solution(n) {
    var answer = Array.from({length : n}, (_, i) => Array(i + 1).fill(0));
    let num = 1, row = -1, col = 0;
    for (let i = 0; i < n; i++){
        for (let j = i; j < n; j++){
            if (i % 3 == 0) row++;
            else if (i % 3 == 1) col++;
            else { row--; col--; }
            answer[row][col] = num++;
        }
    }
    return answer.flat();
}

console.log(solution(4))
