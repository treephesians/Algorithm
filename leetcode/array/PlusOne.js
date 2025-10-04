/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    const len = digits.length;
    digits[len - 1] += 1;
    for (let i = len - 1; i > 0; i--) {
        if (digits[i] >= 10) {
            digits[i - 1] += 1;
            digits[i] -= 10;
        }
    }
    if (digits[0] >= 10) {
        digits[0] -= 10;
        digits.unshift(1);
    }
    return digits;
};

console.log(plusOne([6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]));