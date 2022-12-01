# 모음 제거
def solution(my_string):
    answer = ""
    my_string = list(my_string)
    aeiou = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(my_string)):
        for j in range(len(aeiou)):
            if aeiou[j] in my_string:
                my_string.remove(aeiou[j])
    answer = ''.join(my_string)
    return answer
# 모음 제거 두 번째 방법 replace
def solution(my_string):
    answer = ""
    aeiou = ['a', 'e', 'i', 'o', 'u']
    for i in aeiou:
        my_string = my_string.replace(i, '')
    answer = my_string
    return answer

# 숨어있는 숫자의 덧셈[1]
def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
            answer += int(i)
    return answer

# 개미 군단
def solution(hp):
    answer = 0
    ant = [5, 3, 1]
    for i in ant:
        answer += hp // i
        hp = hp % i
    return answer

# 세균 증식
def solution(n, t):
    answer = 0
    for _ in range(t):
        n *= 2
    answer = n        
    return answer

# n의 배수 고르기
def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer

# 문자열 정렬하기[1]
def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    answer.sort()
    return answer