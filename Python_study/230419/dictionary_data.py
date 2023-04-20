# dictionary 딕셔너리 자료형
# key-value 형태
# {key: value}
# 같은 역할을 하는 명령어가 다른 언어에도 존재.
# python에서는 dictionary

# person = {
#     "이름": "이름", 
#     "나이": 18, 
    
#     "점수": {
#     "영어": 80,
#     "국어": 90, 
#     "수학": 100
#     },
#     1: "문자"
# }
# print(person["나이"])
# print(person["점수"]["영어"])

# dict_1 = {1: 'a',}
# dict_1['b'] = 2 # 'b' = 2 key-value 쌍 추가
# dict_1[1] = 'c' # key 1의 value가 'c'로 변경
# del dict_1[1]   # key 1과 해당하는 value를 삭제
# print(dict_1)

dict_2 = {1: 'a', 2: 'b', 3: 'c'}
# keys()
# 딕셔너리에서 key값만 리스트형태로 가져옴
# print(dict_2.keys())

# values()
# 딕셔너리에서 values값만 리스트형태로 가져옴
# dict_values = dict_2.values()
# print(dict_values)

# items()
# 딕셔너리에서 key-value 쌍을 튜플로 묶은 값을 리스트 형태로 돌려줌
dict_items = dict_2.items()
# print(dict_items)

# get(key)
# key에 대응되는 value를 돌려준다.
# key값이 존재하지 않으면 None을 돌려준다.
# None = Null, 데이터가 없다 라는 의미의 데이터

# dict_2["나이"]
# print(dict_2.get("나이"))
# print(dict_2.get("나이", "나이 불명"))
    # get(a, b) = a 가 None인 경우 b의 값을 돌려줌

# clear()
# 딕셔너리 안의 모든 요소를 삭제한다.
dict_2.clear()
print(dict_2)
