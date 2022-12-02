# 직각삼각형 출력하기
n = int(input())
for i in range(1, n+1):
    print('*'*i)

# 대문자와 소문자
def solution(my_string):
    answer = ''
    for i in my_string:
        if i.islower():
            answer += i.upper()
        elif i.isupper():
            answer += i.lower()
    return answer

# 주사위의 개수
def solution(box, n):
    answer = 1
    for i in box:
        answer *= i // n
    return answer

# 가장 큰 수 찾기
def solution(array):
    answer = []
    n = []
    for i in array:
        n.append(i)
    array.sort(reverse=True)
    answer.append(array[0])
    answer.append(n.index(array[0]))
    return answer
# 가장 큰 수 찾기 두번째 방법
def solution(array):
    answer = []
    answer.append(max(array))
    answer.append(array.index(max(array)))
    return answer

# 약수 구하기
def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)
    return answer

    # 암호 해독
def solution(cipher, code):
    cipher = list(cipher)
    answer = ''
    for i in range(len(cipher)):
        if (i+1) % code == 0:
            answer += cipher[i]
    return answer