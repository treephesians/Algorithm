var reverse = function(x) {
    const INT_MIN = -Math.pow(2, 31);
    const INT_MAX = Math.pow(2, 31) - 1;

    let isMinus = x < 0;
    x = Math.abs(x);

    let answer = parseInt(x.toString().split("").reverse().join(""));
    if (isMinus) answer *= -1;

    // 🔥 여기서 결과값 범위 검사 추가
    if (answer < INT_MIN || answer > INT_MAX) return 0;

    return answer;
};