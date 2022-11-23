# 배열 원소의 길이
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer

# 특정 문자 제거하기
def solution(my_string, letter):
    answer = my_string.replace(letter, '')
    return answer

# 아이스 아메리카노
def solution(money):
    answer = []
    answer.append(money//5500)
    answer.append(money%5500)
    return answer