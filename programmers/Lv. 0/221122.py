# 배열 자르기
def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]
    return answer

# 삼각형의 완성조건 (1)
def solution(sides):
    sides.sort(reverse=True)
    if sides[0] < sides[1]+sides[2]:
        answer = 1
    else :
        answer = 2
    return answer

# 최댓값 만들기 (1)
def solution(numbers):
    numbers.sort(reverse=True)
    answer = numbers[0] * numbers[1]
    return answer