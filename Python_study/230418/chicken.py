age = 20
money = 35000
chicken = 20000
beer = 10000
drink = 5000

# 오리지널 (틀림)
# if money >= chicken:
#     print("치킨을 먹는다.")
# if money >= beer and age >= 20:
#     print("맥주를 먹는다")
# if money >= drink:
#     print("음료수를 먹는다.")

# 1
# if money >= chicken:
#     print("치킨을 먹는다.")
# if money - chicken >= drink:
#     print("음료수를 먹는다.")
# if money - chicken - drink >= beer and age >= 20:
#     print("맥주를 먹는다")


# # teacher 1
# # if money >= chicken:
# #     money = money - chicken
# #     print("치킨을 먹는다.")
# # if money >= beer and age >= 20:
# #     money = money - beer
# #     print("맥주를 먹는다")
# # if money >= drink:
# #     money = money - drink
# #     print("음료수를 먹는다.")

# # teacher 2
# if money >= chicken + beer + drink and age >= 20:
#     print("치킨, 맥주, 음료수 먹는다.")
# elif money >= chicken + beer and age >= 20:
#     print("치킨, 맥주 먹는다")
# elif money >= chicken + drink:
#     print("치킨, 음료수 먹는다.")  
# elif money >= chicken:
#     print("치킨 먹는다")
# elif money >= beer + drink and age >= 20:
#     print("맥주, 음료수 먹는다.")
# elif money >= beer and age >= 20:
#     print("맥주 먹는다.")
# elif money >= drink:
#     print("음료수 먹는다.")

# # 1-1
# if money >= chicken:
#     print("치킨을 먹는다.")
#     if money - chicken >= drink:
#         print("음료수를 먹는다.")
#         if money - chicken - drink >= beer and age >= 20:
#             print("맥주를 먹는다")