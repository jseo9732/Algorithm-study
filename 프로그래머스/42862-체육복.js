function solution(n, lost, reserve) {
  let answer = n - lost.length;

  let lostArr = lost.sort((a, b) => a - b).filter((x) => !reserve.includes(x));
  let reserveArr = reserve
    .sort((a, b) => a - b)
    .filter((x) => !lost.includes(x));
  answer += lost.length - lostArr.length;

  lostArr.forEach((l) => {
    if (reserveArr.length === 0) {
      return;
    }

    if (reserveArr.includes(l - 1)) {
      reserveArr = reserveArr.filter((r) => r !== l - 1);
      answer++;
    } else if (reserveArr.includes(l + 1)) {
      reserveArr = reserveArr.filter((r) => r !== l + 1);
      answer++;
    }
  });

  return answer;
}

console.log(solution(5, [2, 4], [1, 3, 5]));
