/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    const len = height.length;
    const left_max_heights = Array(len).fill(0);
    const right_max_heights = Array(len).fill(0);

    let left_max_height = 0;
    for (let i = 0; i < len; i++) {
        left_max_height = Math.max(left_max_height, height[i]);
        left_max_heights[i] = left_max_height;
    }
    
    let right_max_height = 0;
    for (let i = len - 1; i >= 0; i--) {
        right_max_height = Math.max(right_max_height, height[i]);
        right_max_heights[i] = right_max_height;
    }
    
    let answer = 0;
    for (let i = 0; i < len; i++) {
        const max_height = Math.min(left_max_heights[i], right_max_heights[i]);
        answer += max_height - height[i];
    }

    return answer;
};