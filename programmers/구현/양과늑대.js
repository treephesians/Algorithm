function solution(info, edges) {
    const size = info.length;
    const matrix = Array.from({length : size}, ()=>[]);

    for (const [from, to] of edges) matrix[from].push(to);

    let max_sheep = 0;

    function dfs(sheep, wolf, visited){
        if (sheep <= wolf) return;
        max_sheep = Math.max(max_sheep, sheep);
        
        for (let i = 0; i < visited.length; i++){
            const now = visited[i];
            const new_visited = [...visited];
            new_visited.splice(i, 1);
            new_visited.push(...matrix[now]);
            dfs(sheep + (info[now] == 0 ? 1 : 0), wolf + (info[now] == 1 ? 1 : 0), new_visited);
        }
    }

    dfs(1, 0, [...matrix[0]]);

    return max_sheep;
}

const info = [0,0,1,1,1,0,1,0,1,0,1,1];
const edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]];
console.log(solution(info, edges));