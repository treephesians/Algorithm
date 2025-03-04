function solution(sales, links) {
    var answer = 0;
    const people_num = sales.length;
    const matrix = Array.from({length: people_num + 1}, () => []);

    for (const [from, to] of links) {
        matrix[from].push(to);
    }

    


    return answer;
}

const sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17];
const links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]];