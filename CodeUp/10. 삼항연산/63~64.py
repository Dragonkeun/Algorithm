# 63. 입력된 두 정수 a, b 중 큰 값을 출력하는 프로그램을 작성해보자.
# 단, 조건문을 사용하지 않고 3항 연산자 'and or' 를 사용한다.
a, b = map(int, input().split())
print(a>b and a or b)
# print(a if a > b else b) 3항연산자 예시

# 64. 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자. (단, 삼항 연산자 이용)
a, b, c = map(int, input().split())
big = a if a < b else b
print(big if big < c else c)

# Bonus. 1개의 정수형 입력이 들어오면 삼항 연산을 이용하여 '홀수'와 '짝수'를 판별하여라
a = int(input())
print("짝수" if a % 2 == 0 else "홀수")