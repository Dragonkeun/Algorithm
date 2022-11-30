# # 68. 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
# score = int(input())
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# else:
#     grade = "F"

# # 69. 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.
# rating = input()
# if rating=="A":
#     print("best")
# elif rating=="B":
#     print("good")
# else:
#     print("so so")

# 70. 월이 입력될 때 계절 이름이 출력되도록 해보자.
month = int(input())
if month == 12 or month == 1 or month == 2:
    print("winter")
elif month >= 3 and month <= 5:
    print("spring")
elif month >= 6 and month <= 9:
    print("summer")
else:
    print("autumn")