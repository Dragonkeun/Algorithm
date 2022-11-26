# 문자 반복 출력하기
def solution(my_string, n):
    answer_list = []
    my_string = list(my_string)
    for i in range(len(my_string)):
            answer_list.append(my_string[i]*n)
    answer = ''.join(answer_list)
    return answer