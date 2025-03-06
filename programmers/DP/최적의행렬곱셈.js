function solution(matrix_sizes) {
    var answer = 0;
    const l = matrix_sizes.length;
    const dp = Array.from({length: l}, ()=>Array(l).fill(Infinity));

    for (let i = 0; i < l; i++) dp[i][i] = 0;

    for (let length = 2; length <= l; length++){
        for (let start = 0; start <= l - length; start++){
            let end = start + length - 1;
            for (let i = start; i < end; i++){
                const cost = dp[start][i] + dp[i + 1][end] + matrix_sizes[start][0] * matrix_sizes[i][1] * matrix_sizes[end][1];
                dp[start][end] = Math.min(dp[start][end], cost);
            }
        }
    }
    return dp[0][l - 1];
}

matrix_sizes = [[5,3],[3,10],[10,6]];
console.log(solution(matrix_sizes));