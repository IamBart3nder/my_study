# # for문 for 반복문
# # iterable 
# '''
# for 변수 in iterable:
#     반복할 코드
# '''
# li_1 = ["one", "two", "three"]
# for i in li_1:
#     print(i)
# # 첫 번째 요소부터 마지막 요소까지
# # 변수에 대입하면서 반복

# s1 = "hello"
# for i in s1:
#     print(i)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     print(number)

# numbers.reverse()
# for number in numbers:
#     print(number)

# range()
#숫자 range 객체를 만들어주는 함수
# range(끝 정수)
# 0 ~ 끝 정수 - 1
# range(시작, 끝)
# 시작 ~ 끝 - 1
# range(시작, 끝, 스텝)
# 시작 ~ 끝 - 1 까지인데 스텝만큼 차이나게

# for i in range(10): 
#     print(i) # 0 ~ 9


# for i in range(1, 11):
#     print(i)

# for i in range(1, 21, 2):
#     print(i)


#1 for문을 사용하여 2부터 30까지 출력하라
#2 for문을 사용하여 2부터 30까지의 숫자 중 짝수만 출력하라
#3 for문을 사용하여 10부터 1까지 출력하라

# #1
# for a in range(2, 31):
#     print(a)


#2    
# for b in range(2,31,2):
#     print(b)

# #2 pro 1
# for b in range(2,31):
#     if b % 2 == 1: #홀수
#         pass #아무것도 안하고 버림
#     else: # 짝수
#         print(b)

# #2 pro 2
# for b in range(2,31):
#     if b % 2 == 0: #짝수
#         print(b)
    

#3
# number = [1,2,3,4,5,6,7,8,9,10] 
# number.reverse()
# for c in number:
#     print(c)

# #3 pro 1
# for c in range(10, 0, -1):
#     print(c)

#3 pro 2
# for i in reversed(range(1,11)):
#     print(i)

#3 pro 3
# for i in range(1,11)[::-1]:
#     print(i)

# range (a, b, c)
# a는 값에 포함, b는 미포함, c는 음수 양수 다 가능.

# [::] 슬라이싱 [시작 인덱스:끝 인덱스:방향(음수면 역방향)]


# #
# money = 2000
# price = 1000
# coffee = 5

# #1
# for i in range(coffee): # 0 ~ 4
#     print("커피를 구매했습니다.")
#     money -= price # money = money - price
#     print("남은 커피 :",coffee - 1 - i)
#     print(money)
#     if money < price:
#         break




# #1
# for i in range(coffee): # 0 ~ 4
#     print("커피를 구매했습니다.")
#     money -= price # money = money - price
#     print("남은 커피 :", range(coffee - 1 - i))
#     print(money)


# #2
# for i in range(1, coffee + 1): # 1 ~ 5
#     print("커피를 구매했습니다.")
#     money -= price # money = money - price
#     print("남은 커피 :", coffee - i)
#     print(money) 


# #3
# for i in range(coffee):
#     coffee -= 1
#     print("커피를 구매했습니다.")
#     money -= price # money = money - price
#     print("남은 커피 :", coffee)
#     print(money)


# prices = [500, 700, 930]
# money = int(input("돈:"))

# for i in range(len(prices)):
#     price = prices[i]
#     print(money // prices)
#     print(money % prices)

# for price in prices:
#     print(money // price)
#     print(money % price)

#
# scores = []
# for i in range(5):
#     score = int(input("시험점수:"))
#     scores.append(score)

# 이중 for문 
# 안쪽 for문이 더 먼저 연산 됨.
for i in range(2, 10):# 2 ~ 9
    print(i, '단')
    for j in range(1, 10): # 1 ~ 9
        print(i, "*" , j, "=" , i*j)
    print("------------------")
