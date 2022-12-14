# 53. 1(true, 참) 또는 0(false, 거짓) 이 입력되었을 때 반대로 출력하는 프로그램을 작성해보자.
# **참고**
# 파이썬에서 비교/관계 연산(==, !=, >, <, >=, <=)이 수행될 때,
# 0은 거짓(false)으로 인식되고, 0이 아닌 모든 수는 참(true)으로 인식된다.
# 참 또는 거짓의 논리값을 역(반대)으로 바꾸기 위해서는
# 논리(logical)연산자 'not'를 사용할 수 있다.
# 이러한 논리연산을 NOT 연산이라고 부른다.
# 참, 거짓의 논리값(boolean value)인 불 값을 다루어주는 논리연산자는
# 'not', 'and', 'or'가 있다.
# ** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로
# 참/거짓만 가지는 논리값과 그 연산을 다룬다.
a = int(input())
print(not a)

# 54. 두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 참일 때에만 참을 출력하는 프로그램을 작성해보자.
a, b = map(int, input().split())
if a and b :
    print("참")

# 55. 두 개의 참(1) 또는 거짓(0)이 입력될 때, 하나라도 참이면 참을 출력하는 프로그램을 작성해보자.
a, b = map(int, input().split())
if a or b :
    print("참")

# Bonus. 1개의 정수형 입력이 들어오면 논리 연산을 이용하여 '홀수'와 '짝수'를 판별하여라
n = int(input())
if n % 2 == 0:
    print("짝수")
elif n % 2 == 1:
    print("홀수")
