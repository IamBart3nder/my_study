# tuple(튜플) 형
# 소괄호
# 튜플은 element값 수정이 불가능
# mutable / immutable
# mutable 수정 가능한
# list, dict
# immutable 수정 불가능
# int, float, str, tuple

# my_list = [1, 2, 3]
# my_list[0] = 5
# print(my_list) # 5, 2, 3

# my_tuple = (1, 2, 3)
# my_tuple[0] = 5
# print(my_tuple) # Error 튜플형은 수정 불가능

tuple_1 = ('hello', 'world', 'Python')
t2 = (1, 2, 3, 4, "오")
t3 = (1, 2, 'hello')
t4 = 1, 2, 3
t5 = (1, 2, (3, 4, 5))

# + (값을 연결)
t6 = tuple_1 + t2
# * 
#t7 = t3 * 3 (반복 연산)
t7 = t3 * 4

# r값을 더하는게 아닌 반복 

# print(t3[2])
# print(t3[0:2])
# print(len(t3))

print(t5[2][1])

t8 = (5, 3 ,1 ,4, 2)
# 정렬 등 값이 바뀌기에 수정불가능
for i in t8:
    print(i)
# 순서 중요



