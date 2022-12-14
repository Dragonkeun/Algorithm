# 10. 정수형(int)으로 변수를 선언하고, 변수에 정수값을 저장한 후 변수에 저장되어 있는 값을 그대로 출력해보자.
var = int(input())
print(var)

# 11. 문자형(char)으로 변수를 하나 선언하고, 변수에 문자를 저장한 후 변수에 저장되어 있는 문자를 그대로 출력해보자.
# Tip::input()의 반환값은 기본으로 문자열로 정의된다.
var = input()
print(var)

# 12. 실수형(float)로 변수를 선언하고 그 변수에 실수값을 저장한 후 저장되어 있는 실수값을 출력해보자.
var = float(input())
print(var)

# 13. 정수(int) 2개를 입력받아 그대로 출력해보자. (단, 띄어쓰기를 기준으로 입력한다.)
# Tip::문자열의 메소드(함수)인 split()을 이용하면 문자열을 공백 기준으로 배열(iterable)로 만들어준다.
# 매핑함수인 map()을 이용하면 배열(iterable)의 모든 원소를 첫 번째 매개변수(parameter)로 변환할 수 있다.
# 정확히는 감싸준다는 표현이 맞다.
# 예) map(int, ['1', '2', '3']) >> [1,2,3]
# 매핑함수 map()의 반환값은 map객체이다. 따라서 육안으로 확인하기 위해서는 list()로 변환시켜줘야한다.
var = list(map(int, input().split()))
print(var[0], var[1])

# 14. 2개의 문자(ASCII CODE)를 입력받아서 순서를 바꿔 출력해보자.
var = input().split()
print(var[1], var[0])

# 15. 실수(float) 1개를 입력받아 저장한 후, 저장되어 있는 값을 소수점 셋 째 자리에서 반올림하여 소수점 이하 둘 째 자리까지 출력하시오.
var = round(float(input()), 2)
print(var)