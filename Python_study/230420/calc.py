

while True:
    print("""
    계산기
    =========
    1. 더하기 (+)
    2. 빼기 (-)
    3. 곱하기 (*)
    4. 나누기 (/)
    q. 계산 끝내기
    """)
    operator = input("계산을 선택하세요 : ")
    if operator == "q":
        break

    a = int(input("첫 번째 값 (a): "))
    b = int(input("두 번째 값 (b): "))
    
    if operator == "1":
        print(a,"+", b, "=" , a + b)
 
    elif operator == "2":
        print(a,"-", b, "=" , a - b)
 
    elif operator == "3":
        print(a,"*", b, "=" , a * b)
 
    elif operator == "4":
        print(a,"/", b, "=" , a / b)
   


# 사용자가 가지고 있는 돈을 입력받는다.
# 구매할 수 있는 커피의 개수와 잔돈을 출력한다.
# 구매할 수 있는 음료수의 개수와 잔돈을 출력한다.
# 구매할 수 있는 콜라의 개수와 잔돈을 출력한다.
# 커피 500, 음료 700, 콜라 930원
# 물품의 개수는 무한하다고 가정한다.
# while 사용


idx = 0
prices = [500, 700, 930]
money = int(input("돈:"))

while idx < len(prices):
# or while idx <= 2:
    price = prices[idx]
    print(money // price)
    print(money % price)
    idx += 1
