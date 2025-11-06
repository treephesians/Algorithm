/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let start = 0, end = height.length - 1;
    let max_amount = 0;
    while (start < end) {
        h = Math.min(height[start], height[end]);
        max_amount = Math.max(max_amount, (end - start) * h);
        if (height[start] < height[end]) start++;
        else end--;
    }
    return max_amount;
};