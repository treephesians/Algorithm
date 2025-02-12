function solution(n, t, m, p) {
    var answer = '';
    for (let i = 0; i <= m * t; i++) {
        now = i.toString(n).toUpperCase() + '';
        for (let j = 0; j <= now.length - 1; j++) {
            answer += now[j]
        }
    }
    num = 0, start = 0;
    result = '';
    while (num < t){
        if (start % m == p - 1) {
            result += answer[start];
            num++;
        }
        start++;
    }
    return result;
}

console.log(solution(16, 16, 2, 2))