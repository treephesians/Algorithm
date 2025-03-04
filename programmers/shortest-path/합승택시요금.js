function solution(n, s, a, b, fares) {
    const matrix = Array.from({length: n}, () => Array(n).fill(Infinity));
    for (const [a, b, fare] of fares){
        matrix[a - 1][b - 1] = fare;
        matrix[b - 1][a - 1] = fare;
    }
    for (let i = 0; i < n; i++) matrix[i][i] = 0;
    for (let k = 0; k < n; k++){
        for (let i = 0; i < n; i++){
            for (let j = 0; j < n; j++){
                matrix[i][j] = Math.min(matrix[i][j], matrix[i][k] + matrix[k][j]);
            }
        }
    }

    let result = Infinity;
    for (let i = 0; i < n; i++){
        result = Math.min(result, matrix[s - 1][i] + matrix[i][a - 1] + matrix[i][b - 1]);
    }
    
    return result;
}

const n = 6; // 지점 개수
const s = 4; // 출발지점
const a = 5; // A 도착지점
const b = 6; // B 도착지점
const fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]];

console.log(solution(n, s, a, b, fares));