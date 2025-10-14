/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let l = nums.length;
    if (l == 1) return true;
    for (let i = l - 2; i >=0; i--) {
        if (i + nums[i] >= l - 1) {
            l = i + 1;
        } 
    }
    return l == 1;

};


