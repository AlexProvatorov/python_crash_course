"""
Числа, кратные 10: запросите у пользователя число и сообщите, кратно
оно 10 или нет.
"""

user_number = input("Введите число и я скажу кратно оно 10 или нет: ")
user_number = int(user_number)

if user_number % 10 == 0:
    print("Число " + str(user_number) + " кратно 10!")
else:
    print("Число " + str(user_number) + " не кратно 10!")