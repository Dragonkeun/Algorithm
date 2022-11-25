# 65. 세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.
# a, b, c = map(int, input().split())
# if a%2 == 1:
#     print(a)
# if b%2 == 1:
#     print(b)
# if c%2 == 1:
#     print(c)

# 66. 세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
a, b, c = map(int, input().split())
if a % 2 == 0 :
    print("짝수")
else:
    print("홀수")

if b % 2 == 0 :
    print("짝수")
else:
    print("홀수")

if c % 2 == 0 :
    print("짝수")
else:
    print("홀수")

