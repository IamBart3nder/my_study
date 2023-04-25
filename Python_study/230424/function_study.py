# function 함수
# 입력 -> 처리 -> 출력
# input(입력)을 받아서
# 특정 작업(처리)을 수행하고
# output(출력)을 반환한다

# 내장 함수 (built-in)
# 파이썬이 기본적으로 제공하는 함수
# print()
# len()
# zip()
# int()
# float()
# str()
# list()
# range()

# abs()
# absolute의 약자
# 입력한 숫자형 데이터의 
# 절댓값을 반환한다.
# print(abs(100)) # 100
# print(abs(-253))  # 253 


# sum(리스트)
# 리스트 안의 숫자를
# 더한 값을 반환한다.
# print(sum([1, 2, 3, 4, 5])) # 15

# max(리스트)
# 리스트 안에서 최댓값을
# 찾아 반환한다.
# print(max([1, 2, 3, 4, 5])) # 5

# min(리스트
# 리스트에서 최솟값을
# 찾아 반환한다.
# print(min([1,2,3,4,5]))

# chr()
# 정수를 입력받고 해당하는
# 유니코드 문자를 반환한다.
# print()

# ord(#)
# 문자 한 개를 입력받고
# 해당하는 정수를 반환
# print(ord('A')) # 65


# round(값, 소수 자릿수 = 0)
# round(값, 소수자릿수)
# 반올림 함수
# print(round(1.234))
# print(round(1.234, 2)) # 1.23
# print(round(1.369, 1)) # 1.4



# 함수 정의(define)
# 함수 이름 
# 함수 입력값 parameter
# 함수 결괏값 return value
'''
def 함수이름(함수입력값):
     함수기능코드
     return 함수 결괏값
'''
# def는 함수를 정의하는 명령어(함수 제작)
# 함수 이름도 변수 이름처럼
# 규칙을 지켜서 지어야한다.
# 영어, 숫자, _만 사용.
# 띄어쓰기 사용 
# 키워드 사용 불가능
# 숫자로 시작 불가능
# 기존에 이미 정의된 함수 이름도
# 피하는 것이 좋음

# def print_names():
#     print("손흥민") 
#     print("황희찬")
#     print("김민재")
#     print("이강인")

# print_names()

# def get_name():
#     return "정영도"

# def print_my_name():
#     print(get_name())

# print_my_name()

# print_my_name()
# a = print_names()
# b = get_name()
# print(a)
# print(b)


# # parameter
# # 함수에 입력하는 값
# # 매개변수, argument 혼용
# def add(a,b):
#     return a + b

# def print_add(a, b):
#     print(a+b)

# result = add(1, 2)
# print(result)


# print_add ("안녕", "하세요")
# print_add (1, 2)
# print_add ("안녕", 2)
# print_add (1, "하세요")

# print_add (b = '하세요', a = '안녕')


# def swap_number(a, b):
# # 딱 그 지역에서만 
# # 지역 변수, 로컬 바리에이블
#     temp = a
#     a = b
#     b = temp
#     print(a, b)
#     return a, b
    

# # 전역 변수, 글로벌 바리에이블
# a = 1
# b = 2

# print("함수 호출 전", a, b)
# a, b = swap_number(a, b)
# print("함수 호출 후", a, b)


# 다음 함수를 정의하세요.
# 함수 이름 : mul
# 함수 입력값 : 정수 2개
# 함수 출력값 : 정수 2개의 곱


# def mul(a, b):
#     return a*b
    
# #1
# print(mul(3, 5))
# #2
# result = mul(3,5)
# print(result)

# # 함수 기본값 매개변수
# # default value parameter
# # 함수 호출 시 n2에 입력된 값이 없으면 기본 값 사용
# # def mul(n1, n2=1):
# #     return n1 * n2

# # mul(1, 2)
# # mul(1)


# # def test_func(x , test=5):
# #     test = test
# #     print(x, test)


# # test_func(1)
# # test_func(2)


# # def test_func2(x, test=None):
# #     if test == None:
# #         test = []
# #     test.append(x)
# #     print(x,test)


# # 기본값이 있는 매개변수는
# # 기본값이 없는 매개변수보다
# # 뒤에 위치해야함

# # def sub(n1, n3, n2=0):
# #     print(n1 - n2 - n3)

# # 1 ~ 10까지 더한다
# # *를 사용한 매개변수
# # 입력값이 몇개가 될지
# # 모를 때(안 정해졌을 때)
# def add_many(*args):
#     # 튜플 처럼 사용
#     # 인덱싱, 슬라이싱
#     result = 0
#     for i in args:
#         result += i
#     return result

# # result1 = add_many(1,2,3,4,5)
# # print(result1)

# # result2 = add_many(3, 2, 5 , 9, 1)
# # print(result2)

# # result3 = add_many(1, 2)
# # print(result3)

# def calc_many(*args, n1):
#     result = n1
#     for i in args:
#         result += i
#     return n1




# # 키워드 매개변수
# # **kwargs
# # keyword arguments
# # 딕셔너리로 사용

# def print_kwargs(**kwargs):
#     print(kwargs)

# print_kwargs(a=1, b=2)
# print_kwargs(name='이름', age = 10)


# # 함수의 반환
# # return 반환값
# # 리턴을 만나면 반환값을 반환함과 동시에
# # 함수가 종료된다.

# def test_func5():
#     print(1)
#     print(2)
#     return None
#     print(3)
#     print(4)
#     print(5)
    
# # 함수의 반환값은 무조건 1개이다.
# def test_func6(a, b):
#     a + b, a* b
#     # return (a + b, a * b)
#     return a+b, a*b
# result = test_func6(1, 2)
# res_add, res_mul = test_func6(1,2)
# # res_add, res_mul = (a+b),(a*b)