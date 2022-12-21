// 가까운 수 1. 가장 가까운 수가 여러개일 경우 더 작은 수를 return 하는 조건 불충족, 수정 필요
function solution(array, n) {
    let answer = 0;
    let result = 0;
    let top = Math.abs(array[0]-n);
    for(let i=0; i<array.length; i++){
        answer = Math.abs(array[i] - n);
        if (answer < top) {
            top = answer;
            result = array[i];
        }
    }
    return result;
}

//가까운 수 2. 요구 조건 불충족, 수정 필요
function solution(array, n) {
    let answer = [];
    let top = Math.abs(array[0]-n);
    for(let i=0; i<array.length; i++){
        answer.push(Math.abs(array[i] - n));
    }
    return array[array.indexOf(answer.sort()[0])];
}