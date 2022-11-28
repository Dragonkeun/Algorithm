# 제곱수 판별하기
def solution(n):
    if (n**0.5) == int(n**0.5):
        answer = 1
    else:
        answer = 2
    return answer

# 문자열 안에 문자열
def solution(str1, str2):
    if str2 in str1:
        answer = 1
    else:
        answer = 2
    return answer

# 순서쌍의 개수
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n%i == 0 :
            answer += 1
    return answer

# 중앙값 구하기
def solution(array):
    array.sort(reverse=True)
    answer = array[len(array)//2]
    return answer