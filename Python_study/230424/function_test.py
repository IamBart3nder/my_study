#1
# 홀수 판별 함수
# 정수 1개를 입력받고 홀수인지 
# 판별하는 함수 
# 함수 이름 : is_odd_number
# 파라미터 : n
# 반환값 : 홀수면 True,
#         짝수면 False


# def is_odd_number(n):
#     if n % 2 == 0:
#         False
#         return print("False")        
#     else:
#         True
#         return print("True")


# is_odd_number(5)

# #pro 1
# def is_odd_number(n):
#     if n % 2 == 0:
#         return False
#     else:
#         return True

# is_odd_number(5)

# #pro 2
# def is_odd_number(n):
#     if n % 2 == 0:
#         return False
#     return True


# # pro 3 
# def is_odd_number(n):
#     return n % 2 == 1    
# # 어차피 조건이 참이면 True, 거짓이면 False 일 것.


#######################################################


#2 
# 테두리를 출력하는 함수
# 문자열을 입력받고 print
# 함수를 이용해 테두리와
# 함께 문자를 출력한다.
# 함수 이름 : get_bordered_str
# 파라미터 : message
# 반환값 : Non
# print 예시
'''
*****
hello
*****
'''


#2 me
# def get_bordered_str(message):
#     print("*****")
#     print(message)
#     print("*****")
#     # return None

# get_bordered_str('hello')    

#2 pro
# def get_bordered_str(message):
#     n = len(message)
#     print("*" * n)
#     print(message)
#     print("*" * n)
    
# get_bordered_str("global") 

# #2-2
# def get_bordered_str(message):
#     n = len(str(message))
#     print("*" * n)
#     print(message)
#     print("*" * n)
    
# get_bordered_str(12345) 

# len 함수는 int 타입에 사용할 수 없음

#2-2 pro

# def get_bordered_str(message):
#     message = str(message)
#     n = len(message)
#     print("*" * n)
#     print(message)
#     print("*" * n)
    
# get_bordered_str(12345) 



#3
# 속도를 변환하는 함수
# m/s 단위의 속도가 입력되면
# km/h 단위의 속도로 변환한다.
# 함수 이름 : convert_velocity
# 파라미터 : velocity
# 반환값 : km/h로 변환된 속도

# def convert_velocity(velocity):
#     result = velocity * 3.6
#     return result

# convert_velocity(10)


#4
# 별 찍기 함수
# 정수를 함수에 입력하여
# 호출하면 해당 정수 줄의
# 별을 화면에 출력한다.
# n -> 출력 결과
# 함수 이름 : print_stars
# 파라미터 : n
# 반환값 : none 
"""
*
**
***
****
"""

#4 me
# def print_stars(n):
#     for a in range(0 , n + 1):
#         print(a * '*')
#         a += 1 # 필요없는 코드

# print_stars(10)


# #4 pro 1 
# def print_stars(n):
#     for i in range(n): # 0 ~ n-1
#         for j in range(i+1): # 0 ~ i
#             print("*", end ="")
#         print()
        
# print_stars(4)

# end = '값'
# 줄 바꿈

#4 pro 2
# def print_stars(n):
#     for a in range(0 , n + 1):
#         print(a * '*')

# print_stars(4)

#4 pro 3
# def print_stars(n):
#     i=0
#     while i < n:
#         j = 0
#         while j < i:
#             print("*", end="")
#             j += 1
#         print()
#         i += 1

# print_stars(6)