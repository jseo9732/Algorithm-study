const fs = require('fs');
const input = fs.readFileSync('dev/stdin').toString().split('\n');

const N = Number(input[0]);
const graph = [];
const answer = [];
for (let i = 1; i <= N; i++) {
  graph.push(input[i].split(' ').map(Number));
  answer.push(new Array(N).fill(0));
}

const dfs = (node, start, visited) => {
  for (let i = 0; i < N; i++) {
    if (graph[node][i] && !visited[i]) {
      visited[i] = true;
      answer[start][i] = 1;
      dfs(i, start, visited);
    }
  }
};

for (let i = 0; i < N; i++) {
  const visited = new Array(N).fill(false);
  dfs(i, i, visited);
}

console.log(answer.map(x => x.join(' ')).join('\n'));
