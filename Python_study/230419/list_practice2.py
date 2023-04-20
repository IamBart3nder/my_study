# li_1 = ["Hello", "World", "Python"]
# li_2 = [1, 2, 3]

#1 li_1의 원소를 사용하여 'Hello World Python'을 완성

#2 li_1의 원소를 사용하여 'HelP'를 완성

#3 li_1과 li_2를 사용하여 
# ["Hello", "World", "python", 1, 2, 3] 을 완성

#4 li_1과 li_2를 사용하여  
# ["Hello", 1, "World", 2, "python", 3] 을 완성


#1
#me   print((li_1[0]),(li_1[1]),(li_1[2]))
#pro1 print(li_1[0],li_1[1],li_1[2])

# join(리스트)
# 리스트의 문자열을 합친다.

#pro2 print(" ".join(li_1))
# "a".join(리스트) ## a를 사이에 끼운 상태로 (문자열)을 합친다


#2
# print(li_1[0][:3] + li_1[2][0])


#3
#me print(li_1 + li_2)

#pro1
# li_1.extend(li_2)
# print(li_1)


#4
#me
# print(li_1[:1]+li_2[:1]
#       +li_1[1:2]+li_2[1:2]
#       +li_1[2:]+li_2[2:])

#pro1 
""" li_1.insert(1, li_2[0])
# li_1.insert(3, li_2[1])
# li_1.insert(5, li_2[2])
# # or li_1.append(li_2[2])
# print(li_1) """


#5

# 빈 리스트 만드는 법
# scores = []
# # scores = list()

# scores = []
# scores.append(int(input("영어 점수:")))
# scores.append(int(input("국어 점수:")))
# scores.append(int(input("수학 점수:")))

# # avg = (scores[0] + scores[1] + scores[2]) / 3

# # sum()
# # 리스트의 요소를 모두 더한다
# # 리스트에 문자가 있는 경우 에러가 생김

# avg = sum(scores) / 3

# print(avg)

# if avg >= 91:
#     print("A")
# elif avg >= 81:
#     print("B")
# elif avg >= 71:
#     print("C")
# elif avg >= 61:
#     print("D")
# elif avg < 61:
#     print("F")



#6 
# 나이와 가지고 있는 돈을 입력받는다.
# 가지고 있는 돈으로 물건을 
# 몇개 살 수 있는지와 잔돈을 출력한다.
# 물건의 가격은 500원이다.

#7
# 나이와 가지고 있는 돈을 입력받는다.
# 가지고 있는 돈으로 물건별로 각각 
# 몇개 살 수 있는지와 잔돈을 출력한다.
# 물건의 가격은 1번 물건 1000원,
# 2번 물건 50원, 3번 물건 120원이다.


#6 pro
# age = input("나이:")
# money = int(input("돈:"))
# price = 500

# print(money // price)
# print(money % price) 


#7 pro
# age = input("나이:")
# money = int(input("돈:"))
# prices = [1000, 50, 120]

# print(money // prices[0], money % prices[0])
# print(money // prices[1], money % prices[1])
# print(money // prices[2], money % prices[2])

# 하드 코딩 : 모든 경우의 수를 직접 찾아내는 일. 비효율적