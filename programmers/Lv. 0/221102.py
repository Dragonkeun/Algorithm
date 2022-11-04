# 나머지 구하기
# 정수 num1, num2가 매개변수로 주어질 때, num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.
def solution(num1, num2):
    answer = num1 % num2
    return answer

# 두 수의 곱
# 정수 num1, num2가 매개변수 주어집니다. num1과 num2를 곱한 값을 return 하도록 solution 함수를 완성해주세요.
def solution(num1, num2):
    answer = num1 * num2
    return answer

# 두 수의 차
# 정수 num1과 num2가 주어질 때, num1에서 num2를 뺀 값을 return하도록 soltuion 함수를 완성해주세요.
def solution(num1, num2):
    answer = num1 - num2
    return answer

# 몫 구하기
# 정수 num1, num2가 매개변수로 주어질 때, num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.
def solution(num1, num2):
    answer = num1 // num2
    return answer

# 두 수의 합
# 정수 num1과 num2가 주어질 때, num1과 num2의 합을 return하도록 soltuion 함수를 완성해주세요.
def solution(num1, num2):
    answer = num1 + num2
    return answer

# 숫자 비교하기
# 정수 num1과 num2가 매개변수로 주어집니다. 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.
def solution(num1, num2):
    if num1 == num2 :
        answer = 1
    else :
        answer = -1
    return answer

# 나이 출력
# 머쓱이는 40살인 선생님이 몇 년도에 태어났는지 궁금해졌습니다. 나이 age가 주어질 때, 2022년을 기준 출생 연도를 return 하는 solution 함수를 완성해주세요.
def solution(age):
    answer = 2022 - age + 1
    return answer

# 각도기
# 각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다.
# 각 angle이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를
# return하도록 solution 함수를 완성해주세요.
def solution(angle):
    if angle > 0 and angle < 90 :
        answer = 1
    elif angle == 90 :
        answer = 2
    elif angle > 90 and angle < 180 :
        answer = 3
    elif angle == 180 :
        answer = 4
    return answer
