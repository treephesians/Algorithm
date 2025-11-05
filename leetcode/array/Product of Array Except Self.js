/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    // 이건 0을 처리하는 것이 문제인 것 같다.
    // 0이 1개, 1개 초과일 때 처리하는 것이 중요할 것 같다.
    let nZero = 0;
    let product = 1;
    const arr = Array(nums.length).fill(0);

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) nZero++;
        else product *= nums[i];
    }
    if (nZero > 1) return arr;
    if (nZero === 1) {
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] === 0) {
                arr[i] = product;
                return arr;
            }
        }
    }
    for (let i = 0; i < nums.length; i++) {
        arr[i] = product / nums[i];
    }
    return arr;
};