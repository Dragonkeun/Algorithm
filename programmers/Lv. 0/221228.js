// 2차원으로 만들기
function solution(num_list, n) {
    let answer = [];
    let a = [];
    for(let i=0; i<num_list.length; i++){
        a.push(num_list[i])
        if (a.length == n){
            answer.push(a);
            a = [];
        }
    }
    return answer;
}