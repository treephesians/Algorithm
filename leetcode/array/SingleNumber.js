/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    const map = new Map();
    for (const num of nums) {
        if (map.has(num)) map.set(num, map.get(num) + 1);
        else map.set(num, 1);
    }

    let answer = null;
    map.forEach((value, key) => {
        if (value === 1) answer = key;
    })
    return answer;
};

console.log(singleNumber([2,2,1]));