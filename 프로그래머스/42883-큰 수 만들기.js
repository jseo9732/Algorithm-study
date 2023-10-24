function solution(number, k) {
  let arr = [number[0]];
  let answer = '';
  for (let i = 1; i < number.length; i++) {
    let nextValue = Number(number[i]);
    while (k > 0 && Number(arr[arr.length - 1]) < nextValue) {
      arr.pop();
      k--;
    }
    arr.push(nextValue);
  }
  for (let i = 0; i < k; i++) {
    arr.pop();
  }
  answer = arr.join('');
  // console.log(answer);
  return answer;
}

solution('98765', 1);
