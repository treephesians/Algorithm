function solution(targets) {
    targets.sort((a, b) => a[1] - b[1]);

    let answer = 0;
    let last_shot = -Infinity;

    for (const [s, e] of targets) {
        if (last_shot <= s) {
            last_shot = e - 1e-9;
            answer++;
        }
    }

    return answer;
}

const targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]];
console.log(solution(targets));