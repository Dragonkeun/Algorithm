// 가까운 수
function solution(array, n) {
    let answer = [];
    for(let i=0; i<array.length; i++){
        answer.push(Math.abs(array[i] - n));
    }
    array.sort(function(a, b) {
      if(a > b) return 1;
      if(a === b) return 0;
      if(a < b) return -1;
    });
    for (let j=0; j<array.length; j++){
        if (Math.abs(array[j] - n) == Math.min(...answer)) {
            return array[j];
        }
    }
}