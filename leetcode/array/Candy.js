/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function(ratings) {
    const arr = Array(ratings.length).fill(1);
    // 왼쪽 -> 오른쪽
    for (let i = 1; i < ratings.length; i++) {
        if (ratings[i] > ratings[i - 1]) arr[i] = arr[i - 1] + 1; 
    }
    // 오른쪽 -> 왼쪽
    for (let i = ratings.length - 2; i >= 0; i--) {
        if (ratings[i] > ratings[i + 1]) arr[i] = Math.max(arr[i + 1] + 1, arr[i]); 
    }

    return arr.reduce((a, b) => a + b, 0);
};