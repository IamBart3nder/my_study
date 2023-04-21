#1

# 정수를 입력받고
# 그 정수보다 작은 수 중 
# 가장 큰 제곱수를
# 출력하세요.

# n = int(input("정수 : "))
# a = 1
# while True:
#     if a * a >= n: # = a ** 2
#         break
#     answer = a ** 2
#     a += 1
# print(answer)




#1-2 제곱근 사용 방법
## (n*n) ** 0.5) = n 

# n = int(input("정수 : "))
# a = n - 1
# b = a ** 0.5
# print(int(b))


#2
# [1, 2, 3, 4, 5]
# [10, 20, 30, 40 ,50]
# [532, 5941, 54682, 58, 5]
# 3개의 리스트에서 같은 인덱스의 -
# 값끼리 더하여 출력하세요

# a = [1, 2, 3, 4, 5]
# b = [10, 20, 30, 40 ,50]
# c = [532, 5941, 54682, 58, 5]
# g = [1, 2, 3, 4, 5]
# d = 0

#2 me
# while True:
#     if d > 4:
#         break
#     print(a[d] + b[d] + c[d])
#     d += 1

    
#2 pro    
# for i in range(5):
#     print(a[i] + b[i] + c[i])

# zip()
# 길이가 같은 list를 묶어서 for문 등으로 사용 가능한
# iterable을 반환한다.

#2-2 pro
# for x, y, z in zip(a, b, c):
#     print(x + y + z)

#2-3 pro 
# while d < 5:
#     print(a[d] + b[d] + c[d])
#     d += 1


#3
# 정수를 입력받고 1부터 입력받은 
# 정수까지 모두 출력하세요
# 단 숫자에 3, 6, 9가 들어있는 경우
# 숫자 대신 짝 이라고 출력하세요

#3 me 
# a = int(input("정수 : "))

# for b in range(1, a+1):
#     c = 1
#     if b == 3:
#         c += 1
        
#         print("짝")
#     print(b)
    

# a = int(input("정수 : "))
# for b in range(1, a+1):
#     answer = b    
#     for c in str(b):
#         if int(c) % 3 == 0 and c != "0":
#             answer = "짝"
#             break
#     print(answer)
# str 함수 <-> int 함수

#4
# 정수를 입력받고 그 정수의 약수를
# 모두 출력하시오

#4 for
# a = int(input("정수 : "))
# for b in range(1, a+1):
#     if a % b == 0:
        # print(b)

#4 while
# a = int(input("정수 : "))
# b = 1
# while b <= a:
#     if a % b == 0:
#         print(b)
#     b += 1