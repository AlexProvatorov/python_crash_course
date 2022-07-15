"""
Числа, кратные 10: запросите у пользователя число и сообщите, кратно оно 10 или нет.
"""

user_input = input("Введите число: ")
user_input = int(user_input)

remainder = user_input % 10

if remainder == 0:
    print("Число " + str(user_input) + " - кратно 10.")
else:
    print("Число " + str(user_input) + " - не кратно 10.")