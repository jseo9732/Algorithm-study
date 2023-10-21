function solution(numbers) {
  var answer = '';

  numbers.sort(
    (a, b) =>
      Number(b.toString() + a.toString()) - Number(a.toString() + b.toString())
  );
  numbers.map(number => (answer += number.toString()));
  if (answer[0] === '0') {
    answer = '0';
  }
  console.log(answer);
  return answer;
}

solution([0, 0, 0, 0, 0]);
