function solution(want, number, discount) {
  let answer = 0;
  for (let i = 0; i + 10 <= discount.length; i++) {
    const arr = discount.slice(i, i + 10);
    let allCount = 0;
    for (let j = 0; j < want.length; j++) {
      let count = 0;
      for (const i of arr) {
        if (want[j] === i) {
          count++;
        }
      }
      if (!(number[j] === count)) {
        // console.log('안맞음');
        break;
      }
      allCount += count;
    }
    if (allCount === 10) {
      answer++;
    }
    // console.log('allCount: ', allCount);
    // console.log('-----------');
  }
  // console.log(answer);
  return answer;
}

solution(
  ['banana', 'apple', 'rice', 'pork', 'pot'],
  [3, 2, 2, 2, 1],
  [
    'chicken',
    'apple',
    'apple',
    'banana',
    'rice',
    'apple',
    'pork',
    'banana',
    'pork',
    'rice',
    'pot',
    'banana',
    'apple',
    'banana',
  ]
);
