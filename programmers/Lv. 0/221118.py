# 피자 나눠 먹기 (3)
# 머쓱이네 피자가게는 피자를 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다.
# 피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때,
# n명의 사람이 최소 한 조각 이상 피자를 먹으려면 최소 몇 판의 피자를 시켜야 하는지를
# return 하도록 solution 함수를 완성해보세요.
def solution(slice, n):
    answer = n // slice
    if (n % slice > 0):
        answer += 1
    return answer

# 편지
# 머쓱이는 할머니께 생신 축하 편지를 쓰려고 합니다.
# 할머니가 보시기 편하도록 글자 한 자 한 자를 가로 2cm 크기로 적으려고 하며,
# 편지를 가로로만 적을 때, 축하 문구 message를 적기 위해
# 필요한 편지지의 최소 가로길이를 return 하도록 solution 함수를 완성해주세요.
def solution(message):
    answer = len(message)*2
    return answer

# 배열 두배 만들기
# 정수 배열 numbers가 매개변수로 주어집니다.
# numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.
def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i*2)
    return answer