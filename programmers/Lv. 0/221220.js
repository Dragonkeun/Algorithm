// A로 B 만들기
function solution(before, after) {
    if (before.split("").sort().join('') == after.split("").sort().join(''))
        return 1;
    else
        return 0;
}