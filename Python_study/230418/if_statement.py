# if
'''if 조건:
    실행하려는 코드
    코드 2
    코드 3
코드 4''' #다른 코드
# if문은 조건이 True(참)일 때만 안쪽 코드블럭을 실행

'''else: 
    실행하려는 코드'''
# else는 조건이 False(거짓)일 때만 안쪽 코드블럭을 실행

'''if 조건1:
    조건1이 True(참)일 때 실행
elif 조건2:
    조건1은 False, 조건2는 True일 때 실행, 
    elif의 조건이 옳다면 else까지 넘어가지 않는다.
else:
    조건 1 False 조건2 False일 때 실행'''

# 코드 블럭 (들여쓰기로 코드 구분)

# bool [불린형 변수] (True, False)
# = 대입 연산자, 할당 연산자 

# number1 = 6
# number2 = 6
# if number1 > number2:
#     print(number1 > number2)
#     print("number1이 더 크다")
# elif number1 == number2:
#     print(number1 == number2)
#     print("같다")
# else:
#     print(number1 > number2)
#     print("number2가 더 크다")

# 비교 연산자(a, b는 변수)
# a > b 
# a >= b 
# a < b
# a <= b
# a == b   a와 b가 같다
# a != b   a와 b가 같지 않다

# print(2 > 3) #F
# print(2 >= 3) #F
# print(2 < 3) #T
# print(2 <= 3) #T
# print(2 == 3) #F
# print(2 != 3) #T

# 문자 비교 연산
# # 문자는 사전 순서에서 먼저 오는게 작음.
# print("a" < "b") # T
# print("CAT" < "DOG") # T
# print("COW" > "CAT") # T

# #  대문자가 먼저 오기 때문에 작게 취급.
# print("DOG" == "dog") # F 
# print("DOG" > "dog") # F

# 논리 연산자, Bool(불) 연산자 (True, False에 적용)
# and  a and b
# - a, b가 모두 트루일 경우에만 True, 아니면 False
# or   a or b
# - a와 b 중 하나라도 True면 True, 하나라도 False면 False
# not  not a
# - True <-> False 값을 반대로 바꿈.
# 항이 하나이기에 단항 연산자.

# print(True and True)   # T
# print(True and False)  # F
# print(False and True)  # F
# print(False and False) # F

# print(True or True)    # T
# print(True or False)   # T
# print(False or True)   # T
# print(False or False)  # F

# print(not True)  #F
# print(not False) #T

# age = 17
# money = 10000
# # if age >= 20 and money >= 10000:
# #     print("성인이고 부자입니다.")
# # if age >= 20 or money >= 10000:
# #     print("성인 또는 부자입니다.")


# # 0과 1.
# if "안녕":
#     print("안녕하세요") # 값이 있으면 True
# if 0:
#     print(0) # 값이 없으니 False 

