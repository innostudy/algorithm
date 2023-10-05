/**
과일 장수가 사과 상자를 포장하고 있습니다. 사과는 상태에 따라 1점부터 k점까지의 점수로 분류하며, k점이 최상품의 사과이고 1점이 최하품의 사과입니다. 사과 한 상자의 가격은 다음과 같이 결정됩니다.

한 상자에 사과를 m개씩 담아 포장합니다.
상자에 담긴 사과 중 가장 낮은 점수가 p (1 ≤ p ≤ k)점인 경우, 사과 한 상자의 가격은 p * m 입니다.
과일 장수가 가능한 많은 사과를 팔았을 때, 얻을 수 있는 최대 이익을 계산하고자 합니다.(사과는 상자 단위로만 판매하며, 남는 사과는 버립니다)

예를 들어, k = 3, m = 4, 사과 7개의 점수가 [1, 2, 3, 1, 2, 3, 1]이라면, 다음과 같이 [2, 3, 2, 3]으로 구성된 사과 상자 1개를 만들어 판매하여 최대 이익을 얻을 수 있습니다.

(최저 사과 점수) x (한 상자에 담긴 사과 개수) x (상자의 개수) = 2 x 4 x 1 = 8
사과의 최대 점수 k, 한 상자에 들어가는 사과의 수 m, 사과들의 점수 score가 주어졌을 때, 과일 장수가 얻을 수 있는 최대 이익을 return하는 solution 함수를 완성해주세요.

제한사항
3 ≤ k ≤ 9
3 ≤ m ≤ 10
7 ≤ score의 길이 ≤ 1,000,000
1 ≤ score[i] ≤ k
이익이 발생하지 않는 경우에는 0을 return 해주세요.
 */

function solution(k, m, score) {
  let answer = 0;
  //분류된 사과 상자가 담길 이중배열의 첫 껍데기
  const groupedApples = [];
  //가장 큰 수를 포함하여 자르기 위해 score배열을 재정렬
  const arrangedScoreArr = score.sort((a, b) => b - a);
  //m개씩 담은 상자가 여러개 나올 수 있기 때문에 반복문 안에서 배열을 여러 개 만들 수 있어야 함(이중배열)
  for (let i = 0; i < arrangedScoreArr.length; i += m) {
    //이중배열 안쪽 배열 제작
    const innerArr = arrangedScoreArr.slice(i, i + m);
    //안쪽 배열의 길이가 m과 같은 경우에만 grouping해줌
    if (innerArr.length === m) {
      groupedApples.push(innerArr);
    } else {
      //여기 return으로 하면 오류. 근데 왜 그렇게 되는지를 모르겠음. 
      continue;
    }
  }
  //배열 안에서 각 배열들의 최솟값을 m과 곱하고 모든 값을 더해 최종 가격을 구할 것.
  groupedApples.map(groupedApple => {
    answer += groupedApple[groupedApple.length - 1] * m;
  })

  return answer;
}