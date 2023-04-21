# 2 ~ 9 사이의 숫자를 입력받아
# 해당하는 단의 구구단을 출력하세요
# 2 ~ 9 사이의 숫자가 아닌 값이 입력된 경우,
# 잘못 입력되었다고 출력하고 다시 입력받으세요

#me
# while True:
#     print("구구단 계산식")
#     a = int(input("숫자를 입력하세요: "))  
#     n = 1 
#     if a > 1 and a < 10:    
#         print(a,"단")
#         while n < 10:
#             print(a, "*", n , "=", n*a)
#             n += 1
#     else:
#         print("수치가 잘못되었습니다.")


#pro 1
n = int(input("몇 단?"))
while not 2 <= n <= 9:
    print("2 ~ 9 사이의 숫자를 입력해주세요.")
    n = int(input("몇 단?"))
for i in range(1,10):
    print(n, "*", i, "=", n*i)

# 또는 
# # for i in range(9): # 대신 식을 조금 바꿔줘야함.
    # print(n, "*", (i+1), "=", n*(i+1))
