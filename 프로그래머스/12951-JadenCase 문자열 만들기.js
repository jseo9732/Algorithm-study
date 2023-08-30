function solution(s) {
  var answer = '';
  upper = true;
  for (let i = 0; i < s.length; i++) {
    if (upper) {
      answer += s[i].toUpperCase();
      upper = false;
    } else {
      answer += s[i].toLowerCase();
    }
    if (s[i] === ' ') {
      upper = true;
    }
  }
  console.log(answer);
  return answer;
}

solution('for the last week');
