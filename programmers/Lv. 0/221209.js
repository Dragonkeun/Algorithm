// 인덱스 바꾸기
function solution(my_string, num1, num2) {
    my_string = my_string.split("");
    var temp = my_string[num1];
    my_string[num1] = my_string[num2];
    my_string[num2] = temp;
    answer = my_string.join("");
    return answer;
}