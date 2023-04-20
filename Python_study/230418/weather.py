weather = "맑음" # weather 변수에 값 할당
print("비가 오나요?", weather == "비") # 비가 오나요? True 출력
if weather == "비": # weather의 값이 "비"와 같으면 조건식이 True이므로 안쪽 코드 블록 실행
    print("우산을 가져간다.")
elif weather == "맑음": #elif의 조건이 옳다면 else까지 넘어가지 않는다.
    print("날씨가 좋다.")
else: # False 면 실행
    print("우산을 가져가지 않는다.")
