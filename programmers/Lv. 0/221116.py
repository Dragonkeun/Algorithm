# 피자 나눠 먹기 (1)
# 머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 주어질 때,
# 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.
def solution(n):
    answer = n // 7
    if (n % 7) >= 1 and (n % 7) <= 6:
        answer += 1
    return answer

# 배열 뒤집기
# 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다.
# num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    answer = []
    for i in reversed(num_list):
        answer.append(i)
    return answer

# 문자열 뒤집기
# 문자열 my_string이 매개변수로 주어집니다.
# my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(my_string):
    answer = my_string[::-1]
    return answer
