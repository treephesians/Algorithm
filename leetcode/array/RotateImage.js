/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    const len = matrix.length;

    for (let r = 0; r < len; r++) {
        for (let c = r + 1; c < len; c ++) {
            [matrix[r][c], matrix[c][r]] = [matrix[c][r], matrix[r][c]];
        }
    }

    for (let r = 0; r < len; r++) {
        matrix[r].reverse();
    }

};


// Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
// Output: [[7,4,1],[8,5,2],[9,6,3]]
const matrix = [[1,2,3],[4,5,6],[7,8,9]];
rotate(matrix);