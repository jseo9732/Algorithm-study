function solution(n) {
  var answer = 0;
  for (let i = 2; i < 1000000; i++) {
    if (n % i === 1) {
      answer = i;
      //   console.log(answer);
      return answer;
    }
  }
}
