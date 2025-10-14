/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = [];
    const map = {
        ')': '(',
        ']': '[',
        '}': '{',
    };

    for (let ch of s) {
        // 닫는 괄호일 때
        if (map[ch]) {
        const top = stack.pop();
        if (top !== map[ch]) return false;
        } 
        // 여는 괄호일 때
        else {
        stack.push(ch);
        }
    }

    return stack.length === 0;
};