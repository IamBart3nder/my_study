# # while
# # 반복문
# '''
# while 조건:
#     반복할 코드
#     '''
# # 조건이 참인 경우에 코드를 계속 반복

# # n = 1
# # while n <= 100:
# #     print(n)  
# #     n += 1 # n = n+1

# # += 연산자
# # 더하기 연산 후 할당
# # n += 1은 n+1과 같음 
# # -=
# # *=
# # /=
# # **=
# # //=
# # % =

# # s1 = 안녕
# # s2 += 하세요
# # so

# # 10부터  1까지 순서대로

# # x = 10
# # while x > 0: 
# #     print(x)
# #     x -= 1

# # money = 10000
# # price = 1000
# # coffee = 5
# # while money >= price:
# #     print("커피를 구매했습니다.")
# #     money -= price
# #     coffee -= 1
# #     print("남은 커피 :", coffee)
# #     if coffee == 0:
# #         break

# # break
# # 반복문을 즉시 종료한다.

# # 1부터 10까지 홀수만 출력한다

# x = 1
# while x <= 10:
#     if x % 2 == 1:
#         print(x)
#     x += 1

# continue
# 반복문의 제일 처음으로 돌아감
#

# b = 0
# while b < 10:
#     b += 1
#     if b % 2 == 0:
#         continue
#     print(b)


# 무한 반복문
# 무한 루프
# 조건식에 True를 입력해
# 항상 참이 되도록 하여 무한히 반복하게 함.
# crtl + c 를 터미널에

# while True:
#     user_input = input("종료하려면 1을 입력 하세요")    
#     if user_input == "1":
#         break


# 무한반복문으로 계산기 만들기
# +, -, *, /

while True:
    print("""
    계산기
    =========
    1. 더하기 (+)
    2. 빼기 (-)
    3. 곱하기 (*)
    4, 나누기 (/)
    """)
    operator = input("계산을 선택하세요 : ")
    if operator == "1":
        print("1 + 2 = ", 1 + 2)
 
    if operator == "2":
        print("1 - 2 = ", 1 - 2)
 
    if operator == "3":
        print("1 * 2 = ", 1 * 2)
 
    if operator == "4":
        print("1 / 2 = ", 1 / 2)