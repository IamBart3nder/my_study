# my_calculator 모듈의 MyCalculator 클래스를 상속 받아서
# MaxLimitCalculator 클래스를 정의
# add, sub, mul, div 메소드를 사용하여
# 덧셈, 뺄셈, 곱셈, 나눗셈을 할 수 있다.
# 0으로 나누었을 때 에러가 발생하지 않도록 처리한다
# 입력되는 정수가 1개라도 100보다 크면 계산하지 않고
# 100 이하의 값을 입력하도록 안내 메시지를 출력한다.
# 계산 결과가 100보다 크면 계산하지 않고 
# 100이하의 결과가 나오는 값을 입력하도록 안내메시지를 출력한다

from my_calculator_class import MyCalculator
class MaxLimitCalculator(MyCalculator):
    def __init__(self):
        pass
        
    def add(self, n1, n2):
        if n1 and n2 >= 100:
            print("100 이하의 정수를 입력해주세요. ")
        elif n1 + n2 >= 100:
            print("100 이하의 값이 나오는 정수를 입력해주세요. ")
        else:
            print(f"{n1} + {n2} = {n1 + n2}")
            
    def sub(self, n1, n2):
        if 100 <= n1 and n2:
            print("100 이하의 정수를 입력해주세요. ")
        else:
            print(f"{n1} - {n2} = {n1 - n2}")

    def mul(self, n1, n2):
        if n1 and n2 >= 100:
            print("100 이하의 정수를 입력해주세요. ")
        elif n1 * n2 >= 100:
            print("100 이하의 값이 나오는 정수를 입력해주세요. ")
        else:
            print(f"{n1} * {n2} = {n1 * n2}")

    def div(self, n1, n2):
        if n1 and n2 >= 100:
            print("100 이하의 정수를 입력해주세요. ")
        elif n2 == 0:
            try: 
                n1 / n2
            except:
                print("0으로 나눌 수 없습니다.")
        else:
            print(f"{n1} / {n2} = {n1 / n2}")

max_limit_calculator = MaxLimitCalculator()
max_limit_calculator.sub(10,100)