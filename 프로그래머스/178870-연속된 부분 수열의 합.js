// 시간 초과 (2중 for문 때문인 것 같음)

// function solution(sequence, k) {
//   var answer = [];
//   for (let i = 0; i < sequence.length; i++) {
//     let sum = 0;
//     for (let j = i; j < sequence.length; j++) {
//       // console.log('i: ', i, 'j: ', j);
//       sum += sequence[j];
//       if (sum === k) {
//         answer.push([i, j]);
//         // console.log('i: ', i, 'j: ', j, 'sum: ', sum);
//       } else if (sum > k) {
//         break;
//       }
//     }
//   }
//   // console.log(answer);
//   answer.sort((a, b) => {
//     let aLeng = a[0] - a[1];
//     let bLeng = b[0] - b[1];
//     if (aLeng === bLeng) {
//       return a[0] - b[0];
//     } else {
//       return bLeng - aLeng;
//     }
//   });
//   console.log(answer);
//   answer = answer[0];
//   console.log(answer);
//   return answer;
// }

// 블로그 참고
// https://velog.io/@fervor_dev/프로그래머스-연속된-부분-수열의-합-JS

function solution(sequence, k) {
  let left = 0;
  let right = 0;
  let sum = sequence[0];
  var answer = [];
  while (right < sequence.length) {
    if (sum < k) {
      // 합이 k 보다 작으면
      right++;
      sum += sequence[right];
    } else if (sum > k) {
      // 합이 k 보다 크면
      sum -= sequence[left];
      left++;
    } else {
      // 합이 k랑 같으면
      answer.push([left, right]);
      right++;
      sum += sequence[right];
    }
  }
  // console.log(answer);
  answer.sort((a, b) => {
    let aLeng = a[0] - a[1];
    let bLeng = b[0] - b[1];
    if (aLeng === bLeng) {
      return a[0] - b[0];
    } else {
      return bLeng - aLeng;
    }
  });
  // console.log(answer);
  answer = answer[0];
  // console.log(answer);
  return answer;
}

// solution([1, 2, 3, 4, 5], 7);
solution([1, 1, 1, 2, 3, 4, 5], 5);
// solution([2, 2, 2, 2, 2], 6);
