# while 반복문을 사용해서 
# scores 리스트에 시험 점수 5개를
# 정수형으로 입력받으세요


# #pro
# scores = []
# n = 0
# while n < 5:
#     score = int(input("시험점수:"))
#     scores.append(score)
#     n += 1
# print(scores)


# while 반복문을 사용하여
# 구구단 2단을 출력하세요.

n = 2 
while n < 20:
    print(n)
    n += 2

n = 1
while n < 10:
    print("2 *", n, "=", 2*n)
    n += 1




























# while True:
#     print("""
#     성적 입력 시스템
#     =========
#     1. 국어
#     2. 영어 
#     3. 수학
#     4. 사회
#     5. 과학
#     6. 전체 성적 확인
#     q. 입력 종료 
#     """)

#     scores = []

#     operator = input("과목을 선택하세요: ")
#     if operator == "q":
#         break

#     a = input("점수: ")

#     if operator == "1":
#         print("국어: ",a)
#         scores.insert(0,a)

#     elif operator == "2":
#         print("영어: ",a)
#         scores.insert(1,a)
        
#     elif operator == "3":
#         print("수학: ",a)
#         scores.insert(2,a)
        
#     elif operator == "4":
#         print("사회: ",a)
#         scores.insert(3,a)
        
#     elif operator == "5":
#         print("과학: ",a)
#         scores.insert(4,a)