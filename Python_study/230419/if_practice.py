#A : 91 ~ 100
#B : 81 ~ 90
#C : 71 ~ 80
#D : 61 ~ 70
#F : 60 이하

eng = int(input("영어점수: "))
kor = int(input("국어점수: "))
math = int(input("수학점수: "))
point = (eng + kor + math) / 3


print(point)

if point >= 91:
    print("A")
elif point >= 81:
    print("B")
elif point >= 71:
    print("C")
elif point >= 61:
    print("D")
elif point < 61:
    print("F")



# input() 함수
# 사용자로부터 정보를 입력 받는 함수

# user_input = input()
# print(user_input)

# 정수형 변환 함수
# int()
# integer형, 정수형, int형
# 소수점이 있는 숫자를 넣으면 소수점 아래를 버림