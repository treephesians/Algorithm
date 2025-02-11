function solution(n) {
    var answer = [[1,3]];

    for (let i = 0; i < n - 1; i++){
        new_answer = []
        for (let j = 0; j < answer.length; j++){
            let [from, to] = answer[j]
            if (from == 2) from = 3
            else if (from == 3) from = 2
            if (to == 2) to = 3
            else if (to == 3) to = 2
            new_answer.push([from, to])
        }
        new_answer.push([1, 3])
        for (let j = 0; j < answer.length; j++){
            let [from, to] = answer[j]
            if (from == 1) from = 2
            else if (from == 2) from = 1
            if (to == 1) to = 2
            else if (to == 2) to = 1
            new_answer.push([from, to])
        }
        answer = new_answer
    }
    

    return answer;
}

console.log(solution(4))