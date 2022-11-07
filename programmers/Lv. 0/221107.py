# 머쓱이보다 키 큰 사람
# 머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다.
# 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때,
# 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.
# height : 머쓱이의 키, array : 반 친구들의 키
def solution(array, height):
    answer = 0
    for i in array:
        if height < i :
            answer += 1
    return answer

# 양꼬치
# 머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다.
# 양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다. 정수 n과 k가 매개변수로 주어졌을 때,
# 양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.
def solution(n, k):
    answer = 0
    answer += (n * 12000)
    answer += (k * 2000)
    service = n // 10
    answer -= (service * 2000)
    return answer

# 두 수의 나눗셈
# 정수 num1과 num2가 매개변수로 주어질 때,
# num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 soltuion 함수를 완성해주세요.
def solution(num1, num2):
    answer = int(num1 / num2 * 1000)
    return answer

# 중복된 숫자 개수
# 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때,
# array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.
def solution(array, n):
    answer = 0
    for i in array:
        if i == n :
            answer += 1
    return answer

# 짝수 홀수 개수
# 정수가 담긴 리스트 num_list가 주어질 때,
# num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(num_list):
    odd = 0 #홀수
    even = 0 #짝수
    for i in num_list:
        if i % 2 == 1:
            odd += 1
        if i % 2 == 0:
            even += 1 
    answer = [even, odd]
    return answer