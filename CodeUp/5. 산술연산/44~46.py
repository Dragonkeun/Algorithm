# 44. 정수를 1개 입력받아 1만큼 더해 출력해보자.
a = int(input())
print(a+1)

# 45. 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
# 첫 줄에 합  
# 둘째 줄에 차,  
# 셋째 줄에 곱,  
# 넷째 줄에 몫,   
# 다섯째 줄에 나머지,  
# 여섯째 줄에 나눈 값을 순서대로 출력한다.  
# (실수, 소수점 이하 셋째 자리에서 반올림해 둘째 자리까지 출력)
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b) # /쓰면 나머지까지 계산해줌 3/2=1.5, //쓰면 정수값만 계산해줌 3//2=1
print(a%b)
print(round(a/b, 2)) # /로 쓰면 나머지까지 싹 다 계산

# 46. 정수 3개를 입력받아 합과 평균을 출력해보자.
# 합과 평균을 줄을 바꿔 출력한다.
# 평균은 소수점 이하 둘째 자리에서 반올림해서 소수점 이하 첫째 자리까지 출력한다.
a, b, c = map(int, input().split())
print((a+b+c)/3)
