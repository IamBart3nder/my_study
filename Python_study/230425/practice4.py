#1
# 다음 함수를 정의하세요.
# 정수 n을 입력받고, n보다 작은 수 중 3의 배수와
# 5의 배수를 모두 더한 합을 반환하는 함수
# 함수 이름 : sum_3_5



# def sum_3_5(n):
#     i = 1
#     for a in range(3, n, 3):
#         a * i
#         i += 1 
#     # print(a)      
#     for b in range(5, n, 5):
#         b * i
#         i += 1
#     # print(b) 
#     c = a + b
#     return print(c)

# sum_3_5(15)


# def sum_3_5(n):
#     result = 0
#     for i in range(n):
#         if i % 3 == 0 or i % 5 == 5:
#             result += i
#     return result


# def sum_3_5(n):
#     result = 0
#     for i in range(n):
#         if i % 3 == 0 
#             result += i
#         elif i % 5 == 0:
#             result += i
#     return result



# print(sum_3_5(15))

#2
# 정육면체 주사위 2개가 있다.
# 2개의 주사위를 던졌을 때 
# 나올 수 있는 주사위 눈의 조합을 모두 프린트 하는 함수를 정의하세요.
# 함수 이름 draw_dice
# 출력 예시 
# 1, 2 
# 6, 3

#2
# def double_dice():
#     for i in range(1, 7):
#         for j in range(1, 7):
#             print(i, j)

# double_dice()

# def double_dice():
#     a = 1
#     b = 1
#     while a < 7:
#         while b < 7:
#             print(a , b)
#             b += 1
#         a += 1
        
# double_dice()


#3 
# 두 수의 차이를 구하는 함수
# 함수에 입력된 두 정수의 차이를 계산하고 반환하는 함수를 정의하세요
# 함수 이름 : get_diff


# def get_diff(a, b):
#     result = (abs(a) - abs(b))
#     if a > b:
#         result = a - b
#     else:
#         b - a
#     print(result)
#     return result 

# get_diff(100, 2)



#4
# 가장 큰 수를 만드는 함수
# 함수에 입력된 5개 정수를 사용하여 만들 수 있는 
# 가장 큰 수를 반환하는 함수를 정의하세요
# 함수 이름 : get_biggest

#4 pro
# def get_biggest(a, b, c, d, e):
#     li = [a, b, c, d, e]
#     li.sort()
#     result = 0
#     for i in range(len(li)): # 0 ~ 4
#         result += li[i] * (10 ** i)
#     return result

# print(get_biggest(1, 7,3, 4,5))

#4 pro 2
# def get_biggest(a, b, c, d, e):
#     li = [a, b, c, d, e]
#     li.sort(reverse=True)
#     result = ""
#     for i in li:
#         result += str(i)
#     return int(result)

# print(get_biggest(1,7,3,4,5))

#5
# 별 찍기 2
# 정수를 함수에 입력하여 호출하면
# 해당 정수 줄의 별을 화면에 출력한다
# 함수 이름 : print_stars2
'''
출력 결과
n -> 1
   *
n -> 4
   *
  **
 ***
****
'''

# #5 me
# def print_stars2(n):
#     for a in range(n+1):
#         print(n * " " ,a * "*")
#         n -= 1
# print_stars2(7)


#5 pro
# def print_stars2(n):
#     for i in range(1, n+1):
#         print((n - i) * " ", "*" * i)

# print_stars2(7)

