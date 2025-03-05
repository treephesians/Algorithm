function solution(n, s) {
    let answer = [];
    if (n > s) return [-1];
    while (s > 0){
        const m = Math.floor(s / n);
        answer.push(m);
        n--;
        s -= m;
    }
    return answer;
}

const n = 4;
const s = 18;

console.log(solution(n, s))