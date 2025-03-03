function solution(n) {
    const result = [];

    function generate(current, open, close) {
        // 기저 사례: `n` 쌍을 완성하면 결과에 추가
        if (current.length === 2 * n) {
            result.push(current);
            return;
        }

        // '(' 추가 가능 여부
        if (open < n) {
            generate(current + "(", open + 1, close);
        }

        // ')' 추가 가능 여부 (닫을 수 있는 경우만 추가)
        if (close < open) {
            generate(current + ")", open, close + 1);
        }
    }

    generate("", 0, 0); // 초기값: 빈 문자열, 열린 괄호 0개, 닫힌 괄호 0개
    return result.length; // 가능한 괄호 조합의 개수 반환
}

console.log(solution(4)); // 132