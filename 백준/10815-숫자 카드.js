const fs = require('fs');
const input = fs.readFileSync('dev/stdin').toString().split('\n');

const N = Number(input[0]);
const haveCard = input[1].split(' ').map(Number);
// const M = Number(input[2]);
const qCard = input[3].split(' ').map(Number);

let answers = [];
haveCard.sort((a, b) => a - b);

for (const e of qCard) {
  let start = 0;
  let end = N - 1;
  let answer = 0;

  while (start <= end) {
    let mid = parseInt((start + end) / 2);
    if (e === haveCard[mid]) {
      answer = 1;
    }
    if (e < haveCard[mid]) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  answers.push(answer);
}

console.log(answers.join(' '));
