# 배열의 유사도
def solution(s1, s2):
    answer = 0
    for i in s1:
        for n in s2:
            if i==n:
                answer+=1
    return answer

# 짝수는 싫어요
def solution(n):
    answer = []
    for i in range(n+1):
        if i%2==1:
            answer.append(i)
    return answer

# 옷가게 할인 받기
import math
def solution(price):
    if price >= 500000:
        answer = price * 0.8
    elif price >= 300000:
        answer = price * 0.9
    elif price >= 100000:
        answer = price * 0.95
    else :
        answer = price
    answer = math.trunc(answer)
    return answer
