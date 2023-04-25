# 문자열 포매팅 
# a, b = 1, 2
# result1 = str(a) + " + " + str(b) + " = " + str(a + b)
# result2 = "%d + %d + %d" % (1, 2, 1+2)
# print(result1)
# print(result2)
# result = "%d + %d + %d" % (a, b, a+b)
# print(result)

# 포맷 코드
# %s 문자열(string)
# %d 정수(int)
# %f 실수(float)
# %o 8진수
# %x 16진수
# %% % 글자 자체

# string1 = "hello"
# int1 = 3
# float1 = 1.2345
# print(("%s %d %f") % (string1, int1, float1))

# f-string
# Python 3.6 이후 버전부터 지원
# 더욱 직관적인 사용이 가능
# f"{값}"

# string1 = "hello"
# int1 = 3
# float1 = 1.2345
# result = f"{string1} {int1} {float1}"
# print(result)