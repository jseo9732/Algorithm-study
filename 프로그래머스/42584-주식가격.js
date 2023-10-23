function solution(prices) {
  let answer = [];
  let pricesLen = prices.length;
  for (let i = 0; i < pricesLen; i++) {
    for (let j = i + 1; j < pricesLen; j++) {
      //   console.log('i: ', i, 'j: ', j);
      //   console.log('prices[i]: ', prices[i], 'prices[j]: ', prices[j]);

      if (prices[i] > prices[j]) {
        answer.push(j - i);
        break;
      }
      if (j === pricesLen - 1) {
        answer.push(pricesLen - 1 - i);
      }
      //   console.log(answer);
    }
  }
  answer.push(0);
  return answer;
}

solution([1, 2, 3, 2, 3]);
