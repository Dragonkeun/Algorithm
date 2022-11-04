# 짝수의 합
# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.
def solution(n):
    answer = 0
    for i in range(n+1):
        if i % 2 == 0:
            answer = answer + i
    return answer

# 배열의 평균값
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.
def solution(numbers):
    answer = sum(numbers) / len(numbers)
    return answer