function solution(array, commands) {
  var answer = [];
  for (const x of commands) {
    newArr = array.slice(x[0] - 1, x[1]);
    newArr.sort((a, b) => a - b);
    answer.push(newArr[x[2] - 1]);
  }

  return answer;
}
