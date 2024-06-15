const fs = require("fs");
const input = fs.readFileSync("/dev/stdin");
let parsedInput = input.toString().split("\n");
let [N, M] = parsedInput[0].split(" ").map((elem) => parseInt(elem));

let maze = [];

for (let i = 1; i <= N; i++) {
    maze.push(parsedInput[i].split("").map((x) => parseInt(x)));
}

const d_ij = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
];

function bfs(init_i, init_j) {
    const q = [];
    const visit = Array.from(Array(N), () => Array(M).fill(0));

    visit[0][0] = 1;
    q.push([init_i, init_j]);
    while (q.length) {
        let [i, j] = q.shift();
        if (i === N - 1 && j === M - 1) {
            return visit[i][j];
        }
        for (let [di, dj] of d_ij) {
            let [ni, nj] = [i + di, j + dj];
            if (
                0 <= ni &&
                ni < N &&
                0 <= nj &&
                nj < M &&
                visit[ni][nj] === 0 &&
                maze[ni][nj] === 1
            ) {
                visit[ni][nj] = visit[i][j] + 1;
                q.push([ni, nj]);
            }
        }
    }
}

console.log(bfs(0, 0));
